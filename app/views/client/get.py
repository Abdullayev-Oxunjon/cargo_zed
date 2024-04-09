from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from app.models import Client
from app.serializer.request import ClientModelSerializer


class ListClientView(ListAPIView):
    """
        API view for list requests.

        Attributes:
            serializer_class (class): The serializer class used for serializing/deserializing data.
            queryset (QuerySet): The queryset of client objects used by this view.
            """
    serializer_class = ClientModelSerializer
    queryset = Client.objects.all().order_by("-id")

    # Only allow authenticated users to access this view
    permission_classes = [IsAuthenticated]

    # ordering and filtering and search
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ["keyword", "given_time", "fullname", "telegram_id"]
    search_fields = ["keyword", "given_time", "fullname", "telegram_id"]
    ordering_fields = ["given_time", "fullname"]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(

        responses={
            status.HTTP_200_OK: "Clients retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid client data"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# -----------------------------------------------------------------------------------------------------

class GetClientView(RetrieveAPIView):
    """
        API view for get client.

        Attributes:
            serializer_class (class): The serializer class used for serializing/deserializing data.
            queryset (QuerySet): The queryset of client objects used by this view.
    """
    serializer_class = ClientModelSerializer
    queryset = Client.objects.all()
    # Only allow authenticated users to access this view
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Client retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid client data"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# -----------------------------------------------------------------------------------------------------
