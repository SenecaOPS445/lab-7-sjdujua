#!/usr/bin/env python3
# Student ID: [sjdujua]
class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times, valid_time
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''Return a string representation for the object self'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''return a string representation for the object self'''
        '''just instead of ':', you are required use the '.'  in the formatting string.'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
   
    def format_time(self):
        """Return time object (self) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
    def sum_times(self, t2):
        """Add two time objests and return the sum."""
        """Change this to become object method for our Time object (refer to lab7c.py and change_time() method below)"""
        sum = Time(0, 0, 0)
        sum.hour = self.hour + t2.hour
        sum.minute = self.minute + t2.minute
        sum.second = self.second + t2.second

        # Fix the carry over for seconds and minutes
        while sum.second >= 60:
            sum.second -= 60
            sum.minute += 1
        
        while sum.minute >= 60:
            sum.minute -= 60
            sum.hour += 1

        return sum

    def change_time(self, seconds):
        """Modify the time object by adding seconds."""
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second 
        return None

    def time_to_sec(self):
        '''convert a time object to a single integer representing the number of seconds from midnight'''
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check for the validity of the time object attributes:
        24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
