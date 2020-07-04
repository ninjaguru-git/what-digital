# Generated by Django 2.1.10 on 2019-07-31 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloatModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bs4_float_floatmodel', serialize=False, to='cms.CMSPlugin')),
                ('float_direction', models.CharField(choices=[('left', 'float left'), ('right', 'float right')], default='left', max_length=256)),
                ('float_breakpoint', models.CharField(blank=True, choices=[('', 'very small'), ('sm-', 'small'), ('md-', 'medium'), ('lg-', 'large'), ('xl-', 'very large')], default='', help_text='At which bootstrap4 breakpoint should the float behaviour start, starting from smallest.', max_length=256)),
                ('margin_top', models.PositiveIntegerField(default=0)),
                ('margin_right', models.PositiveIntegerField(default=0)),
                ('margin_bottom', models.PositiveIntegerField(default=0)),
                ('margin_left', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]