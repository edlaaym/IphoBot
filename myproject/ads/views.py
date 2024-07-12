from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import telebot
from .models import Ad

bot = telebot.TeleBot(settings.BOT_TOKEN)


def index(request):
    # if request.method == "POST":
        # update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        # bot.process_new_updates([update])

    return HttpResponse('<h1>Ты подключился!</h1>')



