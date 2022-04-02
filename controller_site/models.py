from django.db import models

class Preset(models.Model):
    power = models.BooleanField(default=False)  # Питание (вкл/выкл)
    brightness = models.IntegerField()  # Яркость
    color = models.TextField()  # Цвет (потом дописать сюда правильное поле)
    degree_x = models.IntegerField()  # Угол поворота по оси X
    degree_y = models.IntegerField()  # Угол поворота по оси Y
    position = models.IntegerField()  # Положение над сценой на рельсах

