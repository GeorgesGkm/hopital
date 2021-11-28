from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from medecin.forms import MedecinForm
from medecin.models import Medecin
from reception.models import Personne


def medecin_grille_list(request):
    persons = Personne.objects.all()

    context = {
        'persons': persons,

    }
    return render(request, 'medecin/grille_patient.html', context)
def medecin_list(request):
    medecins = Medecin.objects.all()

    context = {
        'medecins': medecins,

    }
    return render(request, 'medecin/medecin_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            medecins = Medecin.objects.all()
            data['book_list'] = render_to_string('medecin/medecin_list_2.html', {'medecins': medecins})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def medecins_create(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST)
    else:
        form = MedecinForm()
    return save_all(request, form, 'medecin/medecin_create.html')
