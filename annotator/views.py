from django.shortcuts import render
from django.http import JsonResponse


def get_hierachy_paths(request):
    hierachy_paths = [
        ["/m/0dgw9r", "/m/09l8g", "/m/09x0r", "/m/05zppz"],
        ["/t/dd00123", "/m/07bm98", "/m/01b7fy"],
        ["/t/dd00098", "/m/028v0c"],
        ["/m/0dgw9r", "/m/09l8g", "/m/09x0r", "/m/02qldy"],
        ["/m/059j3w", "/m/03m9d0z", "/m/09t49"],
    ]

    id_to_name = {
        '/m/01b7fy': 'Headphones',
        '/m/028v0c': 'Silence',
        '/m/02qldy': 'Narration, monologue',
        '/m/03m9d0z': 'Wind',
        '/m/059j3w': 'Natural sounds',
        '/m/05zppz': 'Male speech, man speaking',
        '/m/07bm98': 'Sound reproduction',
        '/m/09l8g': 'Human voice',
        '/m/09t49': 'Rustling leaves',
        '/m/09x0r': 'Speech',
        '/m/0dgw9r': 'Human sounds',
        '/t/dd00098': 'Source-ambiguous sounds',
        '/t/dd00123': 'Channel, environment and background'
    }

    return JsonResponse({'hierachy_paths': hierachy_paths,
                         'id_to_name': id_to_name,
                         }, safe=False)


def taxonomy_table(request):
    nodes_data = [
        {
            'id': '/m/01b7fy',
            'name': 'Headphones'
         },
        {
            'id': '/m/028v0c',
            'name': 'Silence'
         },
        {
            'id': '/m/02qldy',
            'name': 'Narration, monologue'
         },
        {
            'id': '/m/03m9d0z',
            'name': 'Wind'
         },
        {
            'id': '/m/059j3w',
            'name': 'Natural sounds'
         },
        {
            'id': '/m/05zppz',
            'name': 'Male speech, man speaking'
         },
        {
            'id': '/m/07bm98',
            'name': 'Sound reproduction'
         },
        {
            'id': '/m/09l8g',
            'name': 'Human voice'
         },
        {
            'id': '/m/09t49',
            'name': 'Rustling leaves'
         },
        {
            'id': '/m/09x0r',
            'name': 'Speech'
         },
        {
            'id': '/m/0dgw9r',
            'name': 'Human sounds'
         },
        {
            'id': '/t/dd00098',
            'name': 'Source-ambiguous sounds'
         },
        {
            'id': '/t/dd00123',
            'name': 'Channel, environment and background'
         },
    ]
    return render(request, 'taxonomy_table.html',
                  {'nodes_data': nodes_data})


def generate_annotations(request):
    freesound_id = 36
    return render(request, 'generate_annotations.html',
                  {'freesound_sound_id': freesound_id})
