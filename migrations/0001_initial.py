# Generated by Django 4.2.13 on 2024-11-26 18:54

from django.db import migrations, models
import django.db.models.deletion
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("categoryName", models.CharField(unique=True)),
                ("localizedName", models.CharField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Item",
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
                ("assetid", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("name_color", models.CharField(blank=True, max_length=255, null=True)),
                ("name_on_market", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("isStattrak", models.BooleanField(default=False)),
                ("stattrak_stat", models.IntegerField(blank=True, null=True)),
                ("isTradable", models.BooleanField(default=True)),
                ("isMarketable", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="ItemType",
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
                ("itemTypeName", models.CharField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="PaymentMethod",
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
                ("paymentMethodName", models.CharField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Quality",
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
                ("qualityName", models.CharField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Rarity",
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
                ("rarityName", models.CharField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
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
                (
                    "rolename",
                    models.CharField(db_index=True, max_length=25, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StatusOrder",
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
                (
                    "statusOrderName",
                    models.CharField(db_index=True, max_length=50, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StatusPayment",
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
                (
                    "statusPaymentName",
                    models.CharField(db_index=True, max_length=50, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("login", models.CharField(max_length=25, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("nickname", models.CharField(blank=True, max_length=25)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("date_created", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("balance", models.FloatField(blank=True, default=0)),
                ("steamid", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "steam_profile_url",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "steam_avatar_url",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "role",
                    models.ForeignKey(
                        blank=True,
                        default=2,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LolzMarket.role",
                    ),
                ),
            ],
            options={
                "index_together": {("login", "password", "nickname")},
            },
        ),
        migrations.CreateModel(
            name="Transactions",
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
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LolzMarket.order",
                    ),
                ),
                (
                    "paymentMethod",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LolzMarket.paymentmethod",
                    ),
                ),
                (
                    "statusPayment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LolzMarket.statuspayment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("tagName", models.CharField(unique=True)),
                ("lozalizedName", models.CharField(unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LolzMarket.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order_Item",
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
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LolzMarket.item",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LolzMarket.order",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="statusOrder",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="LolzMarket.statusorder"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="LolzMarket.user"
            ),
        ),
        migrations.CreateModel(
            name="ItemTag",
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
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LolzMarket.item",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="LolzMarket.tag"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="quality",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="LolzMarket.quality"
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="rarity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="LolzMarket.rarity"
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="LolzMarket.itemtype"
            ),
        ),
        migrations.CreateModel(
            name="Assortment",
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
                ("quantity", models.IntegerField(default=0)),
                ("isInStock", models.BooleanField(default=True)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LolzMarket.item",
                    ),
                ),
            ],
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="user",
            trigger=pgtrigger.compiler.Trigger(
                name="user",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='UPDATE "LolzMarket_user" SET is_active = False WHERE "id" = OLD."id"; RETURN NULL;',
                    hash="27501284905a240c3656e95b6a982c1d80ec6e33",
                    operation="DELETE",
                    pgid="pgtrigger_user_4ca6b",
                    table="LolzMarket_user",
                    when="BEFORE",
                ),
            ),
        ),
    ]
