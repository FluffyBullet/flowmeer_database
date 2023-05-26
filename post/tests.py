from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class SeeAllPostTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username="david", password="reynolds")
        self.user = User.objects.create_user(username="jason", password="megaroll")
        self.client.force_authenticate(self.user)


    def test_can_see_all_post(self):
        jason = User.objects.get(username="jason")
        image_path = './assets/images/default.png'
        Post.objects.create(owner=jason, title="flower A", image=image_path)
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_post(self):
        self.client.login(username='jason', password='megaroll')
        
        image_path = './assets/images/default.png'
        
        with open(image_path, 'rb') as image_file:
            response = self.client.post('/post/', {'title': 'flower A','image': image_file, 'flower_tag' : 'rose'}, format='multipart')

        post = Post.objects.all()
        print(post)
        count = Post.objects.count()
        print(response.json())
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)