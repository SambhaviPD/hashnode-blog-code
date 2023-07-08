from django.http  import JsonResponse
from django.shortcuts import render

from bookreviews.forms import BookReviewForm
from bookreviews.models import BookReview

import json

def home_view(request):
    return render(request, "home.html")


def api_content_list_view(request):
    content_list = [
        {"id": 1, "title": "First Content", "body": "This is the first content"},
        {"id": 2, "title": "Second Content", "body": "This is the second content"},
    ]
    return JsonResponse({"data": content_list})


def api_review_create_view(request):
    if not request.method == "POST":
        return JsonResponse('', status=400)

    data = None
    try:
        data = json.loads(request.body)
    except:
        pass
    print(data)
    form = BookReviewForm(data)
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj, request.user)
        obj.save()
        data = {
            'id': obj.id,
            'title': obj.title,
            'author': obj.author,
            'review': obj.review,
            'is_created': True
        }
        return JsonResponse(data, status=201)
    errors = json.loads(form.errors.as_json())
    return JsonResponse({"errors" : errors}, status=400)
