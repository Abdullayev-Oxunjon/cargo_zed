from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import Client
from app.serializer.request import ClientModelSerializer


class CreateClientView(CreateAPIView):
    """
        API view for creating  client.

        Attributes:
            serializer_class (class): The serializer class used for serializing/deserializing data.
            queryset (QuerySet): The queryset of client objects used by this view.
        """

    serializer_class = ClientModelSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ClientModelSerializer,
        responses={
            status.HTTP_201_CREATED: "Client created successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid client data"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# -----------------------------------------------------------------------------------------------------
