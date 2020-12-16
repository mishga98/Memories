from django.db import models


class Note(models.Model):
    title = models.CharField('Название', max_length=72)
    note = models.TextField('Описание')
    coordinates = models.CharField('Координаты', max_length=72)
    person = models.CharField('Автор', max_length=72)

    def __str__(self):
        return self.title
