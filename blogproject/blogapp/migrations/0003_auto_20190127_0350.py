# Generated by Django 2.1.5 on 2019-01-27 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20190127_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=30)),
                ('auth_bio', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='blog_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Author'),
        ),
    ]
