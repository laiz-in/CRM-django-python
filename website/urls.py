from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register_account/', views.register_account, name='register_account'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),

]
