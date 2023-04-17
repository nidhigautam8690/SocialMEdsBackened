# Generated by Django 3.2 on 2021-04-21 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_mobile', models.IntegerField(max_length=30)),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General_App.role')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_plan_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General_App.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General_App.companyname')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_website', models.CharField(max_length=50)),
                ('company_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('mobile_number', models.IntegerField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General_App.category')),
                ('comapny_planS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General_App.plan')),
                ('company_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General_App.companyname')),
            ],
        ),
    ]