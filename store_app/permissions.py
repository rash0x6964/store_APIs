from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)



# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjU1MDY4LCJpYXQiOjE3Mjg4MjMwNjgsImp0aSI6IjM5ZjFkMzFkZThiODRiMzFiOTk1NzUwMTVmMzlmMDZlIiwidXNlcl9pZCI6Mn0.IGHbrBSnSGjoFEHnmtP_pZUVECWZ4gIKPJq8R8urecU
