# Generated by Django 4.0.4 on 2022-07-29 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_payment_match_payment_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.player'),
        ),
    ]
