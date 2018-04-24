from django.test import TestCase
from .models import ImagerProfile, User
from faker import Faker
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
    bio = factory.Faker('company')
    phone = factory.Faker('phone_number')

    location = factory.Faker('country')
    website = factory.Faker('email')
    fee = factory.Faker('random_number')
    camera = 'DSLR'
    services = 'weddings'
    photostyles = 'macro'



class ProfileUnitTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        # fake = Faker()
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            profile = ProfileFactory.create(user=user)
            profile.save()

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)