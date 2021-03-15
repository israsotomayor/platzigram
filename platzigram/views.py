from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('La hora actual del servidor es {now}'.format(now=str(now)))


def sort_integers(request):
    print(request)
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers ordenados satisfactoriamente'
    }
    # import pdb; pdb.set_trace()
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allow hear'.format(name)
    else:
        message = 'Bienvenido {}!, a Platzigram'.format(name)

    return HttpResponse(message)

