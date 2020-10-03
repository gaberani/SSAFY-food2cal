# Generated by Django 3.1.1 on 2020-10-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('ammount', models.IntegerField()),
                ('calorie', models.IntegerField()),
                ('carbohydrate', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fat', models.IntegerField()),
            ],
        ),
    ]
