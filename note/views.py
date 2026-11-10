from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
import markdown

from .serializers import *
from .models import *
from .services.grammer_checker import check_grammar
from .services.markdown_to_html_renderer import markdown_renderer


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Note.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class NoteGrammerCheck(APIView):

    def post(self, request, note_id, *args, **kwargs):
        note = Note.objects.get(id=note_id)

        file = note.md_note

        text = file.read().decode("utf-8")
        matches = check_grammar(text)

        errors = [
            {"message": match.message, "replacements": match.replacements}
            for match in matches
        ]

        return Response({"has_errors": bool(errors), "errors": errors})


class NoteRendering(APIView):
    def get(self, request, note_id, *args, **kwargs):
        note = Note.objects.get(id=note_id)

        file = note.md_note
        file_content = file.read().decode("utf-8")

        html = markdown_renderer(file_content)
                
        return Response({
            "html": html
        })
