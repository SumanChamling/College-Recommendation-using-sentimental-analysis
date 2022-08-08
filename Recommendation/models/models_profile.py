from django.db import models

class Models_Profile(models.Model):
    email = models.EmailField(max_length=100, default=True, null=True, blank=True)
    email_token = models.CharField(max_length=100, default=True, blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['email']

    def saveProfile(self):
        self.save()