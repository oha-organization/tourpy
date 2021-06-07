from django.contrib import admin
from .models import Page,Slide,Option, TourCategory, TourPhotos,Tour, TourPrices,CategoryTour

class PageAdmin(admin.ModelAdmin):
    left_display= ('title','page_type',)
    prepopulated_fields = {'slug': ('title',)} # while you were typing title, slug is being typed automatic
# Register your models here.
admin.site.register(Page,PageAdmin)
admin.site.register(Slide)
admin.site.register(Option)
admin.site.register(TourCategory)

class PriceInline(admin.TabularInline):
    model = TourPrices
    extra = 3

class PhotoInline(admin.TabularInline):
    model = TourPhotos
    extra = 5

class TourAdmin(admin.ModelAdmin):
    inlines = [PriceInline,PhotoInline]

admin.site.register(Tour,TourAdmin)
admin.site.register(TourPhotos)

class TourPricesAdmin(admin.ModelAdmin):
    list_display = ('begin_date', 'end_date', 'title','price_dollar_for_single')

admin.site.register(TourPrices,TourPricesAdmin)
admin.site.register(CategoryTour)