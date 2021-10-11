from django.contrib import admin
from .models import NewEntry,Socials

# Register your models here.
@admin.register(NewEntry)
class NewEntryAdmin(admin.ModelAdmin):
	list_display = ['username','Topic','TodaysEntry']

@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
	list_display = ['username','linkedin','twitter','facebook','instagram','bio']






