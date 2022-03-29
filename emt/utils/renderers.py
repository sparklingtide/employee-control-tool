from rest_framework import renderers
from rest_framework.response import Response


class PlainTextAttachmentMixin:
    filename = "export"

    def get_filename(self, request=None, response=None, *args, **kwargs):
        return getattr(response, "filename", self.filename)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        if (
            isinstance(response, Response)
            and response.accepted_renderer.format == "txt"
        ):
            response["Content-Disposition"] = "attachment; filename={}".format(
                self.get_filename(request=request, response=response, *args, **kwargs)
            )
        return response


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = "text/plain"
    format = "txt"

    def render(self, data, media_type=None, renderer_context=None):
        return data
