from django import forms

from freebyte.questions.models import Answer, Question


class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='标题',
        max_length=255)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='问题描述',
        max_length=2000)
    tags = forms.CharField(
        widget=forms.TextInput(),
        label='标签',
        help_text='英文逗号分隔的标签')

    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                      queryset=Question.objects.all())
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        max_length=2000)

    class Meta:
        model = Answer
        fields = ['question', 'description']
