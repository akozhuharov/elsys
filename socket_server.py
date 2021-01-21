import aqi
import requests
import os
import pickle
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from socket import (socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR)
from socket import timeout as SOCKET_TIMEOUT


class Server:
    def __init__(self, port=20000):
        self.port = port

    def get_weather(self):
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Sofia&appid=b7ef9a1647a36bdb99c857407dc5e116")
        return pickle.dumps(r.json()['weather'])

    def handler(self, connection, addr):
        pid = os.getpid()
        BUFFER = 1024
        print(f"Handling connection {pid}.")
        received = bytes()
        while True:
            try:
                data = connection.recv(BUFFER)
            except SOCKET_TIMEOUT:
                break
            received += data
            # There is an extra 33 bytes that comes through the connection
            if sys.getsizeof(data) < (BUFFER + 33):
                break
            else:
                # Set a timeout. This is needed if the data is exactly the
                # length of the buffer - in that case without a timeout
                # we will get stuck in the recv part of the loop
                connection.settimeout(0.5)
        request = pickle.loads(data)
        if request.lower() == "time":
            response = pickle.dumps("{}".format(datetime.now()))
        elif request.lower() == "weather":
            response = self.get_weather()
        elif request.lower() == "airquality":
            myaqi = aqi.to_iaqi(aqi.POLLUTANT_PM25, '12', algo=aqi.ALGO_EPA)
            response = pickle.dumps(f"Air quality index is: {myaqi}")
        else:
            response = pickle.dumps("Invalid command")
        connection.send(pickle.dumps(response))
        print(f"Returning response {response} to requester.")
        connection.close()

    def incoming(self):
        print(self.port)
        with ThreadPoolExecutor(max_workers=5) as executor:
            with socket(AF_INET, SOCK_STREAM) as sock:
                sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
                sock.bind(("0.0.0.0", self.port))
                sock.listen(10)
                print(f"Server listening on local TCP socket {self.port}")
                while True:
                    conn, addr = sock.accept()
                    executor.submit(self.handler, conn, addr)
                print("Server shutting down")


if __name__ == "__main__":
    server = Server()
    server.incoming()