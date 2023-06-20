from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from telegram import Bot, Update
import logging, json, websocket
logger = logging.getLogger('django')
from .models import *
from .utils import *

# Stupid fat dumb jokes

# Create your views here.
class Home(APIView):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        pass


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        bot = Bot(token=settings.CHATBOT_TOEKN)
        body = request.body.decode('utf-8') 
        update = Update.de_json(json.loads(body), bot)

        data = json.loads(body)
        logger.info(data)
        user_id = data['message']['from']['id']
        first_name = data['message']['from']['first_name']
        last_name = data['message']['from']['last_name']
        username = data['message']['from']['username']
        chat_id = data['message']['chat']['id']

        message = data['message']['text']

        topic = ""
        if message == '/stupid':
            topic = 'stupid'
        elif message == '/fat':
            topic = 'fat'
        elif message == '/dumb':
            topic = 'dumb'
        else:
            pass

        if topic != "":
            reply = get_ai_answer_via_request(f"Tell me a short joke on {topic}, the joke should be max two line joke without a question answer joke.").replace("\n", "")
        else:
            reply = "Sorr you need to choose one of the option from the menu."

        telegram_user, _ = TelegramUser.objects.get_or_create(username=username, defaults={
            'user_id': user_id,
            'first_name': first_name,
            'last_name': last_name
        })

        BotInteraction.objects.create(message=message, response=reply, user=telegram_user)

        #Update the home data

        url = f"ws://127.0.0.1:8000/ws/socker-server/"
        chatSocket = websocket.WebSocket()
        chatSocket.connect(url)

        def on_message(ws, message):
            data = json.loads(message)
            logger.info("received_data")
            logger.info(data)

        chatSocket.on_message = on_message

        chatSocket.send(json.dumps({
            'message': message
        }))

        # Reply to the message
        reply = reply.replace(" ","%20")
        url = f"https://api.telegram.org/bot{settings.CHATBOT_TOEKN}/sendMessage?chat_id={chat_id}&text={reply}"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

        return HttpResponse()
