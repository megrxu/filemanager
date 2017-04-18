from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from os.path import isfile

from file.models import DeletedFile

from file import fileop


# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'GET':
        location_str = request.GET.get('location')
        response = fileop.read_fd(location_str)

    elif request.method == 'POST':
        location_str = request.POST.get('location')
        action = request.POST.get('action')

        # for item in DeletedFile.objects.all():
        #     item.delete()

        if action == 'delete':
            response = fileop.delete_file(location_str)

        elif action == 'edit':
            content_str = request.POST.get('content')
            response = fileop.edit_file(location_str, content_str)
    else:
        response = HttpResponse('No use')

    return response
