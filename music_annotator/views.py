from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    freesound_ids = ['181425', '370934', '191630', '191630', '232014', '219056', '325407']
    return render(request, 'choose_sound.html', {'freesound_ids': freesound_ids})


@csrf_exempt
def annotate(request, fsid):
    if request.method == 'POST':
        print(request.POST)

    # create a fake schema for now
    schema_dict = {'content_types': {'note': ['note', 'instrument'], 'chord': ['chord', 'instrument']},
                   'proprieties': {'note': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                                   'instrument': ['piano', 'guitar', 'violin'],
                                   'chord': ['A', 'B', 'C']}}
    json_string = json.dumps(schema_dict)
    return render(request, 'annotate.html', {'schema': json_string, 'sound_id': fsid})
