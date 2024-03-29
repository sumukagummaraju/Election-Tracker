# Generated by Django 2.2.1 on 2019-05-03 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('optionId', models.IntegerField(primary_key=True, serialize=False)),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('questionId', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('password_enc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserSelectedOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeRegistered', models.DateTimeField()),
                ('optionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ET_App.Option')),
                ('questionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ET_App.Questions')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ET_App.User')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='questionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ET_App.Questions'),
        ),
    ]
