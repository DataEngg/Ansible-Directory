import json


def get_post_params(request):
    data = request.POST
    if not data:
        try:
            data = json.loads(request.body)
        except:
            data = {}
    return data
