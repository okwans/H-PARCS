# -*- coding:utf-8 -*-
import datetime
import time
from behave import *
import requests
import json

def before_all(context):
    now = datetime.datetime.now()
    test_date = now.strftime('%Y/%m/%d - %H:%M:%S')
    print('== H-PARCS API Test(staging) ======================================================================')
    print("== " + test_date + "    ======================================================================")
    print("==================================================================================================")
    print(" ")

def after_all(context):
    #print('===== After ALL =====')
    print('H-PARCS_API_Test_END')
    #print('===========================================================================================================')

#def before_feature(context, feature):
#    if 'W4.10_설정' in str(feature):
#        print('====Before Feature====' + str(feature))
#        print('App Login 내용이 들어가야 함')

"""
def before_all(context):
    print('===== Before ALL =====')

def after_all(context):
    print('===== After ALL =====')


def before_feature(context, feature):
    if '카플랫-RAiDEA 기업구독 신청 확인' in str(feature):
        print ('====Before Feature====' + str(feature))

def after_feature(context, feature):
    if 'Decorators feature 2' in str(feature):
        print ('====After Feature====' + str(feature))


def before_scenario(context, scenario):
    if 'Decorators check case 4' in str(scenario):
        print ('===Before Scenario===' + str(scenario))


def after_scenario(context, scenario):
    if 'Decorators check case 4' in str(scenario):
        print ('===After Scenario===' + str(scenario))


def before_step(context, step):
    if 'I start decorators check case 2' in str(step):
        print ('==Before Step==' + str(step))


def after_step(context, step):
    if 'I start decorators check case 2' in str(step):
        print ('==After Step==' + str(step))


def before_tag(context, tag):
    if 'tag1' in str(tag):
        print ('=Before Tag=' + str(tag))


def after_tag(context, tag):
    if 'tag1' in str(tag):
        print ('=After Tag=' + str(tag))
"""