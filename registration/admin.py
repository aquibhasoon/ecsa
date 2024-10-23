from django.contrib import admin
from .models import Application

# Register your models here.

@admin.register(Application)
class RegistrationAdmin(admin.ModelAdmin):
	list_display = ['student', 'student_id', 'accepted', 'created_at', 'year_of_graduation']
	list_filter = ['accepted', 'created_at', 'year_of_graduation']
	search_fields = ['student__username', 'student_id']
	list_editable = ['accepted']
	list_per_page = 10