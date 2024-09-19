import os
from django.contrib.admin import (
    register,
    ModelAdmin,
    TabularInline,
    action
)
from .models import (
    Application,
    Archive
)
from apps.api.event.models import Event

# Register your models here.
@register(Archive)
class ArchiveAdmin(ModelAdmin):
    list_display = (
        "application",
        "status"
    )

@register(Application)
class ApplicationAdmin(ModelAdmin):
    """
    Представление заявки на участие
    """

    list_display = ("name", "date", "author")
    actions = ["approve_applications", "reject_applications"]

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    change_form_template = os.path.join(project_root, 'templates', 'admin', 'application_change_form.html')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(archive__isnull=True)

    def create_model(self, model, data):
        if model == User:
            data['password'] = make_password(data['password'])

        model.objects.create(
            **data
        )

    @action(description="Подтвердить все")
    def approve_applications(self, request, queryset):
        for application in queryset:
            self.create_model(
                model=Event,
                data={
                    "name": application.name,
                    "description": application.description,
                    "image": application.image,
                    "date": application.date,
                    "author": application.author,
                    "address":  application.address,
                    "landmark": application.landmark
                }
            )

            self.create_model(
                model=Archive,
                data={
                    "application": application,
                    "reason": request.POST.get('reason'),
                    "status": Archive.ApplicationStatus.APPROVED
                }
            )

            application.save()
            messages.success(request, f'{application.name}, {application.author} was approved.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    @action(description="Отклонить все")
    def reject_applications(self, request, queryset):
        for application in queryset:
            self.create_model(
                model=Archive,
                data={
                    "application": application,
                    "reason": request.POST.get('reason'),
                    "status": Archive.ApplicationStatus.REJECTED
                }
            )

            application.save()
            messages.success(request, f'{application.name} {application.author} was rejected.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    def response_change(self, request, obj):
        if '_approve' in request.POST:
            self.create_model(
                model=Event,
                data={
                    "name": obj.name,
                    "description": obj.description,
                    "image": obj.image,
                    "date": obj.date,
                    "author": obj.author,
                    "address":  obj.address,
                    "landmark": obj.landmark
                }
            )

            self.create_model(
                model=Archive,
                data={
                    "application": obj,
                    "status": Archive.ApplicationStatus.APPROVED
                }
            )

            obj.save()
            messages.success(request, f'{obj.name} {obj.author} was approved.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif '_reject' in request.POST:
            self.create_model(
                model=Archive,
                data={
                    "application": obj,
                    "status": Archive.ApplicationStatus.REJECTED
                }
            )

            obj.save()
            messages.success(request, f'{obj.name} {obj.author} was rejected.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            return super().response_change(request, obj)

    def has_add_permission(self, request):
        return False