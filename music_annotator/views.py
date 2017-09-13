from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    freesound_ids = ['181425', '370934', '191630', '191630', '232014', '219056', '325407']
    return render(request, 'choose_sound.html', {'freesound_ids': freesound_ids})


@csrf_exempt
def annotate(request):
    if request.method == 'POST':
        print(request.POST)

    sound_id = '181425'  # select a hardcoded sound id for now
    # create a fake schema for now
    schema_dict = {'content_types': {'note': ['note', 'instrument']},
                   'proprieties': {'note': ['A', 'B', 'C'],
                                   'instrument': ['drums', 'guitar', 'violin']}}
    json_string = json.dumps(schema_dict)
    return render(request, 'annotate.html', {'schema': json_string, 'sound_id': sound_id})
