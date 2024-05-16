import requests

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt

# parsing data from the client
from rest_framework.parsers import JSONParser

from .models import Quote, SimpleAuthor, SimpleReference

KWOTES_API_KEY = ""

@csrf_exempt
# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the api index.")

@csrf_exempt
def recent(request):
  latest_quote_list = Quote.objects.order_by('-created_at')[:5]
  
  data = {
    'response': {
      'quotes': list(latest_quote_list.values('id', 'author__id', 'author__name', 'created_at', 'language', 'name', 'reference__id', 'reference__name', 'updated_at')),
    }
  }

  return JsonResponse(data, safe=False)

@csrf_exempt
def recentcloud(request):
  url = f"https://us-central1-memorare-98eee.cloudfunctions.net/api/v1/quotes?orderBy=created_at"
  headers = {"Accept": "application/json", "Authorization": KWOTES_API_KEY}
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    data = response.json()
    return JsonResponse(data)
  else:
    return HttpResponse("Error: " + str(response.status_code))


@csrf_exempt
def search(request):
  q: str = request.GET.get('q')
  page: int = request.GET.get('page')
  limit: int = request.GET.get('limit')

  if not q:
    return HttpResponse("Error: q is required")
  
  if not page:
    page = 0
  
  if not limit:
    limit = 12

  author = SimpleAuthor.objects.filter(name__icontains=q).first()
  latest_quote_list = Quote.objects.filter(author=author).order_by('-created_at')

  if not latest_quote_list:
    reference = SimpleReference.objects.filter(name__icontains=q).first()
    latest_quote_list = Quote.objects.filter(reference=reference).order_by('-created_at')
  
  data = {
    'response': {
      'quotes': list(latest_quote_list.values('id', 'author__id', 'author__name', 'created_at', 'language', 'name', 'reference__id', 'reference__name', 'updated_at')),
    }
  }
  
  return JsonResponse(data, safe=False)

@csrf_exempt
def searchcloud(request):
  q: str = request.GET.get('q')
  page: int = request.GET.get('page')
  limit: int = request.GET.get('limit')

  if not q:
    return HttpResponse("Error: q is required")
  
  if not page:
    page = 0
  
  if not limit:
    limit = 12

  url = f"https://us-central1-memorare-98eee.cloudfunctions.net/api/v1/search/quotes?q={q}&page={page}&limit={limit}"
  headers = {"Accept": "application/json", "Authorization": KWOTES_API_KEY}
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    data = response.json()
    return JsonResponse(data)
  else:
    return HttpResponse("Error: " + str(response.status_code))
