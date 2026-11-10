from django.urls import path

from .views import *

app_name = "notes"

urlpatterns = [
    path("", NoteListCreate.as_view()),
    path("<int:note_id>/check-grammar/", NoteGrammerCheck.as_view()),
    path("<int:note_id>/render/", NoteRendering.as_view()),
] 