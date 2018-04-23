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

    bio = factory.Faker('')
    phone = factory.Faker('')
    location = factory.Faker('')
    website = factory.Faker('')
    fee = factory.Faker('')
    camera = factory.Faker('')
    services = factory.Faker('')
    photostyles = factory.Faker('')