import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.TextField(verbose_name="ФИО", null = True, blank = True)
    nickname = models.TextField(verbose_name="Никнейм", null = True, blank = True)
    score = models.IntegerField(verbose_name="Баланс баллов", null = True, blank = True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.nickname

# эту штуку надо будет перенести в экшен регистрации пользователя(не копипастом)
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Client.objects.create(user=instance)
#     instance.client.save()

class Location(models.Model):
    name = models.TextField(verbose_name="Название места", null = True, blank = True)
    coordinate_x = models.TextField(verbose_name="Долгота", null = True, blank = True)
    coordinate_y = models.TextField(verbose_name="Широта", null = True, blank = True)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class Urn(models.Model):
    UUID = models.UUIDField('UUID мусорки', default=uuid.uuid4, editable=False)
    TRASH_TYPE_CHOICES = (
        ("GLASS", "GLASS"),
        ("PLASTIC", "PLASTIC"),
        ("PAPER", "PAPER"),
        ("METAL", "METAL"),
        ("BATTERIES", "BATTERIES"),
        ("OTHER", "OTHER"),
    )

    location = models.ForeignKey("Location",
                                 verbose_name="Местоположение",
                                 related_name="location_urns",
                                 on_delete="CASCADE")
    trash_type = models.TextField(verbose_name="Тип мусора",
                                  choices=TRASH_TYPE_CHOICES)

    class Meta:
        verbose_name = "Мусорка"
        verbose_name_plural = "Мусорки"

    def __str__(self):
        return str(self.location) + " " + str(self.id)

