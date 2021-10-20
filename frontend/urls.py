from django.urls import path 
from .views import *

urlpatterns = [
	path('', index),
	path('<str:page_request>/', render_page)
]