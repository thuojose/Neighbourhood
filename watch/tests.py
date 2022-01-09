from django.test import TestCase
from .models import Neighbourhood
from django.contrib.auth.models import User

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.ngong = Neighbourhood(neighbourhood_name = 'ngong')

    def test_instance(self):
        self.assertTrue(isinstance(self.ngong, Neighbourhood))

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.ngong.create_neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_method(self):
        self.ngong.delete_neighbourhood('ngong')
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)

    def test_find_neighbourhood(self):
        self.ngong.create_neighbourhood()
        fetched_hood = Neighbourhood.find_neighbourhood("ngong")
        self.assertNotEqual(fetched_hood, self.kasarani)

    def test_update_method(self):
        self.ngong.create_neighbourhood()
        edited_hood = Neighbourhood.update_neighbourhood("karen")
        self.assertEqual(self.ngong, edited_hood)

class healthservicesTestClass(TestCase):
    def setUp(self):
        self.optical = healthservices(healthservices = 'optical')

    def test_instance(self):
        self.assertTrue(isinstance(self.optical, healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.optical.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health) > 0)

    def test_delete_method(self):
        self.optical.delete_healthservices('optical')
        health = healthservices.objects.all()
        self.assertTrue(len(health) == 0)