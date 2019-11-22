from django.contrib import admin


# Register your models here.

from .models import EmailSubscriber
from django.db.models import Count
from django.db.models.functions import TruncDay

@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_at")
    date_hierarchy = 'created_at' # display these table columns in the list view
    # ordering = ("-created_at",)                  # sort by most recent subscriber
    change_list_template = 'pages/admin/change_list_dataemail.html'

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data =  EmailSubscriber.objects.annotate(date=TruncDay("created_at")).values("date").annotate(nb_email=Count("id")).order_by("-date")

        data = {
            'chart_data': chart_data,
            'nom': 'Gbane'
        }

        extra_context = extra_context or data

        return super().changelist_view(request, extra_context=data)
