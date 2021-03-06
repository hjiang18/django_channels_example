import random
import string
import haikunator
from django.db import transaction
from django.urls import reverse
from django.shortcuts import render, redirect
from chatroom.models import Room

def about(request):
    return render(request, "chatroom/about.html")

def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = haikunator.Haikunator().haikunate()
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect(reverse('chatroom:chat_room', args=(label,)))

def chat_room(request, label):
    """
    Room view - show the room, with latest messages.
    The template for this view has the WebSocket business to send and stream
    messages, so see the template for where the magic happens.
    """
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chatroom/room.html", {
        'room': room,
        'messages': messages,
    })
