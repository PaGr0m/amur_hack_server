import uuid
from django.db import models


class Client(models.Model):
    login = models.TextField(verbose_name="Логин")
    password = models.TextField(verbose_name="Пароль")
    token = models.UUIDField(verbose_name="Токен",
                             default=uuid.uuid4,
                             editable=False)
    fio = models.TextField(verbose_name="ФИО")
    nickname = models.TextField(verbose_name="Никнейм")
    score = models.IntegerField(verbose_name="Баланс баллов")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.nickname


class Location(models.Model):
    name = models.TextField(verbose_name="Название места")
    longitude = models.TextField(verbose_name="Долгота")
    latitude = models.TextField(verbose_name="Широта")

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

    workload = models.IntegerField(verbose_name="Загруженность урны")

    trashcan = models.ForeignKey("Trashcan",
                                 verbose_name="Мусорка",
                                 related_name="trashcan_urn",
                                 on_delete="CASCADE")

    class Meta:
        verbose_name = "Урна"
        verbose_name_plural = "Урны"

    def __str__(self):
        return str(self.trashcan.location) + " " + str(self.trash_type)

