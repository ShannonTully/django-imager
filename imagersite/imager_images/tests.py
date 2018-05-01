"""Tests for imager_images."""

from django.test import TestCase
from .models import Photo, Album, User
from django.urls import reverse_lazy
import factory
import tempfile


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
    image = tempfile.NamedTemporaryFile(suffix=".jpg").name
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


class ImageViewTests(TestCase):
    """Unit tests for the image views."""

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

    def test_image_view_library_profile(self):
        """Test image view library profile."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('library'))
        self.assertEqual(response.context['profile'].username, self.user.username)

    def test_image_view_library_photos(self):
        """Test image view library photos."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('library'))
        self.assertEqual(len(response.context['photos']), 1)

    def test_image_view_library_albums(self):
        """Test image view library albums."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('library'))
        self.assertEqual(len(response.context['albums']), 1)

    def test_image_view_public_albums(self):
        """Test image view public_albums."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('album'))
        self.assertEqual(len(response.context['public_albums']), 5)

    def test_image_view_public_albums_photo(self):
        """Test image view photo on a public album."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('album'))
        self.assertIsNotNone(response.context['public_albums'].first().photos)

    def test_image_view_albums_public(self):
        """Test image view albums are public."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('album'))
        self.assertEqual(response.context['public_albums'].first().published, 'PUBLIC')

    def test_image_view_public_photos(self):
        """Test image view public_photos."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('photo'))
        self.assertEqual(len(response.context['public_photos']), 5)

    def test_image_view_public_photos_album(self):
        """Test image view album on a public photo."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('photo'))
        self.assertIsNotNone(response.context['public_photos'].first().albums)

    def test_image_view_photos_public(self):
        """Test image view photos are public."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('photo'))
        self.assertEqual(response.context['public_photos'].first().published, 'PUBLIC')

    def test_image_view_album_detail(self):
        """Test image view album detail."""
        self.client.force_login(self.user)
        album = Album.objects.first()
        response = self.client.get(reverse_lazy('album_detail', kwargs={'id': album.id}))
        self.assertEqual(response.context['this_album'].published, 'PUBLIC')

    def test_image_view_album_detail_invalid(self):
        """Test image view album detail that doesnt exist."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('album_detail', kwargs={'id': 9999}))
        self.assertEqual(response.context['this_album'], None)

    def test_image_view_album_detail_not_signed_in(self):
        """Test image view album detail while not signed in."""
        album = Album.objects.first()
        response = self.client.get(reverse_lazy('album_detail', kwargs={'id': album.id}))
        self.assertEqual(response.context['this_album'].published, 'PUBLIC')

    def test_image_view_photo_detail(self):
        """Test image view photo detail."""
        self.client.force_login(self.user)
        photo = Photo.objects.first()
        response = self.client.get(reverse_lazy('photo_detail', kwargs={'id': photo.id}))
        self.assertIsNotNone(response.context['this_photo'])

    def test_image_view_photo_detail_invalid(self):
        """Test image view photo detail that doesnt exist."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('photo_detail', kwargs={'id': 9999}))
        self.assertEqual(response.context['this_photo'], None)

    def test_image_view_photo_detail_not_signed_in(self):
        """Test image view photo detail while not signed in."""
        photo = Photo.objects.first()
        response = self.client.get(reverse_lazy('photo_detail', kwargs={'id': photo.id}))
        self.assertIsNotNone(response.context['this_photo'])