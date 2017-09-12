from django.shortcuts import render


def index(request):
    freesound_ids = ['181425', '370934', '191630', '191630', '232014', '219056', '325407']
    return render(request, 'annotate.html', {'freesound_ids': freesound_ids})
