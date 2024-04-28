# Generated by Django 5.0.4 on 2024-04-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='game',
            field=models.CharField(choices=[(1, 'Unlisted'), (2, 'Magic the Gathering'), (3, 'Pokemon'), (4, 'Yu-Gi-Oh')], default=1),
        ),
        migrations.AlterField(
            model_name='deck',
            name='deckID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='deck',
            name='description',
            field=models.TextField(default='No Description'),
        ),
    ]