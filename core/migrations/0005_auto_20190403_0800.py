# Generated by Django 2.2 on 2019-04-03 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190402_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='star',
            name='user_star',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authored_stars', to=settings.AUTH_USER_MODEL),
        ),
    ]
