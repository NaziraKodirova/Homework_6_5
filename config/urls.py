from django.contrib import admin
from django.urls import path, include
from student import views as student_views  
from library import views as library_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_views.index, name='index'),  
    path('student/', include('student.urls')),  
    path('library/', include('library.urls')),  
]