from django.db import models

# Create your models here.

class Task(models.Model):
    status_choice = [("Pending","Task_Pending"),
                   ("In Progress","Task_In Progress"),
                   ("Completed","Task_Completed")]
    # id = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(default='',null=True,max_length=50)
    due_date = models.DateTimeField(null = True)
    # status = models.Choices(status_choice)
    status = models.CharField(max_length=20, choices=status_choice, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



