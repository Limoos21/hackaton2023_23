from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from shop.models import Quiz










class ContribUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField("Баллы пользователя", default=0)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.user)


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def created_user_profile(sender, instance, created, **kwargs):
    if created:
        ContribUsers.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.ContribUsers.save()
