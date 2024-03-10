from django.shortcuts import render, HttpResponse, redirect
from .models import ImageModel
from .utils import apply_sticker
from django.core.files.base import ContentFile


def index(request):
    uploaded_image = request.FILES.get("image")
    if uploaded_image:
        sticker_image = apply_sticker(uploaded_image)

        image_instance = ImageModel()

        image_instance.save_image_from_bytes(sticker_image, "sticker_image.jpeg")

        image_url = image_instance.get_image_url()

        response = HttpResponse(sticker_image, content_type="image/jpeg")
        return render(
            request, "image.html", {"image_url": image_url, "image_response": response}
        )

    else:
        return render(request, "index.html")


def upload_success(request):
    return HttpResponse("성공하셨네요")
