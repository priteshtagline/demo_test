
from user_roles.admin_permission.admin import \
    AdminAuthenticationPermission
from django.contrib.auth.models import Permission, User
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PermissionViewSet(APIView):
    """User permissions get and update by superuser.  
    """
    permissions = [IsAuthenticated, AdminAuthenticationPermission]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get_user_permissions(self, user):
        all_permissions = User(is_superuser=True).get_all_permissions()
        user_permissions = {p: p in user.get_all_permissions()
                            for p in all_permissions}
        permissions_dict = {}
        for key, value in user_permissions.items():
            app, action_model = key.split(".")
            action, model = action_model.split("_")

            permissions_dict.setdefault(app, {}).setdefault(model, {})[
                action] = value
        return permissions_dict

    def get(self, request, pk, format=None):
        if not request.user.has_perm('auth.view_permission'):
            raise PermissionDenied()
        user = self.get_object(pk)
        return Response(self.get_user_permissions(user))

    def put(self, request, pk, format=None):
        if not request.user.has_perm('auth.change_permission') or not request.user.has_perm('auth.add_permission'):
            raise PermissionDenied()
        user = self.get_object(pk)
        permissions = request.data.get('permissions', False)
        for app in permissions:
            for model in permissions[app]:
                for action in permissions[app][model]:
                    codename = '{0}_{1}'.format(action, model)
                    permission_chnage = Permission.objects.get(
                        codename=codename, content_type__model=model, content_type__app_label=app)
                    if permissions[app][model][action]:
                        user.user_permissions.add(permission_chnage)
                    else:
                        user.user_permissions.remove(permission_chnage)

        return Response(self.get_user_permissions(user))
