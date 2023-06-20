from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    username = models.CharField(max_length=50)
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class BotInteraction(models.Model):
    message = models.CharField(max_length=100)
    response = models.TextField(blank=True)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)