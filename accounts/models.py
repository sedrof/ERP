
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from Entity.models import Entity

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user
        
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.create_user(
            email= self.normalize_email(email),
            password= password,
        )
        user.is_admin= True
        user.is_staff= True
        user.is_superuser= True
        user.save(using= self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
    A class implementing a fully featured User model with admin-compliant
    permissions.

    Email and password are required. Other fields are optional.
    """

    email = models.EmailField(
        _('Email Address'), unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    # entity = models.ForeignKey
    username = models.CharField(
        _('Username'), max_length=30, unique=True, blank=True, null=True,
        help_text=_('30 characters or fewer. Letters, digits and _ only.'),
        validators=[
            validators.RegexValidator(
                r'^\w+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers and _ character.'),
                'invalid'
            ),
        ],
        error_messages={
            'unique': _("The username is already taken."),
        }
    )
    is_staff = models.BooleanField(
        _('Staff Status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.')
    )
    is_active = models.BooleanField(
        _('Active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'

    class Meta(object):
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = False

    def get_full_name(self):
        """
        Returns email instead of the fullname for the user.
        """
        return (self.email)

    def get_short_name(self):
        """
        Returns the short name for the user.
        This function works the same as `get_full_name` method.
        It's just included for django built-in user comparability.
        """
        return self.get_full_name()

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
