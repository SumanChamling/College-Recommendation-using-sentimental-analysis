from django.contrib import admin
from .models.collegereview import Review
from .models.faculty import Faculty
from .models.register import Register
from .models.models_profile import Models_Profile
from .models.AddCollege import AddColleges
from .models.m_oldschool import oldSchool
from .models.review_college_mtom import Review_College


class AdminReview(admin.ModelAdmin):
    list_display = ['id', 'oldschool','schoollocation', 'collegeName', 'collegeLocation', 'facultyName', 'collegeReview','rating' ,'registered_email','Review_result']


class AdminFaculty(admin.ModelAdmin):
    list_display = ['name']

class AdminRegister(admin.ModelAdmin):
    list_display = ['id','school_id','name','email','password','address','phone','date_created']

class AdminAddCollege(admin.ModelAdmin):
    list_display = ['name','address','phone','description','website','image']

class AdminOldSchool(admin.ModelAdmin):
    list_display = ['pastSchool','address','student_email']

class AdminCollege_Review(admin.ModelAdmin):
    list_display = ['addcollege_id', 'collegereview_id']

class AdminCollege_Profile(admin.ModelAdmin):
    list_display = [ 'email','email_token','is_verified']


# Register your models here.
admin.site.register(Review, AdminReview)
admin.site.register(Faculty, AdminFaculty)
admin.site.register(Register, AdminRegister)
admin.site.register(AddColleges, AdminAddCollege)
admin.site.register(oldSchool, AdminOldSchool)
admin.site.register(Review_College, AdminCollege_Review)
admin.site.register(Models_Profile, AdminCollege_Profile)
