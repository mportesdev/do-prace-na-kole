import sys
from operator import itemgetter

from django.db import connections
from django.core.exceptions import ImproperlyConfigured

from import_export import fields
from import_export.resources import ModelResource

from .models import TShirtSize


def dehydrate_decorator(value_field, t_shirt_code_name):
    """Dehydrate field decorator

    :param str value_field: TShirtSize value field name
    :param str t_shirt_code_name: dehydrate function field name

    :return function wrap: dehydrate field wrap function
    """

    def wrap(self, delivery_batch):
        """Dehydrate field wrap

        :param model class instance delivery_batch: DeliveryBatch model
                                                    class instance
        """
        t_shirts = delivery_batch.t_shirt_size_counts(
            value_field=value_field,
        )
        for t_shirt in t_shirts:
            if t_shirt[0] == t_shirt_code_name:
                return t_shirt[1]

    return wrap


def get_all_t_shirt_codes(value_field):
    """Get all t-shirts codes

    :param str value_field: TShirtSize value field name

    :return set codes: unique t-shirts codes
    """
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        return ("TEST",)
    # During build Docker image DB isn't accessible
    try:
        codes = {}
        # Check if "TShirtSize" model DB table exist, during tests
        if (
            TShirtSize._meta.db_table
            in connections["default"].introspection.table_names()
        ):
            codes = set(
                TShirtSize.objects.all().values_list(value_field, flat=True),
            )
            codes.difference_update(["", "nic"])
    except ImproperlyConfigured:
        pass
    return codes


def get_model_resource_class_body():
    """Get model resource class body"""
    body = {}
    all_fields = []
    tshirt_code_field = "code"
    for idx, t_shirt_code in enumerate(
        get_all_t_shirt_codes(tshirt_code_field),
    ):
        field_name = f"tshirt_code_{idx}"
        body[field_name] = fields.Field(column_name=t_shirt_code)
        dehydrate_func = dehydrate_decorator(
            value_field=tshirt_code_field,
            t_shirt_code_name=t_shirt_code,
        )
        body["dehydrate_{}".format(field_name)] = dehydrate_func
        all_fields.append((field_name, t_shirt_code))
    body["fields"] = sorted(all_fields, key=itemgetter(1))
    return body


DeliveryBatchModelBaseResource = type(
    "DeliveryBatchModelBaseResource",
    (ModelResource,),
    get_model_resource_class_body(),
)
