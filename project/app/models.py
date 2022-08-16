from django.db import models
from org.models import DepartmentModel
from django.contrib.auth.models import User


class DeviceModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование (модель)")
    note = models.CharField(max_length=200, verbose_name="Примечание")

    def __str__(self):
        return self.name


class CartridgeModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    m_code = models.CharField(max_length=50, null=True, blank=True, verbose_name="Код производителя")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата, время регистрации")
    reg_user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        verbose_name="Регистратор"
    )
    customer_department = models.ForeignKey(
        DepartmentModel,
        on_delete=models.CASCADE,
        verbose_name='Подразделение заказчика'
    )
    customer_name = models.CharField(max_length=30, verbose_name='ФИО Заказчика')
    customer_phone = models.CharField(max_length=30, blank=True, verbose_name='Телефон заказчика')
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE, verbose_name="Устройство")
    barcode = models.CharField(max_length=30, unique=True, verbose_name='Штрих-код')
    decommissioned = models.BooleanField(verbose_name="Выведен из экстплуатации")


    def __str__(self):
        return '%s: %s (%s) для %s ' % (self.barcode, self.m_code, self.name, self.device)

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджи'
        ordering = ['-reg_date']


