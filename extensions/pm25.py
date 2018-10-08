import requests

def get_pm25():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }

    # req = requests.get("http://datacenter.mep.gov.cn/websjzx/ajaxApi/index/getAqiInfo.vm?regionCode=330100",
    #                    headers=headers)
    #
    # pm25 = req.json()["data"]["AQI"]
    return 1
