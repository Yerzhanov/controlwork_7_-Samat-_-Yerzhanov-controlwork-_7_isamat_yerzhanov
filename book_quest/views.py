from django.shortcuts import render, redirect, get_object_or_404
from book_quest.forms import *
from book_quest.models import *


def index(request):
    context = {
        'title': 'Добро пожаловать',
    }
    return render(request, 'index.html', context)


def records(request):
    records = GuestBook.objects.filter(status='ACTIVE').order_by('-date_created')
    return render(request, 'records.html', {'records': records})

def view_all(request):
    records = GuestBook.objects.filter().order_by('-date_created')
    return render(request, 'records.html', {'records': records})


def view_record(request, record_pk):
    record = get_object_or_404(GuestBook, pk=record_pk)
    if request.method == 'GET':
        form = GuestBookForm()
        return render(request, 'view_record.html', {'record': record, 'form': form})
    else:
        try:
            form = GuestBookForm(request.POST)
            form.save()
            return redirect('records')
        except ValueError:
            return render(request, 'view_record.html', context={'record': record, 'form': form, 'error': 'Неправильно введеные данные'})


def create_record(request):
    if request.method == 'GET':
        return render(request, 'create_record.html', {'form': GuestBookForm()})
    else:
        try:
            form = GuestBookForm(data=request.POST)
            new_to_record = form.save(commit=False)
            new_to_record.save()
            return redirect('index')
        except ValueError:
            return render(request, 'create_record.html',
                          {'form': GuestBookForm(), 'error': 'Были переданы неверные данные. Попробуйте снова.'})


def delete_record(request, record_pk):
    record = get_object_or_404(GuestBook, pk=record_pk)
    if request.method == 'POST':
        record.delete()
        return redirect('index')


def update_record(request, record_pk):
    record = get_object_or_404(GuestBook, pk=record_pk)
    if request.method == 'POST':
        form = GuestBookForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('view_record', pk=record_pk)
        return render (request, 'view_record.html', context={'form': form, 'record': record})
    form = GuestBookForm(instance=record)
    return render (request, 'view_record.html', context={'form': form, 'record': record})