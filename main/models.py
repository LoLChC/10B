from django.db import models

class VisitorLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    path = models.TextField(null=True, blank=True)
    method = models.CharField(max_length=10, null=True, blank=True)
    host = models.CharField(max_length=255, null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    accept_language = models.CharField(max_length=255, null=True, blank=True)
    referer = models.TextField(null=True, blank=True)
    is_secure = models.BooleanField(default=False)
    session_key = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
