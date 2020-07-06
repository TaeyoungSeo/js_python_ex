
# num11 = 20
# num2 = 5

# str1 = "종석"
# str2 = "바보"

# print("===================")
# print("num1 : " + str(num1))
# print("result : {}, {}".format(num1, num2))
# print(str1 + str2)
# print("{}:{}".format(str1, str2))

# if(True):
#     num11 = 10
#     print(num11)
# print(num11)

# arr = [90, 25, 67, 45, 80]

# for item in arr:
#     print("result : " + str(item))

# print("===================")

# arr2 = [0,1,2,3,4]
# # for i in arr2:
# #     print(arr[i])

# for i in range(len(arr)):
#     print("{}번째 result : {}".format(i+1, arr[i]))

# if False :
#     print("true")
# elif(True) :
#     print("else if")
# else:
#     print("else")
#     print("else")

import my_lib
import json

def show_log(obj_to_print):
    print("LOG : " + str(obj_to_print))

def main(name, year, month, day, gender):
    obj = my_lib.get_person_info(name, year, month, day, gender)
    print(json.dumps(obj, ensure_ascii=False))

main("종석", 1982, 4, 13, 0)