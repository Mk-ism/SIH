# Generated by Django 3.0.2 on 2020-01-19 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20200119_0150'),
        ('report', '0003_auto_20200118_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportbasic',
            name='reportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='report.ReportString'),
        ),
        migrations.AlterField(
            model_name='reportlist',
            name='reportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='report.ReportString'),
        ),
        migrations.AlterField(
            model_name='reportstring',
            name='ident',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='login.LoginData'),
        ),
        migrations.AlterField(
            model_name='reportvalues',
            name='reportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='report.ReportString'),
        ),
    ]
