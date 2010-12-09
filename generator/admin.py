from django.contrib import admin
from generator.models import Card, Picture

class CardAdmin(admin.ModelAdmin):
	list_display = ('id', 'hashid', 'sent', 'timestamp', 'spam')
	search_fields = ('toemail', 'message')
	list_filter = ('spam','picture',)

admin.site.register(Card, CardAdmin)
admin.site.register(Picture)