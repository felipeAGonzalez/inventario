from collections import OrderedDict

from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework.status import is_success

from ..common.serializer_examples import (
    SERIALIZER_EXAMPLES,
    BASE64_IMAGE_EXAMPLE,
)


class CustomAutoSchema(SwaggerAutoSchema):
    """
    Custom Swagger Auto Schema.
    """

    def get_tags(self, operation_keys=None):
        """Get the tags from the view.

        Tags are defined in each view as a list of strings in the attribute `swagger_tags`.
        """
        tags = self.overrides.get("tags", None) or getattr(
            self.view, "swagger_tags", []
        )
        if not tags:
            tags = [operation_keys[0]]

        return tags

    def get_response_serializers(self):
        """Get response serializers from the view.

        The default behavior is to set the response serializer to be the same as the request serializer. This functions checks if the view has a response_classes attribute and uses that instead, if it exists.
        """
        manual_responses = self.overrides.get("responses", None) or {}
        if hasattr(self.view, "action"):
            response_dictionary = getattr(self.view, "response_classes", {})
            response_serializer = response_dictionary.get(self.view.action, None)
            if response_serializer:
                if self.view.action == "create":
                    manual_responses = self.overrides.get("responses", None) or {
                        201: response_serializer,
                    }
                else:
                    manual_responses = self.overrides.get("responses", None) or {
                        200: response_serializer,
                    }
        manual_responses = OrderedDict(
            (str(sc), resp) for sc, resp in manual_responses.items()
        )

        responses = OrderedDict()
        if not any(is_success(int(sc)) for sc in manual_responses if sc != "default"):
            responses = self.get_default_responses()

        responses.update((str(sc), resp) for sc, resp in manual_responses.items())
        return responses


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    """
    Custom OpenAPI Schema Generator to add custom examples to the schema.

    The examples are defined in `drftest.common.serializer_examples`.

    For every key of the serializer, if there is a corresponding key in the examples,
    that example will be replaced in the schema.

    If the serializer has a method called get_examples, it will be used instead.

    Note:
        If the key is a reference to another serializer, the example will be ignored.

        This makes it possible to define examples that are used in write serializers
        where there is no reference, while still using the correct reference in read
        serializers. For example, an attribute user may be an id in a write serializer,
        but a reference to UserSerializer in a read serializer.

    """

    def get_schema(self, request=None, public=False):
        """
        Get the schema and replace the examples.

        Note:
            If one of the examples is a property with the title "Base64 Image",
            it will be replaced with `BASE64_IMAGE_EXAMPLE`.

            This makes it possible to define an example for the B64ImageField
            when using read serializers, while still using `BASE64_IMAGE_EXAMPLE`
            in write serializers.

        """
        schema = super().get_schema(request, public)
        for definition in schema.definitions.values():
            examples = SERIALIZER_EXAMPLES
            if hasattr(definition._NP_serializer, "get_examples"):
                examples |= definition._NP_serializer.get_examples()
            for example in examples.keys():
                properties = definition["properties"]
                if example not in properties:
                    continue
                # This means that the key is a reference to another serializer
                # In that case, we don't want to replace the example
                if "$ref" in properties[example]:
                    continue
                if properties[example].get("title", "") == "Base64 Image":
                    properties[example]["example"] = BASE64_IMAGE_EXAMPLE
                elif properties[example].get("title", "") == "Base64 File":
                    properties[example]["example"] = BASE64_IMAGE_EXAMPLE
                else:
                    properties[example]["example"] = examples[example]
        return schema
