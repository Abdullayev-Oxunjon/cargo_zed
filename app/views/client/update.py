from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import Client
from app.serializer.request import ClientModelSerializer


class UpdateClientView(UpdateAPIView):
    """
           API view for update client.

           Attributes:
               serializer_class (class): The serializer class used for serializing/deserializing data.
               queryset (QuerySet): The queryset of client objects used by this view.
       """
    serializer_class = ClientModelSerializer
    queryset = Client.objects.all()
    # Only allow authenticated users to access this view

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ClientModelSerializer,
        responses={
            status.HTTP_200_OK: "Client updated successfully",
            status.HTTP_404_NOT_FOUND: "Client not found",
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

# -----------------------------------------------------------------------------------------------------
