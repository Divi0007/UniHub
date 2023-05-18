# Generated by Django 4.1.6 on 2023-02-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_event_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='participants', to='main.participant'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='events',
            field=models.ManyToManyField(blank=True, null=True, related_name='registered_events', to='main.event'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='events',
            field=models.ManyToManyField(blank=True, null=True, related_name='events_presenting', to='main.event'),
        ),
    ]
