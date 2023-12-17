# Generated by Django 4.2.8 on 2023-12-17 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("habits", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="habit",
            options={"verbose_name": "привычка", "verbose_name_plural": "привычки"},
        ),
        migrations.RemoveField(
            model_name="habit",
            name="award",
        ),
        migrations.RemoveField(
            model_name="habit",
            name="frequency",
        ),
        migrations.RemoveField(
            model_name="habit",
            name="pleasant_habit",
        ),
        migrations.RemoveField(
            model_name="habit",
            name="time",
        ),
        migrations.RemoveField(
            model_name="habit",
            name="time_to_complete",
        ),
        migrations.RemoveField(
            model_name="habit",
            name="user",
        ),
        migrations.AddField(
            model_name="habit",
            name="is_pleasant",
            field=models.BooleanField(default=False, verbose_name="Приятная привычка"),
        ),
        migrations.AddField(
            model_name="habit",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="periodicity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1", "раз в 7 дней"),
                    ("2", "2 раза в 7 дней"),
                    ("3", "3 раза в 7 дней"),
                    ("4", "4 раза в 7 дней"),
                    ("5", "5 раз в 7 дней"),
                    ("6", "6 раз в 7 дней"),
                    ("7", "7 раз в 7 дней"),
                ],
                default=1,
                max_length=10,
                null=True,
                verbose_name="Cколько раз в неделю",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="reward",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Вознаграждение"
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="time_complete",
            field=models.IntegerField(
                default=1, verbose_name="Время на выполнение в сек"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="habit",
            name="time_start",
            field=models.TimeField(default=2, verbose_name="Время выполнения привычки"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="habit",
            name="action",
            field=models.CharField(max_length=150, verbose_name="Действие"),
        ),
        migrations.AlterField(
            model_name="habit",
            name="is_published",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="Опубликована"
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="place",
            field=models.CharField(max_length=50, verbose_name="Место"),
        ),
        migrations.AlterField(
            model_name="habit",
            name="related_habit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="habits.habit",
                verbose_name="Связанная привычка",
            ),
        ),
    ]