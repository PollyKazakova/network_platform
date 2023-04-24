from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

USER = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to="profile_images",
                                    default="blank-profile-picture.png")
    location = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=80)
    image = models.ImageField(upload_to="post_images", blank=True)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=80)

    def __str__(self):
        return self.username
