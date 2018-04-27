"""Tests for imager_images."""

from django.test import TestCase
from .models import Photo, Album, User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of users."""

    class Meta:
        """User meta model."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class AlbumFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of albums."""

    class Meta:
        """Album meta model."""

        model = Album

    title = factory.Faker('company')
    date_created = factory.Faker('date_time')
    date_modified = factory.Faker('date_time')
    published = 'PUBLIC'


class PhotoFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of photos."""

    class Meta:
        """Photo meta Model."""

        model = Photo

    title = factory.Faker('company')
    date_uploaded = factory.Faker('date_time')
    date_modified = factory.Faker('date_time')
    published = 'PUBLIC'


class AlbumUnitTests(TestCase):
    """Unit tests for the albums."""

    @classmethod
    def setUpClass(cls):
        """Test setup."""
        super(TestCase, cls)
        # fake = Faker()
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            album = AlbumFactory.create(user=user)
            album.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for test."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_album(self):
        """Test the album exists."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.albums)

    def test_user_can_see_its_album_title(self):
        """Test the album."""
        one_user = User.objects.first()
        self.assertEqual(one_user.albums.first().title, one_user.albums.first().title)

    def test_user_can_see_its_album_description(self):
        """Test the album."""
        one_user = User.objects.first()
        self.assertEqual(one_user.albums.first().description, one_user.albums.first().description)


class PhotoUnitTests(TestCase):
    """Unit tests for the photos."""

    @classmethod
    def setUpClass(cls):
        """Test setup."""
        super(TestCase, cls)
        # fake = Faker()
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            album = AlbumFactory.create(user=user)
            album.save()

            photo = PhotoFactory.create(user=user)
            photo.save()

            # photo.albums.add(album)
            album.photos.add(photo)

    @classmethod
    def tearDownClass(cls):
        """Tear down for test."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_photo(self):
        """Test the photo exists."""
        one_album = Album.objects.first()
        self.assertIsNotNone(one_album.photos)

    def test_user_can_see_its_photo_title(self):
        """Test the photo."""
        one_album = Album.objects.first()
        self.assertEqual(one_album.photos.first().title, one_album.photos.first().title)

    def test_user_can_see_its_photo_description(self):
        """Test the photo."""
        one_album = Album.objects.first()
        self.assertEqual(one_album.photos.first().description, one_album.photos.first().description)