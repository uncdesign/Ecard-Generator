from django.contrib import admin
from generator.models import Card, Picture, Bow, Typeface

class CardAdmin(admin.ModelAdmin):
	list_display = ('id', 'hashid', 'timestamp')

admin.site.register(Card, CardAdmin)
admin.site.register(Picture)
admin.site.register(Bow)
admin.site.register(Typeface)