from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

import openai

openai.api_key = "7f5AQ030gyWL6Cbgu1GNO-fTRvLAyKgQ8Lcu10bMZnvz6UgH3fXxJgooGCP60ToYx6z3PQAc2HUo72fk2GOVMeg"
openai.api_base = "https://api.openai.iniad.org/api/v1"

def index(request):
    # Your view logic here
    return render(request, 'index.html')

def chatapi(request):
    if request.method == 'POST':
        title = request.POST['title']
        openai.api_key = "7f5AQ030gyWL6Cbgu1GNO-fTRvLAyKgQ8Lcu10bMZnvz6UgH3fXxJgooGCP60ToYx6z3PQAc2HUo72fk2GOVMeg"
        openai.api_base = 'https://api.openai.iniad.org/api/v1'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content":  "You are a helpful assistant."},
                {"role": "user", "content": f"{title}"}
            ]
        )
        ans = response['choices'][0]['message']['content']
        return JsonResponse({'answer': ans})
    else:
        return JsonResponse({'error': 'Invalid request method'})
# def index(request):
#         if request.method == 'GET':
#                 return render(request, 'chat/index.html')
#         if request.method == 'POST':
#                 title = request.POST['title']
#                 openai.api_key = "7f5AQ030gyWL6Cbgu1GNO-fTRvLAyKgQ8Lcu10bMZnvz6UgH3fXxJgooGCP60ToYx6z3PQAc2HUo72fk2GOVMeg"
#                 openai.api_base = 'https://api.openai.iniad.org/api/v1'
#                 response = openai.ChatCompletion.create(
#                     model="gpt-3.5-turbo",
#                     messages=[
#                         {"role": "system", "content":  "You are a helpful assistant."},
#                         {"role": "user", "content": f"{title}"}
#                     ]
#                 )
#                 ans = response['choices'][0]['message']['content']
#         context = {
#                 'title' : title,
#                 'ans' : ans
#                 }
#         return render(request, 'app2/FAQ.html',context)
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
