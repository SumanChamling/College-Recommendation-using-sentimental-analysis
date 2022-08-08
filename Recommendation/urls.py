from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from Recommendation import views
from .views.login import Login, logout, verify
from .views.password_reset import PasswordReset
from .views.schoolfilter import schoolName
from .views.passwordchanges import ChangePassword
from .views.signup import Signup
from .views.home import homePages
from .views.review import postReview
from .views.dashboard import Dashboard
from .views.rating_collect import Rate_collect
from .views.college import College, Search
from .views.ML import GetData
from .views.CheckCategory import CheckSorC
from .views.v_about_contact import About, Contact
from .views.sname_collect import Sname_Collect
from .views.v_examform_blogs import ExamForm, Blogs
from .views.v_oldschool import PastSchool
from .views.recommend_view import Recommend
from .views.dashboardhome import DashboardHome

urlpatterns = [
    path('', homePages, name='homepage'),
    path('Dashboard/', Dashboard, name = 'dashboard'),
    path('signupages',Signup.as_view(), name = 'signuppages'),
    path('changepassword',ChangePassword.as_view(), name = 'changepassword'),
    path('dashboardhome',DashboardHome, name = 'DashboardHome'),
    path('college', College, name = 'college'),
    path('checksorc', CheckSorC, name = 'checksorc'),
    path('search', Search, name = 'search'),
    path('aboutus', About, name = 'aboutus'),
    path('contact', Contact, name = 'contact'),
    path('examform', ExamForm, name = 'examform'),
    path('blogs', Blogs, name = 'blogs'),
    path('rate', Rate_collect, name = 'rate'),
    path('sname', Sname_Collect, name = 'sname'),
    path('oldschool', PastSchool.as_view(), name = 'oldschool'),
    path('recommend', Recommend.as_view(), name = 'recommend'),
    path('login', Login.as_view(), name = 'login'),
    path('reset_user_password', PasswordReset.as_view(), name = 'reset_user_password'),
    path('logout', logout, name = 'logout'),
    path('verify/<str:token>', verify, name = 'verify'),
    path('schoolname', schoolName, name='schoolname'),
    path('review', postReview.as_view(), name='review'),
    path('reviews', GetData, name='GetData'),

    #For Admin
    path('reset_passwords/',auth_views.PasswordResetView.as_view(template_name="../templates/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


]


