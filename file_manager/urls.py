# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('upload/', upload_file, name='upload_file'),
    path('files/', file_list, name='file_list'),
    path('download/<int:file_id>/', download_file, name='download_file'),

]
