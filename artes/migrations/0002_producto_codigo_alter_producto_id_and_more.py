# Generated by Django 4.2.1 on 2023-06-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
