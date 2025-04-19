# firstapp/forms.py
from django import forms
from .models import VocabItem

class VocabItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'other_comments' in self.fields:
            self.fields['other_comments'].widget.attrs.update({
                'maxlength': '250',
                'rows': 1,
                'style': 'resize:none; min-height:2.4em; max-height:3.2em;'
            })
    class Meta:
        model = VocabItem
        fields = ['gender', 'word', 'english_meaning', 'part_of_speech', 'other_comments']