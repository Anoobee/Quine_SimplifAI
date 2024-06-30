from django.db import models
import uuid

# Create your models here.
class Chats(models.Model):
    # chat_id = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    sender = models.CharField(max_length=100)
    isUser = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.text)
    
class Report(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key= True, editable=False)
    plot = models.ImageField(upload_to = '',null = True, blank= True )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class ReportText(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.report.id)


    #   id: 1,
    #   text: "Summarize the Report",
    #   timestamp: "3 minutes ago",
    #   sender: "Anup Aryal",
    #   isUser: true,