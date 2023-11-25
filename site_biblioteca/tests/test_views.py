from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class StatusViewsTestCase(TestCase):
    def setUp(self):
        if not User.objects.filter(username='lucas@gmail.com').exists():
            user = User.objects.create_superuser(
                username='lucas@gmail.com',
                password='meina1246'
        )
            user.save()

    def test_status_login_register_auth_inicio_200(self):
        response = self.client.get(reverse('login_auth'))
        self.assertEquals(response.status_code, 200)

        response2 = self.client.get(reverse('register_auth'))
        self.assertEquals(response2.status_code, 200)

        response3 = self.client.get(reverse('inicio'))
        self.assertEquals(response3.status_code, 200)


    def test_status_home_historico_302_quando_usuario_nao_esta_logado(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 302)

        response2 = self.client.get(reverse('historico'))
        self.assertEquals(response2.status_code, 302)


    def test_status_home_historico_200_quando_usuario_esta_logado(self):
        self.client.login(username='lucas@gmail.com', password='meina1246')

        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

        response2 = self.client.get(reverse('historico'))
        self.assertEquals(response2.status_code, 200)
    