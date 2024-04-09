from django.urls import path

from app.views.chinese_storage.create import CreateChineseStorageView
from app.views.chinese_storage.detete import DeleteChineseStorageView
from app.views.chinese_storage.get import GetChineseStorageView, ListChineseStorageView
from app.views.login import LoginAPIView
from app.views.parties.create import CreatePartyView
from app.views.parties.delete import DeletePartyView
from app.views.parties.get import ListPartyView, GetPartyView
from app.views.parties.update import UpdatePartyView
from app.views.client.create import CreateClientView
from app.views.client.delete import DeleteClientView
from app.views.client.get import ListClientView, GetClientView
from app.views.client.update import UpdateClientView
from app.views.uzbek_storage.create import CreateUzbekStorageView
from app.views.uzbek_storage.delete import DeleteUzbekStorageView
from app.views.uzbek_storage.get import ListUzbekStorageView, GetUzbekStorageView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),

    # Client URLs

    path("create_client/", CreateClientView.as_view(), name="create_client"),
    path("list_clients/", ListClientView.as_view(), name="list_clients"),
    path("get_client/<int:pk>/", GetClientView.as_view(), name="get_client"),
    path("update_client/<int:pk>/", UpdateClientView.as_view(), name="update_client"),
    path("delete_client/<int:pk>/", DeleteClientView.as_view(), name="delete_client"),

    #  Party URLs

    path("create_party/", CreatePartyView.as_view(), name="create_party"),
    path("list_parties/", ListPartyView.as_view(), name="list_parties"),
    path("get_party/<int:pk>/", GetPartyView.as_view(), name="get_party"),
    path("delete_party/<int:pk>/", DeletePartyView.as_view(), name="delete_party"),
    path("update_party/<int:pk>/", UpdatePartyView.as_view(), name="update_party"),

    # Chinese Storage URLs

    path("create_chinese_storage/", CreateChineseStorageView.as_view(), name="chinese_storage"),
    path("list_chinese_storage/", ListChineseStorageView.as_view(), name="list_chinese_storage"),
    path("get_chinese_storage/<int:pk>/", GetChineseStorageView.as_view(), name="get_chinese_storage"),
    path("delete_chinese_storage/<int:pk>/", DeleteChineseStorageView.as_view(), name="delete_chinese_storage"),

    # Uzbek Storage URLs

    path("create_uzbek_storage/", CreateUzbekStorageView.as_view(), name="uzbek_storage"),
    path("list_uzbek_storage/", ListUzbekStorageView.as_view(), name="list_uzbek_storage"),
    path("get_uzbek_storage/<int:pk>/", GetUzbekStorageView.as_view(), name="get_uzbek_storage"),
    path("delete_uzbek_storage/<int:pk>/", DeleteUzbekStorageView.as_view(), name="delete_uzbek_storage"),
]
