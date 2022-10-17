import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from ads.models import Ad, Category


@method_decorator(csrf_exempt, name='dispatch')
class main(View):
    def get(self, request):
        response = {"status": "ok"}
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatListView(ListView):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for category in categories:
            response.append({
                'id': category.pk,
                'name': category.name
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        cat = Category.objects.create(**data)
        return JsonResponse({
            'id': cat.id,
            'name': cat.name
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk, 'name': cat.name}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
    def get(self, request):
        ads = Ad.objects.all()
        response = []
        for ad in ads:
            response.append({
                'id': ad.pk,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        ad = Ad.objects.create(**data)
        return JsonResponse({'id': ad.pk,
                             'name': ad.name,
                             'author': ad.author,
                             'price': ad.price,
                             'description': ad.description,
                             'address': ad.address,
                             'is_published': ad.is_published
                             }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({'id': ad.pk,
                             'name': ad.name,
                             'author': ad.author,
                             'price': ad.price,
                             'description': ad.description,
                             'address': ad.address,
                             'is_published': ad.is_published
                             }, safe=False)
