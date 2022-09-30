from rest_framework.permissions import IsAuthenticated

SAFE_METHODS = ['GET']


class IsAllowed(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) if request.method in SAFE_METHODS else True
