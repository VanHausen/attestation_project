from django.db import models


class NetworkNode(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'

    def __str__(self):
        return f'Узел {self.name}'


class Factory(NetworkNode):
    pass

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return f'Завод {self.name}'


class RetailNetwork(NetworkNode):
    pass

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return f'Розничная сеть {self.name}'


class IndividualEntrepreneur(NetworkNode):
    pass

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальныe предприниматели'

    def __str__(self):
        return f'Индивидуальный предприниматель {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    supplier = models.ForeignKey(NetworkNode, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'Товар {self.name}'
