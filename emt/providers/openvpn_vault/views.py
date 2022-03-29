from rest_framework import generics
from rest_framework.response import Response

from emt.utils.renderers import PlainTextAttachmentMixin, PlainTextRenderer

from .models import OpenVPN
from .serializers import OpenVPNEmployeeIdSerializer, OpenVPNSerializer


class OpenVPNListView(generics.ListCreateAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNSerializer

    def perform_create(self, serializer):
        return OpenVPN.create(**serializer.validated_data)


class OpenVPNDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNSerializer


class OpenVPNGenerateConfigView(PlainTextAttachmentMixin, generics.GenericAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNEmployeeIdSerializer
    renderer_classes = (PlainTextRenderer,)

    def post(self, request, *args, **kwargs):
        openvpn = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.validated_data["employee_id"]
        common_name, config = openvpn.generate_config(employee)
        response = Response(config)
        response.filename = f"{common_name}.ovpn"
        return response
