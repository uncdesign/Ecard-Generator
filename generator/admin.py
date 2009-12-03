from django.contrib import admin
from generator.models import Card, Picture, Border, Typeface

class CardAdmin(admin.ModelAdmin):
	list_display = ('id', 'hashid', 'sent', 'timestamp')

admin.site.register(Card, CardAdmin)
admin.site.register(Picture)
admin.site.register(Border)
admin.site.register(Typeface)