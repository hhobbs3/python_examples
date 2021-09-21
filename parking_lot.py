# Design a parking lot using object-oriented principles
#
# Goals:
# - Your solution should be in Java - if you would like to use another language, please let the interviewer know.
# - Boilerplate is provided. Feel free to change the code as you see fit
#
# Assumptions:
# - The parking lot can hold motorcycles, cars and vans
# - The parking lot has motorcycle spots, car spots and large spots
# - A motorcycle can park in any spot
# - A car can park in a single compact spot, or a regular spot
# - A van can park, but it will take up 3 regular spots
# - These are just a few assumptions. Feel free to ask your interviewer about more assumptions as needed
#
# Here are a few methods that you should be able to run:
# - Tell us how many spots are remaining
# - Tell us how many total spots are in the parking lot
# - Tell us when the parking lot is full
# - Tell us when the parking lot is empty
# - Tell us when certain spots are full e.g. when all motorcycle spots are taken
# - Tell us how many spots vans are taking up

import numpy as np
import uuid
import json

# I recognize this is irregular to have in the global scope. It seemed better than repetition
# in each factory method.
def validate_parking_args(args, num_expected_args):
    len_of_each_arg = len(args[0])
    assert len_of_each_arg == num_expected_args
    for arg in args:
        assert len(arg) == len_of_each_arg
        assert isinstance(arg[0], str)
        for num in arg[1:]:
            assert isinstance(num, int)


small = 'small_parking'
compact = 'compact_parking'
regular = 'regular_parking'


class ParkingLot:
    def __init__(self, parking):
        self.parking = parking

    # allows multiple constructors in case they are needed in the future
    # this format of definition means that we can have unlimited types of parking by simply adding to the tuple that is passed to constructor.
    @classmethod
    def init_parking_types_total(cls, args, vehicles):
        """
        Allows multiple constructors in case they are needed in the future.
        This format of definition means that we can have unlimited types of parking by simply adding to the tuple that
        is passed to constructor.

        :param args: list of tuples that represent the size [0] and number [1] of parking slots
        :param vehicles: list of valid vehicle types that can be hosted
        :return: returns dic containing the overview of the parking lot
        """
        validate_parking_args(args, 2)
        parking_spots = {}
        vehicle_totals = {}
        for arg in args:
            parking_spots[arg[0]] = {'total': arg[1], 'used': 0}
        for vehicle in vehicles:
            vehicle_totals[vehicle.name] = 0

        parking = {'parking_spots': parking_spots,
                   'vehicle_totals': vehicle_totals,
                   'vehicle_list': {}}
        p = cls(parking)
        return p

    def init_parking_from_json(cls, parking_json):
        p = cls(json.loads(parking_json))
        return p

    def get_parking_json(self):
        """
        :return: parking in json format
        """
        return json.dumps(self.parking)

    def get_remaining_parking_available(self):
        """
        :return: dic of remaining parking available categorized by size

        """
        remaining_parking = {}
        for key in self.parking['parking_spots'].keys():
            remaining_parking[key] = self.parking['parking_spots'][key]['total'] - self.parking['parking_spots'][key][
                'used']
        return remaining_parking

        # return total parking for all types of parking

    def get_total_parking_available(self):
        """
        :return: dic of total parking categorized by size

        """
        total_parking = {}
        for key in self.parking['parking_spots'].keys():
            total_parking[key] = self.parking['parking_spots'][key]['total']
        return total_parking

    # add a vehicle to the lot, track it via its ticket_id, substract appropriately from lot with assumption that ticket will assign most
    # efficent parking
    def add_vehicle_to_lot(self, vehicle):
        """
        Inserts vehicle into parking lot if there is space

        :param vehicle: a vehicle class
        :return: either the ticket_id that was created upon parking purchase or a message that there is no space
        """
        ticket_id = str(uuid.uuid4())
        for key in vehicle.parking_required:
            if key in self.parking['parking_spots']:
                if self.parking['parking_spots'][key]['total'] >= self.parking['parking_spots'][key]['used'] + \
                        vehicle.parking_required[key]:
                    self.parking['parking_spots'][key]['used'] = self.parking['parking_spots'][key]['used'] + \
                                                                 vehicle.parking_required[key]
                    self.parking['vehicle_totals'][vehicle.name] = self.parking['vehicle_totals'][vehicle.name] + 1
                    self.parking['vehicle_list'][ticket_id] = (vehicle.name, key, vehicle.parking_required[key])

                    # self.parking['vehicle_list'].append({ticket_id: (vehicle.name, key, vehicle.parking_required[key])})
                    return ticket_id
        return 'no space, turn vehicle away'

    # based on ticket leaving lot, remove the vehicle from the vehicle_list and update total vehicle and available space.
    def remove_vehicle_from_lot(self, ticket_id):
        """
        Removes a vehicle from the parking lot based on the ticket received upon exit.

        :param ticket_id: str containing ticket associated with vehicle
        :return: str containing message that vehicle left or that the ticket was invalid
        """
        if ticket_id in self.parking['vehicle_list']:
            print('found ticket')
            vehicle_type = self.parking['vehicle_list'][ticket_id][0]
            slot_type = self.parking['vehicle_list'][ticket_id][1]
            num_slots = self.parking['vehicle_list'][ticket_id][2]

            self.parking['parking_spots'][slot_type]['used'] = self.parking['parking_spots'][slot_type][
                                                                   'used'] - num_slots
            self.parking['vehicle_totals'][vehicle_type] = self.parking['vehicle_totals'][vehicle_type] - 1
            del self.parking['vehicle_list'][ticket_id]
            return "vehicle successfully left parking lot"
        else:
            return "invalid ticket"


# base class. Currently has no common content across its children but it is added in anticipation for possible future uses.
class Vehicle:
    def __init__(self):
        pass


class Van(Vehicle):
    def __init__(self):
        self.name = 'van'
        self.parking_required = {regular: 3}


class Car(Vehicle):
    def __init__(self):
        self.name = 'car'
        self.parking_required = {compact: 1,
                                 regular: 1}


class Motorcycle(Vehicle):
    def __init__(self):
        self.name = 'motorcycle'
        self.parking_required = {small: 1,
                                 compact: 1,
                                 regular: 1}


# Unit test using pytest. I can't execute properly with pytest command so I will just call it.
# It would also typically be stored separately


if __name__ == '__main__':
    parking_def1 = [(small, 10), (compact, 30), (regular, 40)]
    list_of_vehicles_admitted1 = [Motorcycle(), Car(), Van()]
    tickets = []

    for vehicle in list_of_vehicles_admitted1:
        print(vehicle.name)
        print(vehicle.parking_required)

    parking1 = ParkingLot.init_parking_types_total(parking_def1, list_of_vehicles_admitted1)
    print(parking1.parking)

    print(parking1.get_remaining_parking_available())
    print(parking1.get_total_parking_available())

    for i in range(20):
        tickets.append(parking1.add_vehicle_to_lot(Van()))
        print(tickets[-1:])

    for i in range(40):
        tickets.append(parking1.add_vehicle_to_lot(Car()))
        print(tickets[-1:])

    print(parking1.parking)
    parking1.remove_vehicle_from_lot(tickets[3])

    print(parking1.parking)
