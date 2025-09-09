# vocabularyfunctions/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import VocabItem
from .forms import VocabItemForm
import random

@login_required
def options_view(request):
    user_vocab = VocabItem.objects.filter(user=request.user)
    form = VocabItemForm()
    if request.method == 'POST':
        if 'add_word' in request.POST:
            form = VocabItemForm(request.POST)
            if form.is_valid():
                vocab = form.save(commit=False)
                vocab.user = request.user
                vocab.save()
                return redirect('options')
        elif 'delete_last' in request.POST:
            last_vocab = user_vocab.order_by('-id').first()
            if last_vocab:
                last_vocab.delete()
            return redirect('options')
    else:
        form = VocabItemForm()
    user_vocab = VocabItem.objects.filter(user=request.user)
    return render(request, 'options.html', {'user_vocab': user_vocab, 'form': form})

@login_required
def enter_data_view(request):
    user_vocab = VocabItem.objects.filter(user=request.user)
    if request.method == 'POST':
        form = VocabItemForm(request.POST)
        if form.is_valid():
            vocab = form.save(commit=False)
            vocab.user = request.user
            vocab.save()
            form = VocabItemForm()  # reset the form after successful add
            user_vocab = VocabItem.objects.filter(user=request.user)  # refresh vocab list
            return render(request, 'options.html', {'user_vocab': user_vocab, 'form': form})
    else:
        form = VocabItemForm()
    return render(request, 'options.html', {'user_vocab': user_vocab, 'form': form})

