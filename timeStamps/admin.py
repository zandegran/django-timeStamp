"""
This module is to define how TimeStamp model is represented in the Admin site
It also registers the model to be shown in the admin site 

.. seealso:: :class:`..models.TimeStamp`

"""

from django.contrib import admin


from .models import TimeStamp


class FilterUserAdmin(admin.ModelAdmin): 
    """
    Makes the timestamps of one user not visible to others unless for a superuser

    """
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:          #Assign user only the first time #if obj.user == None:
            obj.user = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(FilterUserAdmin, self).get_queryset(request)
        #qs = admin.ModelAdmin.queryset(self, request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    def has_change_permission(self, request, obj=None):
        if not obj:
            # the changelist itself
            return True # So they can see the change list page
        return obj.user == request.user or request.user.is_superuser

class TimeStampAdmin(FilterUserAdmin):
    """
    This is configuration of TimeStamp model is admin page
    This inherits class FilterUserAdmin
    .. seealso:: :class:`FilterUserAdmin`

    """
    list_display = ('time_stamp','user') # Fields to show in the listing
    list_filter = ['user']               # Enables to se timeStamps of any single user
    def has_add_permission(self, request):
        """
        Disables addition of timeStamps from the admin page

        """
        return False
    def get_readonly_fields(self, request, obj=None):
        """
        Disables editing in admin page

        """
        if obj: # editing an existing object
            return self.readonly_fields + ('time_stamp', 'user')
        return self.readonly_fields
    def has_delete_permission(self, request, obj=None):
        """
        Disable deletion of rcords in admin page

        """
        return False

admin.site.register(TimeStamp,TimeStampAdmin)   # Registers the TimeStamp Model with TimeStampAdmin setting in the Admin site