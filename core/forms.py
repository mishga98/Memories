from .models import Note
from django.forms import ModelForm, TextInput, Textarea


class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields=['title', 'note', 'person','coordinates']

        widgets = {
            'title': TextInput(
                attrs={
                    'type': "text",
                    'class': "form-control",
                    'id': "name_of_note"
                }),
            'note': Textarea(
                attrs={
                    'type': "text",
                    'class': "form-control",
                    'id': "description-text",
                    'height': "100px",

                }),
            'coordinates': TextInput(
                attrs={
                    'type': "text",
                    'class': "form-control",
                    'id': "coord_id",
                    'oninvalid':"this.setCustomValidity('Не забудьте указать точку на карте')",


                }),

        }


