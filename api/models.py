from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # related_nameで逆参照できるようにしている
    user_prof = models.OneToOneField(User,
                                     related_name="profile",
                                     on_delete=models.CASCADE,
                                     )

    following = models.ManyToManyField(
        User, related_name='profile_followings', blank=True,
    )
    create_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_prof.username
