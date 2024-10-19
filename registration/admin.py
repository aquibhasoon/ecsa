from django.contrib import admin
from .models import Application

# Register your models here.

@admin.register(Application)
class RegistrationAdmin(admin.ModelAdmin):
	list_display = ['student', 'id_no', 'accepted', 'created_at', 'year_of_graduation']
	list_filter = ['accepted', 'created_at', 'year_of_graduation']
	search_fields = ['student__username', 'id_no']
	list_editable = ['accepted']
	list_per_page = 10