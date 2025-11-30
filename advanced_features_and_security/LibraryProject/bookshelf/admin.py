from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year', 'author')
    
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('date_of_birth', 'profile_photo',)

    # Define a new fieldset for the custom fields on the user edit page
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields',{'fields':('date_of_birth', 'profile_photo',)})
    )
    ## Defines the layout for adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('email', 'date_of_birth', 'profile_photo',)})
    )

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUserAdmin, CustomUser)
