"""Tests for profile."""

from django.test import TestCase
from .models import ImagerProfile, User
from imager_images.models import Photo, Album
from django.urls import reverse_lazy
# from faker import Faker
import factory

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of users."""

    class Meta:
        """User meta model."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of Imager Profiles."""

    class Meta:
        """Profile meta model."""

        model = ImagerProfile
    bio = factory.Faker('company')
    phone = factory.Faker('phone_number')
    location = factory.Faker('country')
    website = factory.Faker('email')
    fee = factory.Faker('random_number')
    camera = 'DSLR'
    services = 'weddings'
    photostyles = 'macro'


def profile_thing(profile):
    """Create a bunch of Imager Profiles."""
    profile.bio = factory.Faker('company')
    profile.location = factory.Faker('country')
    profile.website = factory.Faker('email')
    profile.camera = 'DSLR'
    profile.services = 'weddings'
    profile.photostyles = 'macro'
    profile.save()
    return profile


class PhotoFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of photos."""

    class Meta:
        """Photo meta Model."""

        model = Photo

    title = factory.Faker('company')
    date_uploaded = factory.Faker('date_time')
    date_modified = factory.Faker('date_time')
    published = 'PUBLIC'


class AlbumFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of albums."""

    class Meta:
        """Album meta model."""

        model = Album

    title = factory.Faker('company')
    date_created = factory.Faker('date_time')
    date_modified = factory.Faker('date_time')
    published = 'PUBLIC'


class ProfileUnitTests(TestCase):
    """Unit tests for the profiles."""

    @classmethod
    def setUpClass(cls):
        """Test setup."""
        super(TestCase, cls)
        # fake = Faker()
        for _ in range(10):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            profile_thing(user.profile)
            user.save()

            # profile = ProfileFactory.create(user=user)
            # profile.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for test."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        """Test the profile exists."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)

    def test_profile_has_camera(self):
        """Test the profile has a camera."""
        one_user = User.objects.first()
        self.assertEqual(one_user.profile.camera, 'DSLR')

    def test_profile_has_services(self):
        """Test the profile has a services."""
        one_user = User.objects.first()
        self.assertEqual(one_user.profile.services[0], 'weddings')


class ProfileViewTests(TestCase):
    """Unit tests for the profile view."""

    @classmethod
    def setUp(self):
        """Test setup."""
        super(TestCase, self)
        # fake = Faker()
        for _ in range(5):
            self.user = UserFactory.create()
            self.user.set_password(factory.Faker('password'))
            self.user.save()

            self.album = AlbumFactory.create(user=self.user)
            self.album.save()

            self.photo = PhotoFactory.create(user=self.user)
            self.photo.save()

            # photo.albums.add(album)
            self.album.photos.add(self.photo)

    @classmethod
    def tearDown(self):
        """Tear down for test."""
        super(TestCase, self)
        User.objects.all().delete()
        Photo.objects.all().delete()

    def test_profile_view_profile(self):
        """Test profile view profile."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('profile'))
        self.assertEqual(response.context['profile'].user.username, self.user.username)

    def test_profile_view_photos(self):
        """Test profile view photos."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('profile'))
        self.assertEqual(len(response.context['photos']), 5)

    def test_profile_view_num_photos(self):
        """Test profile view num_photos."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('profile'))
        self.assertEqual(response.context['num_photos'], 5)
