import json
import js_naming

# 추천 이름 api
# 파라미터
# name : 이름
# year, month, day : 생년월일
def get_name_recommand(name, year, month, day, hour, minute, gender):
    pass


# 이름 분석 api
def get_name_analysis(name):
    print(json.dumps(name, ensure_ascii=False))


get_name_analysis("종석")