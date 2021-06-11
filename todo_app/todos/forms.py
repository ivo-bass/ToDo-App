from django import forms
# from django.utils import timezone

from todo_app.todos.models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Title here'
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Enter Description here'
                }
            ),
            'due_date': forms.DateTimeInput(
                attrs={
                    'class': "form-control",
                    'type': 'datetime-local',
                }
            ),
            'priority': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'is_done': forms.CheckboxInput(
                attrs={
                    'class': 'form-check'
                }
            )
        }
