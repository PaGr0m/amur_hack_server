from django.db import models


class User(models.Model):
    login = models.TextField(verbose_name="Логин")
    password = models.TextField(verbose_name="Пароль")
    fio = models.TextField(verbose_name="ФИО")
    nickname = models.TextField(verbose_name="Никнейм")
    score = models.TextField(verbose_name="Баланс баллов")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.login


# Абсолютно не уверен в данном классе. Его делаю, чтобы урны могли
# ссылаться на {типы}. Возможно это все решается простым {enum}
# class TypesUrn(models.Model):
#     name = models.TextField(verbose_name="Тип мусора")
#
#     class Meta:
#         verbose_name = "Тип мусорки"
#         verbose_name_plural = "Типы мусорок"
#
#     def __str__(self):
#         return self.name


class Location(models.Model):
    name = models.TextField(verbose_name="Название места")
    coordinate_x = models.TextField(verbose_name="Долгота")
    coordinate_y = models.TextField(verbose_name="Широта")

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class Urn(models.Model):
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
    # types = models.ForeignKey("TypesUrn",
    #                           verbose_name="Тип",
    #                           related_name="type_urns",
    #                           on_delete="CASCADE")

    class Meta:
        verbose_name = "Мусорка"
        verbose_name_plural = "Мусорки"

    def __str__(self):
        return str(self.location) + " " + str(self.id)





