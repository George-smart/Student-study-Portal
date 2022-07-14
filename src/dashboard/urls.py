from django.urls import path
from . views import *

urlpatterns = [
    path('', IntroHomeView),
    path('dashboard', DashboardView, name='dashboard'),
    path('assignment', HomeworkView, name='assignment'),
    path('delete_assignment/<int:pk>', deleteHomeWork, name='delete_work'),
    path('update_assignment/<int:pk>', UpdateHomeWork, name='update_assignment'),
    path('notes', NotesView, name='notes'),
    path('delete_note/<int:pk>', DeleteNote, name='delete_note'),
    path('note_detail/<int:pk>', NoteDetail.as_view(), name='note_detail'),
    path('assignment_detail/<int:pk>', HomeworkDetail.as_view(), name='homework_detail'),
    path('introductory-page', HomeView, name='introductory_page'),
    path('create_dashboard', DashboardCreateView.as_view(), name='create_dashboard'),
    path('book', Books, name='book'),
    path('wikipedia', Wiki, name='wikipedia'),
    path('feedback', FeedbackView.as_view(), name='feedback')

]
