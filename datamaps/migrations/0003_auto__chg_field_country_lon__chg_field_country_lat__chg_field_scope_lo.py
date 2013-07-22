# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Country.lon'
        db.alter_column(u'datamaps_country', 'lon', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Country.lat'
        db.alter_column(u'datamaps_country', 'lat', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Scope.lon'
        db.alter_column(u'datamaps_scope', 'lon', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Scope.lat'
        db.alter_column(u'datamaps_scope', 'lat', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):

        # Changing field 'Country.lon'
        db.alter_column(u'datamaps_country', 'lon', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8))

        # Changing field 'Country.lat'
        db.alter_column(u'datamaps_country', 'lat', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8))

        # Changing field 'Scope.lon'
        db.alter_column(u'datamaps_scope', 'lon', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8))

        # Changing field 'Scope.lat'
        db.alter_column(u'datamaps_scope', 'lat', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8))

    models = {
        u'datamaps.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'radius': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'scope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datamaps.Scope']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'topo': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'datamaps.scope': {
            'Meta': {'object_name': 'Scope'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'scale': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '8'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'topo': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'datamaps.world': {
            'Meta': {'object_name': 'World'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topo': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['datamaps']