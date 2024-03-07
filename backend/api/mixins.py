from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditiorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]