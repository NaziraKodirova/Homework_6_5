from django.contrib import admin
from .models import Address, Student
from import_export.admin import ImportExportModelAdmin


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'get_status_display', 'address')
    list_display_links = ('id', 'first_name', 'last_name')

    def get_status_display(self, obj):
       
        return obj.get_status_display()
