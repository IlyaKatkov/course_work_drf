from django.db import models
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class NiceHabit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=100, **NULLABLE, verbose_name='место')
    action = models.CharField(max_length=100, verbose_name='действие')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    time = models.TimeField(verbose_name='время')
    place = models.CharField(max_length=100, verbose_name='место')
    action = models.CharField(max_length=100, verbose_name='действие')
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name='вознаграждение')
    associated_nice_habit = models.ForeignKey(NiceHabit, on_delete=models.SET_NULL,
                                              **NULLABLE, verbose_name='связанная привычка')
    periodicity = models.PositiveIntegerField(verbose_name='периодичность')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    duration_time = models.TimeField(verbose_name='продолжительность')
    next_date = models.DateField(**NULLABLE, verbose_name="дата следующего действия")

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
