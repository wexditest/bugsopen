from django.db import models

# Create your models here.
from django.db import models
from datetime import date
import datetime
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here.
PRIORITY = (
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    )
PHASE = (
        ('US', 'US'),
        ('ISSUE', 'ISSUE'),
        ('OTHER', 'OTHER'),
    )
MONTH = (
        ('1', 'JAN'),
        ('2', 'FEB'),
        ('3', 'MAR'),
        ('4', 'APR'),
        ('5', 'MAY'),
        ('6', 'JUN'),
        ('7', 'JUL'),
        ('8', 'AUG'),
        ('9', 'SEPT'),
        ('10', 'OCT'),
        ('11', 'NOV'),
        ('12', 'DEC'),
    )
SCORE = (
        ('1', '1'),
        ('3', '3'),
        ('5', '5'),
        ('8', '8'),
        ('13', '13'),
        ('21', '21'),

    )

STATUS = (
        ('NOTSTARTED', 'NOT-STARTED'),
        ('INPROGRESS', 'IN-PROGRESS'),
        ('FIXED', 'FIXED'),
        ('HOLD', 'HOLD'),
        ('OPEN', 'OPEN'),
        ('REOPEN', 'REOPEN'),
        ('CLOSE', 'CLOSE'),

    )

ADMIN_PEOPLE = (
        ('DEEPAK', 'DEEPAK'),
        ('SANTHOSH', 'SANTHOSH'),
        ('AJAY', 'AJAY'),
    )

class ReleaseDetails(models.Model):
    release_name = models.CharField(max_length=80,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.release_name)

class Board(models.Model):
    board_name = models.CharField(max_length=80,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.board_name)


BUGSTATUS = (
        ('Bug', 'Bug'),
        ('BugTesting', 'BugTesting'),
        ('UserStory', 'UserStory'),
        ('UserStoryTesting', 'UserStoryTesting'),
    )


import datetime
LEVELSTATUS = (
        ('Easy', 'Easy'),
        ('Normal', 'Normal'),
        ('Moderate', 'Moderate'),
        ('Difficult', 'Difficult'),
    )





class Bug(models.Model):
    record_date = models.DateField(default=datetime.date.today)
    release_det = models.ForeignKey(ReleaseDetails,verbose_name = 'Release Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    board_obj = models.ForeignKey(Board,verbose_name = 'Board Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    board_id = models.CharField(max_length=80,blank=True, null=True)
    kadet_id = models.CharField(max_length=80,blank=True, null=True)
    start_date = models.DateField(default=datetime.date.today)
    bug_type = models.CharField(max_length=100, blank=True, null=True, choices=BUGSTATUS)
    bug_title = models.CharField(max_length=800,blank=True, null=True)
    assgined_to = models.ForeignKey(User,verbose_name = 'User Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    dev_status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    testing_status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    priority = models.CharField(max_length=10, blank=True, null=True, choices=PRIORITY)
    end_date = models.DateField(default=datetime.date.today)
    bug_level = models.CharField(max_length=10, blank=True, null=True, choices=LEVELSTATUS)
    comment= models.CharField(max_length=100 ,blank=True, null=True)

RESULT = (
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('Retested', 'Retested'),
        ('NotRetested', 'NotRetested'),
    )


class TestCaseSteps(models.Model):
    test_case_name = models.CharField(max_length=80,blank=True, null=True)

    comment= models.CharField(max_length=100 ,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.test_case_name)


class Steps(models.Model):
    test_case_step_obj = models.ForeignKey(TestCaseSteps,verbose_name = 'TestCaseSteps',default='', blank=True, null=True, on_delete=models.CASCADE)
    step_count = models.CharField(max_length=80,blank=True, null=True)
    description = models.CharField(max_length=800,blank=True, null=True)
    action = models.CharField(max_length=800,blank=True, null=True)
    expected_result = models.CharField(max_length=800,blank=True, null=True)
    actual_result = models.CharField(max_length=800,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.step_count)





class TestCase(models.Model):
    bug_obj = models.ForeignKey(Bug,verbose_name = 'Bug Name',default='', blank=True, null=True, on_delete=models.CASCADE)

    rel_det_obj = models.ForeignKey(ReleaseDetails,verbose_name = 'Release',default='', blank=True, null=True, on_delete=models.CASCADE)
    test_case_obj = models.ForeignKey(TestCaseSteps,verbose_name='TestCase ID',default='', blank=True, null=True, on_delete=models.CASCADE)

    test_result = models.CharField(max_length=80,blank=True, null=True,choices=RESULT)

    comment= models.CharField(max_length=100 ,blank=True, null=True)







