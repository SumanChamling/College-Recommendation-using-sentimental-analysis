from importlib import import_module
from django.conf import settings

# SessionStore = import_module(settings.SESSION_ENGINE).sessionStore

from django.db import models

from .AddCollege import AddColleges
from .faculty import Faculty

class Review(models.Model):

    oldschool = models.CharField( max_length=200 ,default=True, null=True, blank=True)
    schoollocation = models.CharField(max_length=200,default=True, null=True, blank=True)
    registered_email = models.EmailField(default=True, null = True)
    # register_id = models.OneToOneField(Register, on_delete=models.CASCADE, default=True)
    collegeName = models.CharField(max_length=200)
    collegeLocation = models.CharField(max_length=200)
    facultyName = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    collegeReview = models.CharField(max_length=200, null = True)
    rating = models.IntegerField(default=True, null = True, blank = True)
    Review_result = models.CharField(max_length=300, default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank=True)

    def AddReview(self):
        self.save()

    # def ReviewResult(self):
    #     self.save()

    # @staticmethod
    # def get_school_name(self):
    #     try:
    #         return Review.objects.filter(schoolname = self.schoolname)
    #     except:
    #         return False



    # @staticmethod
    # def get_review_from_data(int):
    #     try:
    #         return Review.objects.get(rating = int)
    #     except:
    #         return False

    @property
    def isExists(self):
        if Review.objects.filter(registered_email = self.registered_email):
            return True
        return False


    @property
    def isExist(self):
        if Review.objects.filter(registered_email = self.registered_email):
            return True
        return False

    @staticmethod
    def get_review_value():
        return Review.objects.all()

    @isExists.setter
    def isExists(self, value):
        self._isExists = value

