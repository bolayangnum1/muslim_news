from django.contrib import admin
from .models import Vacancy, Registration


registerfields = ['phone_number', 'email', 'fio', 'dateofbirth', 'city', 'workexperience', 'levelstudies', 'vacancy']
vacancyfields = ['name', 'company', 'salary', 'adress', 'time_work', 'number', 'education', 'duties', 'conditions']


class VacancyAdmin(admin.ModelAdmin):
    list_display = vacancyfields
    list_filter = vacancyfields
    search_fields = vacancyfields


class RegistrationAdmin(admin.ModelAdmin):
    list_display = registerfields
    list_filter = registerfields
    search_fields = registerfields


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Registration, RegistrationAdmin)
