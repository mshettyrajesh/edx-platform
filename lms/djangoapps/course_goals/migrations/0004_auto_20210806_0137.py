# Generated by Django 2.2.24 on 2021-08-06 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_goals', '0003_historicalcoursegoal'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegoal',
            name='days_per_week',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coursegoal',
            name='subscribed_to_reminders',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalcoursegoal',
            name='days_per_week',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalcoursegoal',
            name='subscribed_to_reminders',
            field=models.BooleanField(default=False),
        ),
    ]
