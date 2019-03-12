from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from mcstatus import MinecraftServer
import os

server = MinecraftServer.lookup('mc.unlogic.ru:25565')

def main_page(request):
    try:
        players_online = str(get_online()) + '/50'
    except Exception as e:
        print(e)
        players_online = "Введутся технические работы"
    context ={
        'online': players_online,
    }
    return render(request, 'index.html', context)

@staff_member_required
def server_query(request):
    if request.method == 'POST':
        query = request.POST['query']
        return HttpResponse(query_server(query))
    elif request.method == 'GET':
        return render(request, 'admin.html')


def query_server(query):
    return 'Консоль больше не работает'


def get_online():
    status = server.status()
    return status.players.online
