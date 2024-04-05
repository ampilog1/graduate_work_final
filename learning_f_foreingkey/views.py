from django.shortcuts import render
from .forms import *
from accounts.models import *
from .models import *


def send_to_santa_views(request):
    if request.method == 'POST':
        form = text_to_send(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                send_local = send_to_santa()
                send_local.text = form.cleaned_data.get('text_to_send')
                send_local.owner = request.user
                send_local.save()
            context = {'form': form}
            return render(request, 'learning_f_foreingkey/send_to_santa.html', context)
    form = text_to_send()
    context = {'form': form}
    return render(request, 'learning_f_foreingkey/send_to_santa.html', context)
# Create your views here.
