from django.db import models


class Product(models.Model):
    """
        Modelo da minha aplicação.
        : values_choices: As duas opções para o Status do produto

    """

    values_choices = [
        ('draft', 'draft'),
        ('imported', 'imported')
    ]

    code = models.BigIntegerField(null=False, default=0)
    barcode = models.CharField(max_length=35)
    status = models.CharField(max_length=10, choices=values_choices)
    imported_t = models.DateTimeField(auto_now=False, auto_now_add=True)
    url = models.CharField(max_length=150)
    product_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    categories = models.CharField(max_length=450)
    packaging = models.CharField(max_length=450)
    brands = models.CharField(max_length=450)
    image_url = models.CharField(max_length=150)

    def __str__(self):
        """
            :return: retorna o nome do produto no site de administração.
        """
        return self.product_name
