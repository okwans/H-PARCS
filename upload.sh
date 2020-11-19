#!/bin/bash

timestamp=`date +%Y%m%d_%H%M`
sudo mkdir ~/work/dockers/apache/apiTest_"$timestamp"/
sudo mv result/*.html ~/work/dockers/apache/apiTest_"$timestamp"/
sudo mv result/report.txt ~/work/dockers/apache/apiTest_"$timestamp"/

# slack_alarm_bdd
TEST_CATEGORY="API_Test"
Test_URL='apiTest_'$timestamp'/'
TEST_CATEGORY=${TEST_CATEGORY}
TEST_URL=${Test_URL}

#CIRCLE_BUILD_NUM=${CIRCLE_BUILD_NUM}
#bash slack_alarm_bdd.sh ${TEST_CATEGORY} ${CIRCLE_BUILD_NUM}
bash slack_alarm_bdd.sh ${TEST_CATEGORY} ${TEST_URL}
sudo rm result/testResult.txt
