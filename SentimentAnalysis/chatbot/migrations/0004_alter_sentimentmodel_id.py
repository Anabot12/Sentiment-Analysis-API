# Generated by Django 4.2.2 on 2023-07-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_alter_sentimentmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentimentmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]