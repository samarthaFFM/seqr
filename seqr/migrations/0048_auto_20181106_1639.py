# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def set_parent_objects(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    # see https://docs.djangoproject.com/en/1.11/ref/migration-operations/#django.db.migrations.operations.RunPython
    Individual = apps.get_model("seqr", "Individual")
    db_alias = schema_editor.connection.alias
    individuals_by_id = {i.individual_id: i for i in Individual.objects.using(db_alias).all()}
    for i in individuals_by_id.values():
        if i.maternal_id or i.paternal_id:
            i.mother = individuals_by_id[i.maternal_id] if i.maternal_id else None
            i.father = individuals_by_id[i.paternal_id] if i.paternal_id else None
            i.save()


def set_parent_ids(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    # see https://docs.djangoproject.com/en/1.11/ref/migration-operations/#django.db.migrations.operations.RunPython
    Individual = apps.get_model("seqr", "Individual")
    db_alias = schema_editor.connection.alias
    for i in Individual.objects.using(db_alias).all():
        if i.mother or i.father:
            i.maternal_id = i.mother.individual_id if i.mother else None
            i.paternal_id = i.father.individual_id if i.father else None
            i.save()


class Migration(migrations.Migration):

    dependencies = [
        ('seqr', '0047_merge_20180809_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='seqr.Individual'),
        ),
        migrations.AddField(
            model_name='individual',
            name='mother',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='seqr.Individual'),
        ),

        migrations.RunPython(set_parent_objects, reverse_code=set_parent_ids),

        migrations.RemoveField(
            model_name='individual',
            name='maternal_id',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='paternal_id',
        ),
    ]
