from django.contrib import admin
from .models import Movie, Actor

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'updated_at')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
