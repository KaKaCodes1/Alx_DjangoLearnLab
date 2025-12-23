from rest_framework import permissions
# Even if you have a Token, you can't delete this 
# post unless you are the one who wrote it
class isAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Safe methods (GET, HEAD, OPTIONS) are allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author
        return obj.author == request.user