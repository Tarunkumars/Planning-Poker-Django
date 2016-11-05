from django.contrib import admin

# Register your models here.
from .models import Game, Ustory

admin.site.register(Game)
admin.site.register(Ustory)
