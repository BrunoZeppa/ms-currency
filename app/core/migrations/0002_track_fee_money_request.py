from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track_fee',
            name='money_request',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]