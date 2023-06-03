from django.urls import path, include
from rest_framework import routers
from veterinaria import views

router = routers.DefaultRouter()
router.register('Animal', views.AnimalViewSet)

urlpatterns = [

    path('',include(router.urls))

]