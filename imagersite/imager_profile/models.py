"""Models for the profiles."""

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.dispatch import receiver


class ImagerProfile(models.Model):
    """Database model for the Imager Profile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    website = models.URLField(max_length=180, blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    camera = models.CharField(max_length=180, blank=True, null=True,
                              choices=(('DSLR', 'Digital Single Lens Reflex'),
                                       ('M', 'Mirrorless'),
                                       ('AC', 'Advanced Compact'),
                                       ('SLR', 'Single Lens Reflex')))

    services = MultiSelectField(
        choices=(('weddings', 'Weddings'),
                 ('headshots', 'HeadShots'),
                 ('landscape', 'LandScape'),
                 ('portraits', 'Portraits'),
                 ('art', 'Art')))

    photostyles = MultiSelectField(
        choices=(('blackandwhite', 'Black and White'),
                 ('night', 'Night'),
                 ('macro', 'Macro'),
                 ('3d', '3D'),
                 ('artistic', 'Artistic'),
                 ('underwater', 'Underwater')))

    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Show the stringed username."""
        return self.user.username

    @classmethod
    def active(cls):
        """Show if profile is active."""
        return cls.objects.filter(is_active=True)


@receiver(models.signals.post_save, sender=User)
def create_profile(sender, **kwargs):
    """Implement the reciever for the profile."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
