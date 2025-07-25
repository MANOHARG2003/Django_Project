from django.urls import path
from . import views

urlpatterns = [
    path("",views.post_List),
    path("contact/",views.contact),
]