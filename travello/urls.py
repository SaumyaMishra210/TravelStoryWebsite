from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    # path('travello-regs/',views.register,name= 'register'),
    # path('intro',views.intro, name = 'intro')
]