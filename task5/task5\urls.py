from django.contrib import admin
from django.urls import path

from task.views import task5
urlpatterns = [
    path('admin/', admin.site.urls), # by default admin.site.urls will create
    path('task5', task5),

]
