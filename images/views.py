from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
# Create your views here.
def images(request):
    images = Image.objects.all()
    return render(request, 'images/index.html',{'images':images})

def image(request, pk):
    imageObject = Image.objects.get(id=pk)
    return render(request, 'images/image.html',{'image':imageObject})

def createImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imaginerium')
    else:
        form = ImageForm()
        context = {'form':form}
        return render(request, 'images/create.html', context)

def deleteImage(request, pk):
    image = Image.objects.get(id=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('imaginerium')

    context = {'object':image}
    return render(request, 'images/delete.html',context)

def updateImage(request, pk):
    image = Image.objects.get(id=pk)
    form = ImageForm(instance=image)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('imaginerium')
    else:
        context = {'form':form}
        return render(request, 'images/update.html', context)