from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Movie, Review

class MovieAdminForm(ModelForm):
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if self.instance.pk:
            old_obj = Movie.objects.get(pk=self.instance.pk)
            if old_obj.stock == 0 and stock != old_obj.stock:
                raise ValidationError("Cannot change stock when current stock is 0.")
        return stock

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    form = MovieAdminForm

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)