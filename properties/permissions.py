from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        # SAFE METHODS
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # OWNER CHECK
        return obj.owner == request.user