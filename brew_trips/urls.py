from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('brewapi/',views.brewapi,name='brewapi'),
path('brewmap/',views.brewmap,name='brewmap'),
path('<int:id>/delete/',views.delete, name='delete'),
path('<int:id>/update/',views.update,name='update'),
]
