from pathlib import Path

from rest_framework import serializers
from django.conf import settings
from rest_framework.exceptions import ValidationError


from .models import *


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ("title", "created_at", "created_by", "md_note")
        read_only_fields = ["created_by", "created_at"]
        
    def validate_md_note(self, md_note):
        # Extension
        if Path(md_note.name).suffix.lower() != ".md":
            raise serializers.ValidationError(
                "Only .md files are allowed."
            )

        # File size (2 MB maximum)
        if md_note.size > 5242800:
            raise serializers.ValidationError(
                "File size cannot exceed 50 MB."
            )

        # Empty file
        if md_note.size == 0:
            raise serializers.ValidationError(
                "The uploaded file is empty."
            )

        # UTF-8 encoding
        try:
            content = md_note.read()
            content.decode("utf-8")
        except UnicodeDecodeError:
            raise serializers.ValidationError(
                "File must use UTF-8 encoding."
            )
        finally:
            md_note.seek(0)

        # Reject obvious binary content
        if b"\x00" in content:
            raise serializers.ValidationError(
                "Binary files are not allowed."
            )

        return md_note
    
class NoteGrammarCheckingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = ("id",)
        