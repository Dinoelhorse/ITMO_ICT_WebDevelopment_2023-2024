# Generated by Django 4.2.6 on 2023-12-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0006_alter_classes_classroom_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='subject',
            field=models.CharField(choices=[('Math', 'Математика'), ('Physics', 'Физика'), ('Arts', 'Искусства'), ('Music', 'Музыка'), ('Chemisty', 'Химия'), ('Sports', 'Физра'), ('Languanges', 'Языки'), ('Literature', 'Литература')], max_length=50, verbose_name='Название'),
        ),
    ]