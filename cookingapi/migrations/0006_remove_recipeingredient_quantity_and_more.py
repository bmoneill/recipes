# Generated by Django 5.2.3 on 2025-06-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookingapi', '0005_alter_recipe_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='quantity',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='amount',
            field=models.FloatField(default=1.0, null=True),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(choices=[('unit', ''), ('tsp', 'Teaspoon'), ('dsp', 'Dessertspoon'), ('tbsp', 'Tablespoon'), ('floz', 'Fluid Ounce'), ('cup', 'Cup'), ('pt', 'Pint'), ('qt', 'Quart'), ('gal', 'Gallon'), ('l', 'Liter'), ('ml', 'Milliliter'), ('g', 'Gram'), ('mg', 'Milligram'), ('clov', 'Clove')], default='unit', max_length=4),
        ),
        migrations.DeleteModel(
            name='Quantity',
        ),
    ]
