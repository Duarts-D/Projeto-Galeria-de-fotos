from django.urls import path
from .views import index,imagem,buscar,nova_imagem,editar_imagem,deletar_imagem,filtro

urlpatterns = [
    path('',index, name='index'),
    path('imagem/<int:foto_id>',imagem,name='imagem'),
    path('buscar', buscar, name='buscar'),  
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar-imagem'),  
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar-imagem'),
    path('/<str:categoria>', filtro, name='filtro'),  

]

