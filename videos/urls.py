from django.urls import path
from videos import views
urlpatterns =[
    path('',views.index)
]