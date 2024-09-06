from django.contrib import admin
from .models import Employee, Division
from .models import PersonalInfo


admin.site.register(Employee)
admin.site.register(Division)
admin.site.register(PersonalInfo)