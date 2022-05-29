from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #TODO: notes.html
    path('notes', views.notes, name='notes'),
    path('delete_note/<int:pk>', views.delete_note, name='delete-note'),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view, name='notes-detail'),
    
    # TODO: homework
    #TODO: homework.html
    path('homework', views.homework, name='homework'), 
    
    #TODO: Functions update_homework in views.
    path('update_homework/<int:pk>', views.update_homework, name='update-homework'), 
    #TODO: Functions delete_homework in views
    path('delete_homework/<int:pk>', views.delete_homework, name='delete-homework'),
    
    
    #TODO: Youtube.html
    path('youtube', views.youtube, name='youtube'),
    
    #TODO: Todo.html
    path('todo', views.todo, name='todo'),
    
    #TODO: Functions update_todo in views
    path('update_todo/<int:pk>', views.update_todo, name='update-todo'), 
    #TODO: Functions delete_todo in views
    path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),
    
    
    #TODO: Books.html
    path('books', views.books, name='books'),
    
    #TODO: Dictionary.html
    path('dictionary', views.dictionary, name='dictionary'),

    #TODO: wiki.html
    path('wiki', views.wiki, name='wiki'),
    
    #TODO: conversion.html
    path('conversion', views.conversion, name='conversion'),
    
    #TODO:
    # path('register', views.register, name='register'),
]

