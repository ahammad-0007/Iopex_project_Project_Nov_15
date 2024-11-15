# Generated by Django 5.1.3 on 2024-11-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=50, null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Task_Pending'), ('In Progress', 'Task_In Progress'), ('Completed', 'Task_Completed')], default='', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
