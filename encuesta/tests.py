from django.test import TestCase
from .models import Hotel

class HotelTestCase(TestCase):
    def setUp(self):
        # Configura los datos iniciales para las pruebas
        Hotel.objects.create(name="Hotel Test", location="Test City")

    def test_hotel_creation(self):
        # Verifica que el hotel se haya creado correctamente
        hotel = Hotel.objects.get(name="Hotel Test")
        self.assertEqual(hotel.location, "Test City")

    def test_hotel_str(self):
        # Verifica el método __str__ del modelo
        hotel = Hotel.objects.get(name="Hotel Test")
        self.assertEqual(str(hotel), "Hotel Test")
