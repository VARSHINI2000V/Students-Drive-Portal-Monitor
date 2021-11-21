from . import views
from django.urls import path

urlpatterns=[
    path('',views.index),
    path('register/',views.register),
    path('login/',views.login),
    path('registered/',views.registering),
    path('profile/',views.logining),
    path('myprofile/',views.myprofile),
    path('updated/',views.updateprofile),
    path('logout/',views.logout),
    path('drives/',views.viewdrives),
    path('mydrives/',views.drives),
    path('placed/',views.placed),
    path('adminlogin/',views.admins),
    path('adminlogining/',views.adminlogining),
    path('adminlogout/',views.adminlogout),
    path('studentdrives/',views.admindrive),
    path('admin/placed/',views.adminplaced),
    path('admin/company/',views.newcompany),
    path('admin/addedcompany/',views.addcompanies),
    path('drives/<int:id>/',views.registerationstatus),
    path('drives/registered/',views.registerationcompany),
    path('placed/submit/',views.placedstatus),
    path('admin/companies/',views.existingcompanies),
    path('admin/companies/delete/<int:id>/',views.deletecompanies),
    path('staff/register/',views.staffregister),
    path('staff/login/',views.stafflogin),
    path('staff/registering/',views.stafflogining),
    path('staff/checklogin/',views.stafflogins),
    path('staff/home/',views.staffhome),
    path('staff/placed/',views.staffplaced),
    path('staff/studentdrives/',views.staffdrives),
    path('staff/logout/',views.stafflogout),
    path('staff/search/',views.search),
    path('staff/search/company/',views.searching),
    path('admin/search/',views.adminsearch),
    path('admin/search/company/',views.adminsearching),
    path('about/',views.about)


]