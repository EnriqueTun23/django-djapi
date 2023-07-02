from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import ProductoList, ProductoDetalle, CategoriaList, \
    SubCategoriaList, CategoriaDetail, SubCategoriaAdd, ProductosViewSet, \
    UserCreate, LoginView

router = DefaultRouter()

router.register('v2/productos', ProductosViewSet, basename='productosV2')

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='productos_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/categorias/', CategoriaList.as_view(), name='categorias'),
    # path('v1/subcategorias/', SubCategoriaList.as_view(), name='subcategorias'),
    path('v1/categorias/<int:pk>', CategoriaDetail.as_view(), name='Categoria_detalle'),
    path('v1/categorias/<int:pk>/subcategoria/', SubCategoriaList.as_view(), name='Categoria_list'),
    path('v1/categorias/<int:pk>/subcategoria/', SubCategoriaList.as_view(), name='Categoria_list'),
    path('v1/categorias/<int:cat_pk>/addsubcategoria/', SubCategoriaAdd.as_view(), name='add_subcategoria_list'),
    path('v1/usuarios/', UserCreate.as_view(), name="create_user"),

    path("v1/login/", LoginView.as_view(), name="login"),
    path("v1/login-drf/", views.obtain_auth_token, name="login-drf"),
]

urlpatterns += router.urls