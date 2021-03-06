# Generated by Django 2.0.5 on 2018-06-09 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reddit_clone', '0002_sub_reddit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('sub_reddit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='reddit_clone.Sub_Reddit')),
            ],
        ),
    ]
