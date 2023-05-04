# Generated by Django 3.2.4 on 2023-03-28 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqs', '0005_layer_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='geojson',
            field=models.JSONField(verbose_name='Layer GeoJSON'),
        ),
        migrations.CreateModel(
            name='LayerAccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=64, verbose_name='Application name')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='access_logs', to='sqs.layer')),
            ],
            options={
                'ordering': ('-when',),
            },
        ),
    ]