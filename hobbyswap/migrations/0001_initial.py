# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Condition'
        db.create_table(u'hobbyswap_condition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hobbyswap', ['Condition'])

        # Adding model 'Item'
        db.create_table(u'hobbyswap_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_post', to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=4000)),
            ('price', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('deposit', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('condition', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_condition', to=orm['hobbyswap.Condition'])),
            ('beg_availability', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_availability', self.gf('django.db.models.fields.DateTimeField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'hobbyswap', ['Item'])

        # Adding model 'Renter'
        db.create_table(u'hobbyswap_renter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='renter', to=orm['auth.User'])),
            ('rentals', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['hobbyswap.Item'])),
        ))
        db.send_create_signal(u'hobbyswap', ['Renter'])


    def backwards(self, orm):
        # Deleting model 'Condition'
        db.delete_table(u'hobbyswap_condition')

        # Deleting model 'Item'
        db.delete_table(u'hobbyswap_item')

        # Deleting model 'Renter'
        db.delete_table(u'hobbyswap_renter')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hobbyswap.condition': {
            'Meta': {'object_name': 'Condition'},
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'hobbyswap.item': {
            'Meta': {'object_name': 'Item'},
            'beg_availability': ('django.db.models.fields.DateTimeField', [], {}),
            'condition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_condition'", 'to': u"orm['hobbyswap.Condition']"}),
            'deposit': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            'end_availability': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_post'", 'to': u"orm['auth.User']"}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'hobbyswap.renter': {
            'Meta': {'object_name': 'Renter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'renter'", 'to': u"orm['auth.User']"}),
            'rentals': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['hobbyswap.Item']"})
        }
    }

    complete_apps = ['hobbyswap']