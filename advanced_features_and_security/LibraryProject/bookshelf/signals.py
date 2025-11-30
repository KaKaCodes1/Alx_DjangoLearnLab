

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Book # Import the model that holds the permissions

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Ensure this code only runs for the current app
    if sender.name != 'bookshelf':
        return

    # 1. Get the ContentType for the Book model
    try:
        content_type = ContentType.objects.get_for_model(Book)
    except:
        # Prevents crash if ContentType isn't ready during first migration
        return 

    # 2. Retrieve all custom permissions defined in the Book model
    permissions_map = {}
    codenames = ['can_view', 'can_create', 'can_edit', 'can_delete']
    
    for codename in codenames:
        try:
            # Look up the Permission object by its codename and content type
            perm = Permission.objects.get(codename=codename, content_type=content_type)
            permissions_map[codename] = perm
        except Permission.DoesNotExist:
            print(f"Warning: Permission {codename} not found. Did you run makemigrations?")
            return

    # 3. Create Groups and Assign Permissions
    
    # Viewers Group
    viewers, created = Group.objects.get_or_create(name='Viewers')
    if created:
        viewers.permissions.add(permissions_map['can_view'])

    # Editors Group
    editors, created = Group.objects.get_or_create(name='Editors')
    if created:
        editors.permissions.add(
            permissions_map['can_view'],
            permissions_map['can_create'],
            permissions_map['can_edit'],
        )

    # Admins Group
    admins, created = Group.objects.get_or_create(name='Admins')
    if created:
        admins.permissions.add(
            permissions_map['can_view'],
            permissions_map['can_create'],
            permissions_map['can_edit'],
            permissions_map['can_delete'],
        )
    
    if created:
        print(" Default permission groups (Admins, Editors, Viewers) created.")