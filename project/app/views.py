from django.shortcuts import render, HttpResponse, redirect
from .models import ImageModel

# Create your views here.
def index(request):
  uploaded_image = request.FILES.get('image')
  if uploaded_image:
    image_instance = ImageModel(image=uploaded_image)
    image_instance.save()

    image_url = image_instance.image.url
    return render(request, 'image.html', {'image_url': image_url})
  
  else:
    return render(request, 'index.html')

def upload_success(request):
  return HttpResponse('성공하셨네요')