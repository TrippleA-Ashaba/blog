from django.test import TestCase
from django.urls import reverse


# Testing the Home Page
class HomeViewTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


# Testing the Tutorial Page
class TutorialViewTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/tutorials/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("tutorials"))
        self.assertEqual(response.status_code, 200)


# Testing the Tales Page
class TalesViewTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/tales/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("tales"))
        self.assertEqual(response.status_code, 200)


# Testing the About Page
class AboutViewTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
