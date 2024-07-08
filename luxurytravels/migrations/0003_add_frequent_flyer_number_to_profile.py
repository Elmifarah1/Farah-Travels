from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('luxurytravels', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='frequent_flyer_number',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='emergency_contact_name',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='emergency_contact_phone',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
    ]
