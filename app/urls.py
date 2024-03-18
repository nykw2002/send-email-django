from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from .views import *

urlpatterns = [
    path("__reload__/",
	include("django_browser_reload.urls")),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    
    path('', Home, name='Home'),
    path('confirmEmail/', ConfirmEmail, name="confirmEmail"),
    path('welcomeToRoIMM/', WelcomeToRoIMM, name="welcomeToRoIMM"),
]
