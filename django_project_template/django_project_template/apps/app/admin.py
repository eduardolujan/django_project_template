from django.contrib import admin
from django_project_template.apps.app.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
