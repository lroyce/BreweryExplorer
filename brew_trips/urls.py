from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('save/',views.save,name='save'),
path('brewmap/',views.brewmap,name='brewmap'),
path('<int:id>/delete/',views.delete, name='delete'),

# path('update/',views.update,name='update'),
]
