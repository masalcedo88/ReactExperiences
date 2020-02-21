# Generated by Django 3.0.3 on 2020-02-20 23:35


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('picture', models.ImageField(blank=True, upload_to='adventure_image')),
                ('location', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adventures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booked', models.DateField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='main_app.Adventure')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
