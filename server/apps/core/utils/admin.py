from django.forms import Textarea
from easy_select2 import select2_modelform
from import_export.admin import ExportActionMixin
from import_export.resources import ModelDeclarativeMetaclass, ModelResource


class SuperUserAdminMixin:
    """
    Добавляет поля, которые не доступны пользователю
    если он не являются суперпользователем
    """

    list_readonly_not_superuser_fields = ()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            for field in self.list_readonly_not_superuser_fields:
                if field in form.base_fields:
                    form.base_fields[field].disabled = True

        return form


class TextareaAdminMixin:
    list_textarea_fields = ()

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in self.list_textarea_fields:
            kwargs["widget"] = Textarea()
            return db_field.formfield(**kwargs)
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class Select2AdminMixin:
    use_select2_form = True

    def get_form(self, request, obj=None, **kwargs):
        if self.use_select2_form:
            kwargs["form"] = select2_modelform(self.model)
        return super().get_form(request, obj, **kwargs)


class ExportMixin(ExportActionMixin):
    list_export_fields = ()

    def modelresource_factory(self, model, resource_class=ModelResource):
        """
        Factory for creating ``ModelResource`` class for given Django model.
        """
        attrs = {"model": model}

        if self.list_export_fields:
            attrs = {"fields": self.list_export_fields, **attrs}

        Meta = type(str("Meta"), (object,), attrs)

        class_name = model.__name__ + str("Resource")

        class_attrs = {
            "Meta": Meta,
        }

        metaclass = ModelDeclarativeMetaclass
        return metaclass(class_name, (resource_class,), class_attrs)

    def get_resource_class(self):
        if not self.resource_class:
            return self.modelresource_factory(self.model)
        return self.resource_class


class BaseAdminMixin(
    ExportMixin,
    TextareaAdminMixin,
    SuperUserAdminMixin,
    Select2AdminMixin,
):
    pass
