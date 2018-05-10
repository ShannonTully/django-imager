"""Tests for imagersite."""

from django.test import TestCase
from django.core import mail
from urllib.parse import urlparse
import factory
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
import tempfile


class UserFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of users."""

    class Meta:
        """User meta model."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


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


class AlbumFactory(factory.django.DjangoModelFactory):
    """Creating a bunch of albums."""

    class Meta:
        """Album meta model."""

        model = Album

    title = factory.Faker('company')
    date_created = factory.Faker('date_time')
    date_modified = factory.Faker('date_time')
    published = 'PUBLIC'


class EmptyViewTests(TestCase):
    """Class for testing views."""

    def test_home_view_empty(self):
            """Test home view public photos are empty."""
            response = self.client.get('/')
            self.assertEqual(response.context['image_title'], 'logo')


class BasicViewTests(TestCase):
    """Class for testing views."""

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
        Photo.objects.all().delete()

    def test_home_view_correct(self):
        """Test that the first value pased to the home view is the correct photo."""
        response = self.client.get('/')
        photo = Photo.objects.get(title=response.context['image_title'])
        self.assertEqual(response.context['image_url'], photo.image.url)

    def test_home_status(self):
        """Test home route status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        """Test home route template."""
        response = self.client.get('/')
        self.assertEqual(response.templates[0].name, 'generic/home.html')
    
    def test_home_base_template(self):
        """Test home route base template."""
        response = self.client.get('/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_login_status(self):
        """Test login route status code."""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_template(self):
        """Test login route template."""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.templates[0].name, 'registration/login.html')

    def test_login_base_template(self):
        """Test login route base template."""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_register_status(self):
        """Test register route status code."""
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_template(self):
        """Test register route template."""
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.templates[0].name, 'registration/registration_form.html')

    def test_register_base_template(self):
        """Test register route base template."""
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_logout_staus(self):
        """Test logout route staus code."""
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)

    def test_logout_template(self):
        """Test logout route template."""
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.templates[0].name, 'registration/logout.html')

    def test_logout_base_template(self):
        """Test logout route base template."""
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_register_user(self):
        """Test for user registration."""
        self.client.post('/accounts/register/', {'username': 'person', 'password1': 'codefellows1', 'password2': 'codefellows1', 'email': 'email@email.com'})
        email = mail.outbox[0]
        link = email.body.splitlines()[-1]
        link = urlparse(link)
        self.client.get(link.path)
        self.assertTrue(self.client.login(username='person', password='codefellows1'))


class ImagesRoutesTests(TestCase):
    """Class for testing views."""

    @classmethod
    def setUpClass(cls):
        """Test setup."""
        super(TestCase, cls)
        # fake = Faker()
        for _ in range(1):
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
        Photo.objects.all().delete()

    def test_library_status(self):
        """Test library route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/library/')
        self.assertEqual(response.status_code, 200)

    def test_library_template(self):
        """Test library route template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/library/')
        self.assertEqual(response.templates[0].name, 'imager_images/library.html')

    def test_library_base_template(self):
        """Test library route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/library/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_profile_status(self):
        """Test profile route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_template(self):
        """Test profile route template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/')
        self.assertEqual(response.templates[0].name, 'imager_profile/profile.html')

    def test_profile_base_template(self):
        """Test profile route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_profile_user_status(self):
        """Test profile route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/{}'.format(user.username))
        self.assertEqual(response.status_code, 200)

    def test_profile_user_template(self):
        """Test profile route template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/{}'.format(user.username))
        self.assertEqual(response.templates[0].name, 'imager_profile/profile.html')

    def test_profile_user_base_template(self):
        """Test profile route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/{}'.format(user.username))
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_album_status(self):
        """Test album route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/albums/')
        self.assertEqual(response.status_code, 200)

    def test_album_template(self):
        """Test album route template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/albums/')
        self.assertEqual(response.templates[0].name, 'imager_images/album.html')

    def test_album_base_template(self):
        """Test album route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/albums/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_photo_status(self):
        """Test photo route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/photos/')
        self.assertEqual(response.status_code, 200)

    def test_photo_template(self):
        """Test photo route template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/photos/')
        self.assertEqual(response.templates[0].name, 'imager_images/photo.html')

    def test_photo_base_template(self):
        """Test photo route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/photos/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_album_detail_status(self):
        """Test album_detail route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        album_id = Album.objects.first().id
        response = self.client.get(f'/images/albums/{album_id}')
        self.assertEqual(response.status_code, 200)

    def test_album_detail_template(self):
        """Test album_detail route template."""
        user = User.objects.first()
        self.client.force_login(user)
        album_id = Album.objects.first().id
        response = self.client.get(f'/images/albums/{album_id}')
        self.assertEqual(response.templates[0].name, 'imager_images/album_detail.html')

    def test_album_detail_base_template(self):
        """Test album_detail route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        album_id = Album.objects.first().id
        response = self.client.get(f'/images/albums/{album_id}')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_photo_detail_status(self):
        """Test photo_detail route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        photo_id = Photo.objects.first().id
        response = self.client.get(f'/images/photos/{photo_id}')
        self.assertEqual(response.status_code, 200)

    def test_photo_detail_template(self):
        """Test photo_detail route template."""
        user = User.objects.first()
        self.client.force_login(user)
        photo_id = Photo.objects.first().id
        response = self.client.get(f'/images/photos/{photo_id}')
        self.assertEqual(response.templates[0].name, 'imager_images/photo_detail.html')

    def test_photo_detail_template_base(self):
        """Test photo_detail route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        photo_id = Photo.objects.first().id
        response = self.client.get(f'/images/photos/{photo_id}')
        self.assertEqual(response.templates[1].name, 'generic/base.html')
