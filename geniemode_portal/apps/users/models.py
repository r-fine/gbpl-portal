from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


DEPARTMENTS = (('A', 'A'), ('B', 'B'), ('C', 'C'),)
DESIGNATION = (('X', 'X'), ('Y', 'Y'), ('Z', 'Z'),)


class User(AbstractUser):
    """
    Default custom user model for Geniemode Portal.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(_("E-mail Address"), unique=True)
    phone = models.CharField(_("Phone Number"), max_length=11, null=True)
    designation = models.CharField(_("Department"), choices=DESIGNATION, max_length=50, null=True)
    department = models.CharField(_("Department"), choices=DEPARTMENTS, max_length=50, null=True)
    profile_pic = models.ImageField(
        verbose_name='Profile Picture',
        upload_to="images/",
        default="images/500_500.png"
    )
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
