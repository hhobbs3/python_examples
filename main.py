import os
import pymongo_helper_functions as pymongo

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

if __name__ == '__main__':
    for x in range(100):
        str_fizz_buzz = ""
        if x % 3 == 0:
            str_fizz_buzz = "Fizz"
        if x % 5 == 0:
            str_fizz_buzz = str_fizz_buzz + "Buzz"
        if str_fizz_buzz != "":
            print(str_fizz_buzz)
        else:
            print(x)

    p1 = Person("John", 36)
    p1.myfunc()

    car_collection_name = "cars";
    car = {"brand": "Honda",  "model": "Civic",  "year": 1994}

    # car_id = pymongo.insert(car, car_collection_name)
    # print(car_id)
    car_list = pymongo.query_all(car_collection_name)
    print(car_list)

    car_found = pymongo.find({"brand": "Honda"}, car_collection_name)
    for car in car_found:
        print(car.get('brand'))

    print(pymongo.get_all_collections())


