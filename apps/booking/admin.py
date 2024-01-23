from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.booking.models import Booking, Service, City, State


class CityInline(admin.StackedInline):
    model = City
    extra = 5


class StateAdmin(admin.ModelAdmin):
    inlines = [CityInline]


class BookingResource(resources.ModelResource):

    def get_export_headers(self):
        headers = super().get_export_headers()
        print(headers)
        new_headers = ['id', 'First Name', 'Last Name', 'Mobile Number', 'Service', 'Booking Date', 'State', 'City',
                       'Message']
        return new_headers

    class Meta:
        model = Booking
        fields = ('id', 'first_name', 'last_name', 'mobile_number', 'service__service', 'booking_date', 'state__state',
                  'city__city', 'message')
        export_order = ('id', 'first_name', 'last_name', 'mobile_number', 'service__service', 'booking_date',
                        'state__state', 'city__city', 'message')
        import_id_fields = ['id']


class BookingAdmin(ImportExportModelAdmin):
    resource_class = BookingResource
    list_display = ('first_name', 'last_name', 'service', 'booking_date')


admin.site.register(Booking, BookingAdmin)
admin.site.register(Service)
admin.site.register(State, StateAdmin)
