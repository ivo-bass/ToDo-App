from django.shortcuts import render, redirect

from todo_app.forms.form import UserForm


def show_form(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            fields = ['name', 'age', 'email', 'password', 'text']
            for field in fields:
                print(field, form.cleaned_data[field])
        else:
            print(form.errors)
        return redirect(show_form)
    else:
        context = {
            'form': UserForm()
        }
        return render(request, 'given/forms.html', context)
