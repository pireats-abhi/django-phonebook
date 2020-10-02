from django.contrib import admin
from .models import ContactList

# Register your models here.
class ContactListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'contactName', 'contactEmail', 'contactNumber')

admin.site.register(ContactList, ContactListAdmin)