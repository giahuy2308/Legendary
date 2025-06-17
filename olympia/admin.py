from django.contrib import admin
from django.apps import apps
# Register your models here.

models = apps.get_app_config('olympia').get_models()

admin.site.register(models)