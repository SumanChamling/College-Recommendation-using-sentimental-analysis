from django.db import models

from .faculty import Faculty

class AddColleges(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    phone = models.IntegerField()
    description = models.CharField(max_length=499, null=True)
    facultyName = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    website = models.URLField(max_length=100)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['college_id']


    @staticmethod
    def get_all_college():
        return AddColleges.objects.all()
    
    # @staticmethod
    # def get_school_name(id):
    #     return AddColleges.objects.get(id = id )


    # def get_session_college(self):
    #     return AddColleges.objects.get(pk=name)