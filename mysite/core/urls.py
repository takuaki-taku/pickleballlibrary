from django.urls import path

from .views import *
from .views import ItemListView, CategoryListView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("item/<int:pk>/", ItemView.as_view(), name="item"),  # pkは商品のpk
    path("cart/<int:pk>/", CartView.as_view(), name="cart"),  # pkはユーザーのpk
    path(
        "delete_cart_item/<int:pk>/",
        DeleteCartItemView.as_view(),
        name="delete_cart_item",
    ),  # pkはユーザーのpk
    path("order/", OrderView.as_view(), name="order"),
    path("success/", SuccessView.as_view(), name="success"),
    path("api/items/", ItemListView.as_view(), name="api_items"),
    path("api/items/<int:pk>/", ItemDetailView.as_view(), name="api_item_detail"),
    path("api/categories/", CategoryListView.as_view(), name="api_categories"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "api/cart/<int:pk>/", CartApiView.as_view(), name="api_cart"
    ),  # pkはユーザーのpk
]
