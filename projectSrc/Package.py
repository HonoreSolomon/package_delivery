class Package:
    def __init__(self, package_id, address, city, state, zip, Deadline_time, weight, notes, status="At Hub"):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.status = status
        self.notes = notes
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state, self.zip,
                                                       self.Deadline_time, self.weight, self.delivery_time ,self.status,)


    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:

            self.status = "Delivered"
        elif self.departure_time > convert_timedelta:
            self.status = "In Departure"
        else:
            self.status = "At Hub"


