from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from .forms import MessageForm

@login_required
def room_list(request):
    rooms = Room.objects.filter(users=request.user)
    return render(request, 'room_list.html', {'rooms': rooms})

@login_required
def room_chat(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    messages = Message.objects.filter(room=room).order_by('-timestamp')[:50]
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = room
            message.sender = request.user
            message.save()
            return redirect('room_chat', room_id=room_id)
    else:
        form = MessageForm()
    return render(request, 'room_chat.html', {'room': room, 'messages': messages, 'form': form})

# @login_required
# def new_message(request, room_id):
#     room = get_object_or_404(Room, id=room_id)
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.room = room
#             message.sender = request.user
#             message.save()
#             return redirect('room_chat', room_id=room_id)
#     else:
#         form = MessageForm()
#     return render(request, 'new_message.html', {'room': room, 'form': form})
