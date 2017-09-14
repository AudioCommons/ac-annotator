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
    schema_dict = {'content_types': {'note': ['note', 'instrument'], 'chord': ['chord', 'instrument'],
                                     'melody': ['instrument', 'mood'], 'chord progression': ['mood'],
                                     'percussive hit': ['percussion'], 'rhythm pattern': ['mood'],
                                     'musical loop': ['mood'], 'texture/drone': ['mood']},
                   'proprieties': {'note': ['C', 'C#/D♭', 'D', 'D#/E♭', 'E', 'F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B'],
                                   'instrument': ['piano', 'guitar', 'violin', 'bass', 'accordion', 'saxophone', 'trumpet'],
                                   'chord': ['C', 'C#/D♭', 'D', 'D#/E♭', 'E', 'F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B'],
                                   'mood': ['happy', 'funny', 'sad', 'tender', 'exciting', 'angry', 'scary'],
                                   'percussion': ['kick', 'snare', 'hi-hat', 'tom', 'crash', 'ride'],
                                   }}

    json_string = json.dumps(schema_dict)
    return render(request, 'annotate.html', {'schema': json_string, 'sound_id': fsid})
