from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def send(request):
    return render(request, "send.html")


def deliver(request):
    return render(request, "deliver.html")
