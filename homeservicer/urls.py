from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("basic", views.basic, name="basic"),
   path("about", views.about, name="about"),
   path("contact", views.contact, name="contact"),
   path("signin", views.signin, name="signin"),
   path("signup", views.signup, name="signup"),
   path("viewdata", views.viewdata, name="viewdata"),
   path('checkuser', views.checklogin, name='checkuser'),
   path('logout', views.logout, name='logout'),
   path('profile', views.yourprofile, name='profile'),
   path('allservices', views.allservices, name='allservices'),
   path('myservices', views.myservices, name='myservices'),
   path('completeprofile', views.completeprofile, name='completeprofile'),
   path('completeprofilesubmit', views.completeprofilesubmit, name='completeprofilesubmit'),
   path('addservice', views.addservice, name='addservice'),
   path('editservice/<int:service_id>', views.edit_service_view, name='editservice'),
   path('servicesubmit', views.servicesubmit, name='servicesubmit'),
   path('editservicesubmit', views.editservicesubmit, name='editservicesubmit'),
   path('userbookings', views.userbookings, name='userbookings'),
   path('viewagentbookings', views.viewagentbookings, name='viewagentbookings'),
   path('SubmitReview', views.SubmitReview, name='SubmitReview'),
   path('deleteserv/<int:dsid>',views.deleteserv,name="deleteserv"),
   path('bookservice',views.bookservice,name="bookservice"),
   path('acceptbooking/<int:abid>',views.acceptbooking,name="acceptbooking"),
   path('rejectbooking/<int:rbid>',views.rejectbooking,name="rejectbooking"),
   path('cancelbooking/<int:cbid>',views.cancelbooking,name="cancelbooking"),
   path('servicesingle/<int:ssid>',views.servicesingle,name="servicesingle"),
   path('catwiseservice/<int:cwsid>',views.catwiseservice,name="catwiseservice"),
   path('searchservice',views.searchservice,name="searchservice"),
   path('feedback.html', views.feedbackpage, name="feedbackpage"),
   path('storefeedback', views.storefeedback, name="storefeedback"),
   path("viewDetails/<int:id>", views.viewDetails, name="viewDetails"),
   path("create_order", views.create_order, name="create_order"),
   path("forgotpasswordpage", views.forgotpasswordpage, name="forgotpassword"),
   path("forgotpassword", views.forgotpassword, name="forgotpassword"),
   path("editprofile", views.editprofile, name="editprofile")
]