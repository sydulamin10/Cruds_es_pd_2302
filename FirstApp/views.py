from django.shortcuts import render, redirect
import os
from .models import Profile
from django.db.models import Q

def home(request):

    if request.method == 'GET':
        src = request.GET.get('search')
        if src:
            all_profile = Profile.objects.filter(Q(name__icontains=src) | Q(email__icontains=src))
        else:
            all_profile = Profile.objects.all()
    context = {
        'all_prof': all_profile
    }
    return render(request, 'home.html', context)


def Create(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES.get('image')
        email = request.POST['email']
        address = request.POST['address']
        number = request.POST['number']
        age = request.POST['age']
        gender = request.POST['gender']
        religion = request.POST['religion']
        division = request.POST['division']
        post_code = request.POST['post_code']

        if image:
            prof = Profile(name=name, image=image, email=email, address=address, number=number, age=age, gender=gender,
                           religion=religion, division=division, post_code=post_code)
            prof.save()
            return redirect('home')
        else:
            prof = Profile(name=name, email=email, address=address, number=number, age=age, gender=gender,
                           religion=religion, division=division, post_code=post_code)
            prof.save()
            return redirect('home')

    return render(request, 'create.html')


def delete(request, id):
    delete_prof = Profile.objects.get(id=id)
    if delete_prof:
        if delete_prof.image != 'def.png':
            os.remove(delete_prof.image.path)
        delete_prof.delete()

    return redirect('home')


def update(request, id):
    update_prof = Profile.objects.get(id=id)
    return render(request, 'update.html', locals())