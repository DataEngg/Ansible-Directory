from django.conf.urls import url
from views import Modules
urlpatterns = [
    url(r'^$', Modules.as_view(), name='modules'),
]
