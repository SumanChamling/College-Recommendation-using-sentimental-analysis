from django.db import models


class oldSchool(models.Model):
    pastSchool = models.CharField(max_length=200)
    student_email = models.EmailField(default=True)
    address = models.CharField(max_length=200)
    # SEE_Students = models.BooleanField(blank=True, null=True)
    # PlusTwo_Students = models.BooleanField(blank=True, null=True)


    def __str__(self):
        return self.pastSchool


    @property
    def email_check(self):
        if oldSchool.objects.filter(student_email=self.student_email):
            return True
        return False


    def SaveOldSchool(self):
        self.save()


