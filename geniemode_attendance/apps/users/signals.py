from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import User

current_site = Site.objects.get_current()
site_domain = current_site.domain
site_name = current_site.name


@receiver(post_save, sender=User)
def send_email_on_user_creation(sender, instance, **kwargs):
    email = instance.email
    s = email.split('@')[0]
    password = s[0] + s[-1] + '@gbpl23'
    change_password_url = site_domain + '/accounts/password/change/'

    context = {
        'site_domain': site_domain,
        'site_name': site_name,
        'email': email,
        'password': password,
        'change_password_url': change_password_url,
    }

    html_path = str(settings.APPS_DIR) + '/templates/account/new_user_creation_email.html'
    msg_html = render_to_string(html_path, context)

    subject = 'New User Created on ' + site_domain
    recipient = [instance.email]

    send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, recipient, html_message=msg_html)
