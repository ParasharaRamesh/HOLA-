# Generated by Django 2.1.1 on 2018-10-02 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holaserver', '0005_auto_20181002_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardetailstable',
            name='carId',
        ),
        migrations.RemoveField(
            model_name='cardetailstable',
            name='driverId',
        ),
        migrations.AddField(
            model_name='carstatustable',
            name='carId',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='holaserver.CarDetailsTable', verbose_name='carId'),
        ),
        migrations.AlterField(
            model_name='driverdetailstable',
            name='carId',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='holaserver.CarDetailsTable', verbose_name='carId'),
        ),
        migrations.AlterField(
            model_name='triptable',
            name='carId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='holaserver.CarDetailsTable', verbose_name='carId'),
        ),
    ]