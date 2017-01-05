
import os

from rest_framework import status
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from utils import get_post_params
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class Modules(View):

    def post(self, request, *args, **kwargs):
        response = dict(status=status.HTTP_400_BAD_REQUEST)
        list_directory = ['group_vars', 'roles']
        list_files = ['__init__.py', 'ansible.cfg', 'hosts', 'server.yml']
        list_roles = ['files', 'handlers', 'meta', 'tasks', 'templates']
        try:
            data = get_post_params(request)
            path = data['path']
            name = data['name']
            path = os.path.join(path, 'ansible_' + str(name))
            if not os.path.exists(path):
                os.makedirs(path)
            for i in list_directory:
                path_dir = os.path.join(path, i)
                if not os.path.exists(path_dir):
                    if i != 'roles':
                        os.makedirs(path_dir)
                    else:
                        os.makedirs(path_dir)
                        path_name = os.path.join(path_dir, name)
                        os.makedirs(path_name)
                        for j in list_roles:
                            path_value = os.path.join(path_name, j)
                            if j == 'templates':
                                os.makedirs(path_value)
                            else:
                                os.makedirs(path_value)
                                f = open(path_value + '/main.yml', 'w +')
                                f.close()
            for i in list_files:
                f = open(path + '/' + i, 'w+')
                f.close()
            response['message'] = "Created a dircetory"
            return JsonResponse(response,
                                status=status.HTTP_200_OK)
        except Exception as e:
            response['error'] = str(e)
            return JsonResponse(response,
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
