from django.db import models


class DepartmentModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")

    def __str__(self):
        return self.name

