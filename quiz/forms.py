from django import forms
from .import models


class Add_question(forms.ModelForm):
    class Meta:
        model=models.Question
        fields=["question_text","option1","option2","option3","option4","answer","subject","chapter","subtopic","exam"]
