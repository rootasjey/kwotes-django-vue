from django.contrib import admin

from .models import Quote, SimpleAuthor, SimpleReference

# Register your models here.
admin.site.register(Quote)
admin.site.register(SimpleAuthor)
admin.site.register(SimpleReference)
