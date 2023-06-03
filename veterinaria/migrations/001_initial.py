from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipoAnimal', models.CharField(max_length=100)),
                ('fnac', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
            ],
        ),
    ]