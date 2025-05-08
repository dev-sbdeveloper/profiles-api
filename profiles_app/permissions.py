from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnFeed(permissions.BasePermission):
    """Allow users to update their own feed status"""

    def has_object_permission(self, request, view, obj):
        """Check that user is trying to update their own feed status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile_author.id == request.user.id
