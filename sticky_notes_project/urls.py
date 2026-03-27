from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from notes import views as notes_views

urlpatterns = [
    path('admin/', admin.site.urls),                    # Admin panel
    
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', notes_views.register_view, name='register'),
    
    # Notes app k URLs
    path('notes/', include('notes.urls')),
    
    # Root url http://127.0.0.1:8000/ ko notes list pe redirect kr diya
    path('', lambda request: redirect('note_list')),
]