from django.contrib import admin
from chest.models import Toast, Tag
from chest.forms import ToastForm


@admin.register(Toast)
class ToastAdmin(admin.ModelAdmin):
    list_display    = ['toast', 'disabled', 'explicit', 'numUsed']
    list_filter     = ['tags', 'disabled', 'explicit', 'numUsed']
    search_fields   = ['toast', 'tags']
    ordering        = ['toast']
    readonly_fields = ['numUsed']
    form            = ToastForm
    
    # Used for the form
    def queryset(self, request):
        qs = super(ToastAdmin, self).queryset(request)
        qs = qs.order_by('toast').distinct('toast')
        return qs


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display    = ['tag', 'number_of_toasts', 'created']
    search_fields   = ['tag']
    
    def number_of_toasts(self, obj):
        return obj.toast_set.count()
