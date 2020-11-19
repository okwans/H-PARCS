import os

class UrlConfig():
    RUN_TIME_ENV = os.environ.get("RUN_TIME_ENV", None)
    print("RUN_TIME_ENV = %s" % RUN_TIME_ENV)

    # Test에 필요한 환경
    Test_ENV = "stg"
    Test_ID = "humax"
    Test_PW = "humax@!"

    Test_API_URL = "http://localhost:3000/api"  # HPARCS API URL

urlconfig = UrlConfig()