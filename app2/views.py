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
    



# OpenAI APIキーとエンドポイントを設定
openai.api_key = 'PO-ff9eWT3byCD1phldL-Ka6GhBwsxHPnO7cHmcmYz5StkIt5jFkAml1VItwt13O0iCcTDbQtHZktPbCzBh0uzA'
openai.api_base = 'https://api.openai.iniad.org/api/v1'

def chat_with_gpt(prompt):
    # ChatGPT 3.5 Turboに対して質問を送信
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': prompt},
        ]
    )

    # ChatGPTからの回答を返す
    return response['choices'][0]['message']['content']

def chat_view(request):
    if request.method == 'POST':
        # フォームからユーザーの質問を取得
        user_input = request.POST.get('user_input', '')

        # ChatGPTに質問し、回答を取得
        response = chat_with_gpt(user_input)

        # ChatGPTからの回答をテンプレートに渡して表示
        return render(request, 'app2/chat.html', {'user_input': user_input, 'response': response})

    # GETリクエストの場合、単にテンプレートを表示
    return render(request, 'app2/chat.html', {'user_input': None, 'response': None})

#PO-ff9eWT3byCD1phldL-Ka6GhBwsxHPnO7cHmcmYz5StkIt5jFkAml1VItwt13O0iCcTDbQtHZktPbCzBh0uzA
