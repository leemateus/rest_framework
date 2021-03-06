# Generated by Django 2.1.1 on 2019-05-14 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lograduro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('pessoa', models.ManyToManyField(to='api.Pessoa')),
            ],
        ),
    ]
