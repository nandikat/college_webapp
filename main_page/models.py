# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


##class Student(models.Model):
##    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
##    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
##    course = models.CharField(max_length=20, blank=True, null=True)
##
##    class Meta:
##        managed = False
##        db_table = 'student'

##class Student(models.Model):
##    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
##    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
##    course = models.CharField(max_length=20, blank=True, null=True)
##    pwd = models.CharField(max_length=10, blank=True, null=True)
##
##    class Meta:
##        managed = False
##        db_table = 'student'

class Student(models.Model):
    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(max_length=20, blank=True, null=True)
    pwd = models.CharField(max_length=10, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

        
class Scores(models.Model):
    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
    subject_1 = models.IntegerField(blank=True, null=True)
    subject_2 = models.IntegerField(blank=True, null=True)
    subject_3 = models.IntegerField(blank=True, null=True)
    subject_4 = models.IntegerField(blank=True, null=True)
    subject_5 = models.IntegerField(blank=True, null=True)
    subject_6 = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scores'

##class TimeTable(models.Model):
##    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
##    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
##    monday = models.CharField(db_column='Monday', max_length=20, blank=True, null=True)  # Field name made lowercase.
##    tuesday = models.CharField(db_column='Tuesday', max_length=20, blank=True, null=True)  # Field name made lowercase.
##    wednesday = models.CharField(db_column='Wednesday', max_length=20, blank=True, null=True)  # Field name made lowercase.
##    thursday = models.CharField(db_column='Thursday', max_length=20, blank=True, null=True)  # Field name made lowercase.
##    friday = models.CharField(db_column='Friday', max_length=20, blank=True, null=True)  # Field name made lowercase.
##
##    class Meta:
##        managed = False
##        db_table = 'time_table'

class TimeTable(models.Model):
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    monday = models.CharField(db_column='Monday', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tuesday = models.CharField(db_column='Tuesday', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wednesday = models.CharField(db_column='Wednesday', max_length=20, blank=True, null=True)  # Field name made lowercase.
    thursday = models.CharField(db_column='Thursday', max_length=20, blank=True, null=True)  # Field name made lowercase.
    friday = models.CharField(db_column='Friday', max_length=20, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=20, blank=True, null=True)  # Field name made lowercase.
    semester = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_table'



class Fees(models.Model):
    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    paid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees'

class Attendance(models.Model):
    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendance'

class Tutor(models.Model):
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=20, blank=True, null=True)  # Field name made lowercase.
    roll_no = models.IntegerField(db_column='Roll_no', blank=True, null=True)  # Field name made lowercase.
    subject_1 = models.CharField(db_column='Subject_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subject_2 = models.CharField(db_column='Subject_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subject_3 = models.CharField(db_column='Subject_3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subject_4 = models.CharField(db_column='Subject_4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subject_5 = models.CharField(db_column='Subject_5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subject_6 = models.CharField(db_column='Subject_6', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tutor'


