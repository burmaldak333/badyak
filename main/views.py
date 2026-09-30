import os
import random
from django.shortcuts import render, redirect
from django.conf import settings


def gender_view(request):
    if request.method == 'POST':
        request.session.pop('name', None)
        request.session['gender'] = request.POST.get('gender')
        return redirect('name')
    return render(request, 'gender.html')


def name_view(request):
    gender = request.session.get('gender')
    if not gender:
        return redirect('gender')

    if request.method == 'POST':
        request.session['name'] = request.POST.get('name', '').strip()
        return redirect('result')

    return render(request, 'name.html')


def result_view(request):
    gender = request.session.get('gender')
    name = request.session.get('name')

    if not gender or not name:
        return redirect('gender')

    # Проверка первых 3 букв (регистр не важен)
    first_three = name[:3].lower()
    special_names = ('бад', 'бод')

    if first_three in special_names:
        image = 'images/special.jpg'
    else:
        folder = os.path.join(settings.BASE_DIR, 'static', 'images', gender)
        images = os.listdir(folder) if os.path.isdir(folder) else []
        image = f"images/{gender}/{random.choice(images)}" if images else None

    return render(request, 'result.html', {
        'name': name,
        'gender': gender,
        'image': image,
    })


def reset_view(request):
    request.session.flush()
    return redirect('gender')