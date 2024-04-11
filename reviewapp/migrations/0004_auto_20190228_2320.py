# Generated by Django 2.1.7 on 2019-02-28 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0003_auto_20190227_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='review_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='review_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]