from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


DEPARTMENTS = (
    ('ALL', 'All'), ('Operation', 'Operation'), ('Design & Business Development',
                                                 'Design & Business Development'), ('Merchandising', 'Merchandising'),
)
DESIGNATION = (
    ('Vice President', 'Vice President'), ('Business Head', 'Business Head'), ('Merchandising Manager', 'Merchandising Manager'), ('Merchandiser', 'Merchandiser'), ('Assistant Merchandiser',
                                                                                                                                                                     'Assistant Merchandiser'), ('Trainee Merchandiser', 'Trainee Merchandiser'), ('Senior Merchandiser', 'Senior Merchandiser'), ('Assistant Merchandiser officer', 'Assistant Merchandiser officer'),
)


class User(AbstractUser):
    """
    Default custom user model for Geniemode Attendance.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Full Name of Employee"), blank=True, max_length=255)
    email = models.EmailField(_("E-mail Address"), unique=True)
    phone = models.CharField(_("Phone Number"), max_length=11, null=True)
    department = models.CharField(_("Department"), choices=DEPARTMENTS, max_length=50, null=True)
    designation = models.CharField(_("Designation"), choices=DESIGNATION, max_length=50, null=True)
    profile_pic = models.ImageField(
        verbose_name='Profile Picture',
        upload_to="images/",
        default="images/500_500.png"
    )
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def get_absolute_url(self):
        return reverse('users:update')


User._meta.get_field('username').blank = True
