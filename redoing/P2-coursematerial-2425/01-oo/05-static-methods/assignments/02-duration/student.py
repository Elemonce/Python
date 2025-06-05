# class Duration:
#     def __init__(self, seconds):
#         self.__seconds = seconds
#         self.__minutes = seconds / 60
#         self.__hours = self.__minutes / 60

#     @property
#     def seconds(self):
#         return self.__seconds
    
#     @property
#     def minutes(self):
#         return self.__minutes
    
#     @property
#     def hours(self):
#         return self.__hours
    

#     @staticmethod
#     def from_seconds(seconds):
#         return Duration(seconds)
    
#     @staticmethod
#     def from_minutes(minutes):
#         return Duration(minutes * 60)
    
#     @staticmethod
#     def from_hours(hours):
#         return Duration(hours * 3600)

class Duration:
    def __init__(self, seconds=None, minutes=None, hours=None):
        self.__seconds = 0
        
        if not seconds and not minutes and not hours:
            raise ValueError("No unit specified")
        
        if seconds:
            self.__seconds += seconds

        if minutes:
            self.__seconds += minutes * 60

        if hours:
            self.__seconds += hours * 3600
            
        self.__minutes = self.__seconds / 60
        self.__hours = self.__minutes / 60

    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def hours(self):
        return self.__hours
    
    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds=seconds)
    
    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes=minutes)
    
    @staticmethod
    def from_hours(hours):
        return Duration(hours=hours)


# duration = Duration(minutes=1)
# duration = Duration(seconds=1)
# duration = Duration(hours=1)

# duration=Duration(minutes=60)

# print(duration.hours)

# duration = Duration()


