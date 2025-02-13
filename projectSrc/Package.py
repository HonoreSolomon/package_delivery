from datetime import time, datetime, timedelta

#used to store information about the package
class Package:
    def __init__(self, package_id, address, city, state, zip, Deadline_time, weight, notes, status="At Hub"):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.Deadline_time = self._parse_deadline(Deadline_time)
        self.weight = weight
        self.status = status
        self.notes = notes
        self.departure_time = None
        self.delivery_time = None
        self.truck = "Not Loaded Yet"

    def __str__(self):
        return "ID: %s, %s, %s, %s,  %s, Deadline: %s,  %s, Delivery: %s, Status: %s, Departure: %s" % (self.package_id, self.address, self.city, self.state, self.zip,
                                                       self.Deadline_time, self.weight, self.delivery_time ,self.status,self.departure_time)

    def update_status(self, chosen_time):
        if self.delivery_time < chosen_time:
            self.status = "Delivered"
        elif self.departure_time > chosen_time:
            self.status = "En Route"
        else:
            self.status = "At Hub"
        if self.package_id == 9:
            if chosen_time > timedelta(hours=10, minutes=20):
                self.address = '410 S State St'
                self.zip = "84111"
            else:
                self.address = "300 State St"
                self.zip = "84103"

    def _parse_deadline(self, deadline_str):
        """Convert deadline string to datetime.time object"""
        if deadline_str.lower() == 'eod':
            return time(17, 0)  # 5:00 PM
        try:
            return datetime.strptime(deadline_str, "%I:%M %p").time()
        except ValueError:
            return datetime.strptime(deadline_str, "%H:%M:%S").time()