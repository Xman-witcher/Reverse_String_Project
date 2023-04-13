from django.contrib import admin
from django.urls import path
from reverse_string_app.views import reverse_string, reverse_string_json
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reverse_string, name=''),
    path('json/', reverse_string_json, name='json'),
    path('json', reverse_string_json, name='json')
]

