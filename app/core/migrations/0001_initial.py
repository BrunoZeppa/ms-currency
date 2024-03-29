from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id_currency', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=4)),
                ('exchange', models.FloatField()),
                ('fee_percentage', models.FloatField()),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Track_Fee',
            fields=[
                ('id_track_fee', models.AutoField(primary_key=True, serialize=False)),
                ('fee_amount', models.FloatField()),
                ('date_transaction', models.CharField(max_length=45)),
                ('base_currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='base', to='core.currency')),
                ('quote_currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote', to='core.currency')),
            ],
        ),
    ]