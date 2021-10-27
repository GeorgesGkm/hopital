from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from reception.forms import PersonneForm
from reception.models import Personne


def book_list(request):
    persons = Personne.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'book_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            persons = Personne.objects.all()
            data['book_list'] = render_to_string('book_list_2.html', {'persons': persons})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
    else:
        form = PersonneForm()
    return save_all(request, form, 'book_create.html')
