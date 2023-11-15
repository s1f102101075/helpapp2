from django.urls import path
from accounts import views
from app2 import views

urlpatterns = [
    path('training/', views.TrainingView.as_view(), name='training'),
    path('FAQ/', views.FAQView.as_view(), name='FAQ'),
    path('plan/', views.PlanView.as_view(), name='plan'),
    path('food/', views.FoodView.as_view(), name='food'),
]