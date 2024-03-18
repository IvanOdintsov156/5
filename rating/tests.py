from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comic, Rating

class RatingSystemTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.comic = Comic.objects.create(title='Test Comic', author='Test Author')

    def test_create_rating_and_update_comic_rating(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/api/ratings/', {'comic': self.comic.id, 'user': self.user.id, 'value': 5})
        self.comic.refresh_from_db()
        self.assertEqual(self.comic.rating, 5)  # Assuming this is the first and only rating

    def test_get_comic_average_rating(self):
        Rating.objects.create(comic=self.comic, user=self.user, value=5)
        response = self.client.get(f'/api/comics/{self.comic.id}/rating/')
        self.assertEqual(response.json()['rating'], 5)  # Assuming this is the first and only rating