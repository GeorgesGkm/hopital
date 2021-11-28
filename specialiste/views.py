from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required

from medecin.models import Medecin
from reception.models import Personne
from specialiste.forms import SpecialisteForm
from specialiste.models import Specialiste


def etape1_list(request):
    medecins = Medecin.objects.all()

    context = {
        'medecins': medecins,

    }
    return render(request, 'specialiste/etape_list.html', context)

def specialiste_list(request):
    specialistes = Specialiste.objects.all()

    context = {
        'specialistes': specialistes,

    }
    return render(request, 'specialiste/specialiste_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            specialistes = Specialiste.objects.all()
            data['book_list'] = render_to_string('specialiste/specialiste_list.html', {'specialistes': specialistes})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def specialiste_create(request):
    if request.method == 'POST':
        form = SpecialisteForm(request.POST)
    else:
        form = SpecialisteForm()
    return save_all(request, form, 'specialiste/specialiste_create.html')
