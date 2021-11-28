from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from reception.forms import PersonneForm, EntrepriseForm, ServiceForm
from reception.models import Personne, Entreprise, Service


def book_list(request):
    persons = Personne.objects.all()

    context = {
        'persons': persons,

    }
    return render(request, 'receptions/book_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            persons = Personne.objects.all()
            data['book_list'] = render_to_string('receptions/book_list_2.html', {'persons': persons})
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
    return save_all(request, form, 'receptions/book_create.html')

def book_delete(request, pk):
    book = get_object_or_404(Personne, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        books = Personne.objects.all()
        data['html_book_list'] = render_to_string('receptions/book_create.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/includes/partial_book_delete.html', context, request=request)
    return JsonResponse(data)

#  views for entreprise.
def entreprise_list(request):
    business = Entreprise.objects.all()
    context = {
        'business': business,
    }
    return render(request, 'entreprises/entreprise_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            business = Entreprise.objects.all()
            data['entreprise_list'] = render_to_string('entreprises/entreprise_list_2.html', {'business': business})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def entreprise_create(request):
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
    else:
        form = EntrepriseForm()
    return save_all(request, form, 'entreprises/entreprise_create.html')


# views for services.
def service_list(request):
    business = Service.objects.all()
    context = {
        'business': business,
    }
    return render(request, 'services/service_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            business = Service.objects.all()
            data['service_list'] = render_to_string('services/service_list_2.html', {'business': business})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
    else:
        form = ServiceForm()
    return save_all(request, form, 'services/service_create.html')


def service_update(request, pk):
    business = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=business)
    else:
        form = ServiceForm(instance=business)
    return save_all(request, form, 'services/service_update.html')


def service_delete(request, pk):
    business = get_object_or_404(Service, pk=pk)
    data = dict()
    if request.method == "POST":
        business.delete()
        data['form_is_valid'] = True
        business = Service.objects.all()
        data['service_list'] = render_to_string('services/service_list_2.html', {'business': business})
    else:
        context = {'business': business}
        data['html_form'] = render_to_string('services/service_delete.html', context, request=request)
    return JsonResponse(data)