from django.contrib import admin
from django.urls import path
from xyz import views
urlpatterns = [
        path('admin/', admin.site.urls),

    path( 'home/',views.home,name=''),
    path( 'customer/',views.contact,name=''),
    path('',views.homepage),
    path('second/',views.second),
    path('test/', views.test)


]
