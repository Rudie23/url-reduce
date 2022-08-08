# Generated by Django 4.1 on 2022-08-08 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encurtador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('origem', models.URLField(blank=True, max_length=512, null=True)),
                ('user_agent', models.CharField(blank=True, max_length=512, null=True)),
                ('host', models.CharField(blank=True, max_length=512, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('url_redirect', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='logs', to='encurtador.urlredirect')),
            ],
        ),
    ]
