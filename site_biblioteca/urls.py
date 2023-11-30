from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init, name="inicio"),
    path('register_auth/', views.register_auth, name='register_auth'),
    path('login/', views.login_auth, name='login_auth'),
    path('esquecisenha/', views.esqueci_senha, name='esqueci_senha'),
    path('codigoverify/', views.codigo_verify, name='codigo_verify'),
    path('trocarsenha/', views.trocar_senha, name='trocar_senha'),
    path('home/', views.home, name="home"),
    path('register/', views.registerbook, name="register"),
    path('livro/<int:book_id>/', views.livroview, name='livroview'),
    path('delete_book/<int:book_id>/', views.deletebook, name='deletebook'),
    path('update_book/<int:book_id>/', views.updatebook, name='updatebook'),
    path('registerBorrowing/', views.registerBorrowing, name='registerBorrowing'),
    path('historico/', views.historico, name='historico'),
    path('download_comprovante/<int:emprestimo_id>/', views.download_comprovante, name='download_comprovante'),
    path('download_acervo', views.download_acervo, name='download_acervo'),
    path('download_categorias', views.download_categorias, name='download_categorias'),
    path('logout/', views.logoutp, name='logout')
] 