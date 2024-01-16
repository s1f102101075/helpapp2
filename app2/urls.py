from django.urls import path
from accounts import views
from app2 import views
from .views import index, TrainingView, FAQView, FoodView, PlanView

# from .views import YourView

urlpatterns = [
    path('training/', views.TrainingView.as_view(), name='training'),
    path('FAQ/', views.FAQView.as_view(), name='FAQ'),
    path('plan/', views.PlanView.as_view(), name='plan'),
    path('food/', views.FoodView.as_view(), name='food'),
    path('', views.index, name='index'),
    path('index/', index, name='index'),
    # path('api/v1/', YourView.as_view(), name='your_view_name')
]