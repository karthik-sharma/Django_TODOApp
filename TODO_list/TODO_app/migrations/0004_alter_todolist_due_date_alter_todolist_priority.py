# Generated by Django 4.2.6 on 2023-10-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_app', '0003_alter_todolist_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
