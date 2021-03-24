# Generated by Django 2.2.6 on 2020-03-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('cost', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]