from django.test import TestCase
from .models import ImagerProfile, User
import factory

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ImagerProfile

    bio = factory.Faker('street_address')
    phone = factory.Faker('phone_number')
    location = factory.Faker('location')
    website = factory.Faker('website')
    fee = factory.Faker('')
    camera = factory.Faker('')
    services = factory.Faker('')
    photostyles = factory.Faker('')