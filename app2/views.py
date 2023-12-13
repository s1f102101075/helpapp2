from django.views import View
from django.shortcuts import render

from django.shortcuts import render
import openai

def my_view(request):
    openai.api_key = settings.OPENAI_API_KEY

    # OpenAI APIを使った処理

    return render(request, 'template.html')
class TrainingView(View):
    def get(self, request, *args, **kwargs):
        # 何かの処理
        some_data = "This is some data."  # 何かしらのデータを代入する
        return render(request, 'app2/training.html', {'some_data': some_data})
    
class FAQView(View):
    def get(self, request, *args, **kwargs):
        # 何かの処理
        some_data = "This is some data."  # 何かしらのデータを代入する
        return render(request, 'app2/FAQ.html', {'some_data': some_data})

class FoodView(View):
    def get(self, request, *args, **kwargs):
        # 何かの処理
        some_data = "This is some data."  # 何かしらのデータを代入する
        return render(request, 'app2/food.html', {'some_data': some_data})
    
class PlanView(View):
    def get(self, request, *args, **kwargs):
        # 何かの処理
        some_data = "This is some data."  # 何かしらのデータを代入する
        return render(request, 'app2/plan.html', {'some_data': some_data})
