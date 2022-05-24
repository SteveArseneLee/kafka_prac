from nemo import get_nemo_api, get_submunicipality_code
from seoul_api import get_all_seoul_data
from utils import SEOUL_DATA_API_KEYS, SEOUL_MUNICIPALITY_CODE
from kafka import KafkaProducer
import json
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9091'],
                         valur_serializer=json_serializer,)

if __name__ == "__main__":
    """
    서울시 데이터
    """
    for key, data_api_key in SEOUL_DATA_API_KEYS.items():
        for year in [2018, 2019, 2020, 2021, 2022]:
            for data in get_all_seoul_data(key, data_api_key, year):
                result = {"key": key, **data}
                if "year" not in result:
                    result.update({"year": year})
                print(result)
                # 여기에 producer  연결하는 코드 작성
                producer.send("rtc", result)
                time.sleep(4)
                

    """
    네모 데이터
    """
    # for municipality_code in SEOUL_MUNICIPALITY_CODE.values():
    #     for data in get_nemo_api(municipality_code):
    #         print(data)
    #         print()