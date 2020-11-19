# -*- coding:utf-8 -*-

import sys
from behave import __main__ as Runner

if __name__ == '__main__':
    sys.stdout.flush()
    #RunnerOption = ''
    Runner.main('-k --no-capture --no-capture-stderr --tags=@api -f plain')
    # Runner.main('--no-capture --no-capture-stderr -f plain --tags=@E1.1_자원등록관리_스테이션등록')

"""
Reporting
> behave --tags=-test -f json -o reports/report.json

> behave --no-capture --no-capture-stderr --tags=-test -f json -o reports/report.json

> For additional formats see here: https://behave.readthedocs.io/en/latest/formatters.html

Install npm (nodejs) from https://www.npmjs.com/get-npm
npm install cucumber-html-reporter -g
pip install behave2cucumber
# cucumber report merge
npm install -g cucumber-json-merge
cucumber-json-merge [option] <report1.json> <report2.json> ...


> python2 -m behave2cucumber -i reports/report.json -o reports/cucumber.json -f
> cp html_reporter.js reports/
> node reports/html_reporter.js
"""
