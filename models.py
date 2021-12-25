# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Scores(models.Model):
    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
    subject_1 = models.IntegerField(blank=True, null=True)
    subject_2 = models.IntegerField(blank=True, null=True)
    subject_3 = models.IntegerField(blank=True, null=True)
    subject_4 = models.IntegerField(blank=True, null=True)
    subject_5 = models.IntegerField(blank=True, null=True)
    subject_6 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scores'


class Student(models.Model):
    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
