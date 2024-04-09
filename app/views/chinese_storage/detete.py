from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import ChineseStorage
from app.serializer.chinese_storage import ChineseStorageModelSerializer


class DeleteChineseStorageView(DestroyAPIView):
    """
           API view for delete chinese_storage.

           Attributes:
               serializer_class (class): The serializer class used for serializing/deserializing data.
               queryset (QuerySet): The queryset of client objects used by this view.
       """
    serializer_class = ChineseStorageModelSerializer
    queryset = ChineseStorage.objects.all()
    # Only allow authenticated users to access this view

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "ChineseStorage deleted successfully",
            status.HTTP_404_NOT_FOUND: "Not found ChineseStorage",
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
