import uuid
from django.db import models


class Client(models.Model):
    email = models.EmailField(verbose_name="Почта")
    password = models.TextField(verbose_name="Пароль")
    token = models.UUIDField(verbose_name="Токен",
                             default=uuid.uuid4,
                             editable=False)
    firstname = models.TextField(verbose_name="Имя клиента")
    surname = models.TextField(verbose_name="Фамилия клиента")
    phone = models.TextField(verbose_name="Номер телефона")
    score = models.IntegerField(verbose_name="Баланс баллов",
                                default=0)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.email


class Location(models.Model):
    name = models.TextField(verbose_name="Название места")
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class Trashcan(models.Model):
    # name = models.TextField(verbose_name="Название мусорки")
    location = models.ForeignKey("Location",
                                 verbose_name="Местоположение",
                                 related_name="location_urns",
                                 on_delete="CASCADE")

    class Meta:
        verbose_name = "Мусорка"
        verbose_name_plural = "Мусорки"

    def __str__(self):
        return str(self.location)


class Company(models.Model):
    name = models.TextField(verbose_name="Название организации")
    location = models.ForeignKey("Location",
                                 verbose_name="Местоположение",
                                 related_name="location_companies",
                                 on_delete="CASCADE")

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return str(self.name) + " " + str(self.location)


class Urn(models.Model):
    TRASH_TYPE_CHOICES = (
        ("GLASS", "GLASS"),
        ("PLASTIC", "PLASTIC"),
        ("PAPER", "PAPER"),
        ("METAL", "METAL"),
        ("BATTERIES", "BATTERIES"),
        ("OTHER", "OTHER"),
    )

    UUID = models.UUIDField('UUID мусорки',
                            default=uuid.uuid4,
                            editable=False)
    trash_type = models.TextField(verbose_name="Тип мусора",
                                  choices=TRASH_TYPE_CHOICES)

    workload = models.IntegerField(verbose_name="Загруженность урны",
                                   default=0)

    trashcan = models.ForeignKey("Trashcan",
                                 verbose_name="Мусорка",
                                 related_name="trashcan_urn",
                                 on_delete="CASCADE")

    class Meta:
        verbose_name = "Урна"
        verbose_name_plural = "Урны"

    def __str__(self):
        return str(self.trashcan.location) + " " + str(self.trash_type)

