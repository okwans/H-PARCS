var today = new Date();

var reporter = require('cucumber-html-reporter');
var test_env = process.env['RUN_TIME_ENV'];
var build_num = process.env['CIRCLE_BUILD_NUM'];
var test_items = process.env['TEST_CATEGORY'];
var c_time = today.toLocaleString();

var options = {
        theme: 'bootstrap',
        jsonFile: 'cucumber.json',
        output: 'cucumber_HPARCS_ApiTest_report.html',
        reportSuiteAsScenarios: true,
        launchReport: false,
        metadata: {
            "BDD Script Version":"0.9.0",
            "Test Environment": test_env,
            "CircleCI Build Number": build_num,
            "Parallel": "Scenarios",
            "Executed": "Automation",
            "Test Items": test_items,
            "Report Generated Time": c_time
        }
    };

    reporter.generate(options);
