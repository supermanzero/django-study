from django.contrib import admin
from djgtest.models import Publisher,Author,Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book,BookAdmin)