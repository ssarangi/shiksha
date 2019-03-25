from django.db import models

# Create your models here.


class Location:
    def __init__(self, zip_code=None, city=None, state=None, country=None, time_zone=None):
        self._zip_code = zip_code
        self._city = city
        self._state = state
        self._country = country
        self._time_zone = time_zone

    def get_zip_code(self):
        return self._zip_code

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_country(self):
        return self._country

    def get_time_zone(self):
        return self._time_zone

    def __str__(self):
        s = sf.same_line(self._city, self._state, self._country, ', ')
        s += sf.new_line() + sf.same_line(self._zip_code)
        s += sf.new_line() + sf.same_line(self._time_zone)
        return s


class Profile:
    def __init__(self, first_name, last_name, location):
        self._first_name = first_name
        self._last_name = last_name
        self._location = location

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_location(self):
        return self._location

    def __str__(self):
        s = sf.same_line(self._first_name, self._last_name, delimiter=', ')
        s += sf.new_line() + sf.same_line(self._location)
        return s

    __repr__ = __str__


class Student:
    def __init__(self, grade=1):
        self._grade = Grade(grade)
