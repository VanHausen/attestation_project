# Generated by Django 4.2 on 2023-04-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factory',
            options={'verbose_name': 'Завод', 'verbose_name_plural': 'Заводы'},
        ),
        migrations.AlterModelOptions(
            name='individualentrepreneur',
            options={'verbose_name': 'Индивидуальный предприниматель', 'verbose_name_plural': 'Индивидуальныe предприниматели'},
        ),
        migrations.AlterModelOptions(
            name='networknode',
            options={'verbose_name': 'Сеть', 'verbose_name_plural': 'Сети'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='retailnetwork',
            options={'verbose_name': 'Розничная сеть', 'verbose_name_plural': 'Розничные сети'},
        ),
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
