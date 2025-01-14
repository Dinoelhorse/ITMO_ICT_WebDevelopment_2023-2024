# Generated by Django 4.2.6 on 2023-12-18 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_remove_subjects_fio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1000, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teachers',
            name='cabinet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school_app.cabinets'),
        ),
    ]
