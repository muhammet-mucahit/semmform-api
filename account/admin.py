from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from account.models import User
from django.utils.translation import ugettext_lazy as _

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username',)
        }),
        (
            _('Kişisel Bilgiler'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'phone',
                )
            },
        ),
        (
            _('Yetkinlik'),
            {
                'fields': ('is_superuser',)
            },
        ),
    )
    model = User
    list_display = (
        'username',
        'first_name',
        'last_name',
        'phone',
        'date_joined',
        'is_superuser'
    )
    # list_filter = (
    #     'is_staff',
    #     'date_joined',
    #     'gender',
    #     'is_own_writer',
    #     'is_seozeo_writer',
    # )
    # list_editable = ('phone',)
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('-date_joined',)
