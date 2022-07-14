from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .form import *
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import requests
import wikipedia


def Wiki(request):
    if request.method == "POST":
        text = request.POST.get('search')
        form = SearchForm(request.POST)
        search = wikipedia.page( text)
        context = {
            'form': form,
            'title': search.title,
            'link': search.url,
            'details': search.content
        }
        return render(request, 'wikipaedia.html', context)
    else:
        form = SearchForm()
        context = {'form': form}

    return render(request, 'wikipaedia.html', context)



def Books(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = request.POST.get('search')
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink')
            }
           
            result_list.append(result_dict)

        context = {
            'form': form,
            'results': result_list
        }
        return render(request, 'materials.html', context)
    else:
        form = SearchForm()

    context = {
        'form': form
    }
    return render(request, 'materials.html', context)


def HomeworkView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HomeWorkForm(request.POST)
            if form.is_valid():
                try:
                    finished = request.POST('is_finished')
                    if finished == 'checked':
                        finished = True
                    else:
                        finished = False
                except:
                    finished = False

                Homework = HomeWorks(user=request.user, title=request.POST['title'], description=request.POST['description'], is_finished=finished)
                Homework.save()
            messages.success(request, f'{request.user.username} Assignment successufully Created')
        else:
            form = HomeWorkForm()
    
        Homework = HomeWorks.objects.filter(user=request.user)    
        if len(Homework) == 0:
            homework_done = False
        else:
            homework_done = True    
        context = {
            'homeworks': Homework,
            'form': form,
            'homework_done': homework_done
        }
        return render(request, 'assignment.html', context)
    else:
        return redirect('login')

    

def deleteHomeWork(request, pk=None):
    HomeWorks.objects.get(id=pk).delete()
    return redirect('assignment')

def UpdateHomeWork(request, pk=None):
    homework = HomeWorks.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('assignment')


def IntroHomeView(request):
    return render(request, 'home.html')

def HomeView(request):
    return render(request, 'intro.html')


def DashboardView(request):
    homework = HomeWorks.objects.filter(user=request.user)[:3]
    note = Notes.objects.filter(user=request.user)[:3]

    if homework.count() == 0:
        homework_count = False
    else:
        homework_count = True

    if note.count() == 0:
        notes_count = False
    else:
        notes_count = True

    context = {
        'homeworks': homework,
        'notes': note,
        'homeworks_count': homework_count,
        'notes_count': notes_count
    }
    return render(request, 'dashboard_home..html', context)


class DashboardCreateView(CreateView):
    form_class = DashboardForm
    template_name = 'create_dashboard.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    

def NotesView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid():
                Note = Notes(user=request.user, title=request.POST['title'], description=request.POST['description']).save()
            messages.success(request, f"{request.user.username} Your note was created successfully")
        else:
            form = NoteForm()

        Note = Notes.objects.filter(user=request.user)
        context = {
            'notes': Note,
            'form': form,
        }
        return render(request, 'notes.html', context)
    else:
        return redirect('login')

class NoteDetail(DetailView):
    model = Notes
    template_name = 'notes_detail.html'
    fields = '__all__'


class HomeworkDetail(DetailView):
    model = HomeWorks
    template_name = 'assignment_detail.html'
    fields = '__all__'

    

def DeleteNote(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')


class FeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback.html'

    success_url = reverse_lazy('dashboard')


    



