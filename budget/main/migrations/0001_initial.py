# Generated by Django 3.2.12 on 2022-06-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('type', models.CharField(choices=[('IN', 'Income'), ('OUT', 'Out')], max_length=3)),
            ],
        ),
    ]
