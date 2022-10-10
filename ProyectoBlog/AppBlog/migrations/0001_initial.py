# Generated by Django 4.1 on 2022-10-10 10:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id_categoria", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Estado",
            fields=[
                ("id_estado", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id_tag", models.AutoField(primary_key=True, serialize=False)),
                ("tag", models.CharField(max_length=200)),
                ("relacion", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("usuario", models.CharField(max_length=40)),
                ("password", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("lastlogin", models.DateTimeField()),
                ("dateregistro", models.DateTimeField()),
                ("datecupleanho", models.DateTimeField()),
                ("estado", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("autor", models.CharField(max_length=200)),
                ("titulo", models.CharField(max_length=200)),
                ("body", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("fechapublicacion", models.DateTimeField(auto_now_add=True)),
                ("imagen", models.ImageField(blank=True, null=True, upload_to="post")),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppBlog.categoria",
                    ),
                ),
                (
                    "estado",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppBlog.estado",
                    ),
                ),
                (
                    "tags",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppBlog.tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comentario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateTimeField(default=django.utils.timezone.now)),
                ("contenido", models.TextField()),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="AppBlog.post",
                    ),
                ),
            ],
        ),
    ]
