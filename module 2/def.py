# def sum(num1, num2):
#     result = num1 + num2
#     return result


# total = sum(99, 11)
# print('total :', total)

# def display_person(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# display_person(Name="Amir Khan", Age="45")

# numbers = [9, 15, 2, 36]
# numbers[1:4] = [20, 14, 36]
# print(numbers)
# person_info = {"name": "Sakib", "salary": 80000}
# value = person_info.get("salary")
# print(value)
# student = {
#     "name": "Amir",
#     "class": 10,
#     "marks": 85
# }
# student.pop("marks")


try:
    result = 20//5
except:
    print("error happened")
finally:
    print("finally here")

    from math import *
result = ceil(5.00001)
print(result)


def num(a): return a*a


print(num(2**2))
