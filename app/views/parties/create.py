from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import Party
from app.serializer.parties import PartyModelSerializer


class CreatePartyView(CreateAPIView):
    """
    API view for creating a party.

    Attributes:
        serializer_class (class): The serializer class used for serializing/deserializing data.
        queryset (QuerySet): The queryset of client objects used by this view.
    """

    serializer_class = PartyModelSerializer
    queryset = Party.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=PartyModelSerializer,  # Use your serializer class
        responses={
            status.HTTP_201_CREATED: "Party created successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid party data"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
