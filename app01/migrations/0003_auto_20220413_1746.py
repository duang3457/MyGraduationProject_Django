# Generated by Django 2.0.1 on 2022-04-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_department_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_POSCAR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('value', models.CharField(default=0, max_length=32, verbose_name='数值')),
            ],
        ),
        migrations.RenameModel(
            old_name='Department',
            new_name='Model_INCAR',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='depart',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
