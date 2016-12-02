from django.contrib import admin

# Register your models here.
from .models import TimeStamp


class FilterUserAdmin(admin.ModelAdmin): 
    def save_model(self, request, obj, form, change):
    	if getattr(obj, 'user', None) is None:    		#Assign user only the first time #if obj.user == None:
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
    list_display = ('time_stamp','user')
    list_filter = ['user']
    def has_add_permission(self, request):
        return False
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('time_stamp', 'user')
        return self.readonly_fields
    def has_delete_permission(self, request, obj=None):
        #Disable delete
        return False


admin.site.register(TimeStamp,TimeStampAdmin)