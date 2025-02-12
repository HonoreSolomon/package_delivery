
class DeliveryStatus:
    def __init__(self):
        self.map = {}

    def add_current_statuses(self, package_table, delivery_time):
            inner_dict = {}
            for i in range(1, package_table.count + 1):
                package = package_table.get(i)
                inner_dict[package.package_id] = package.status
            self.map[delivery_time] = inner_dict
    def get_time_stamp(self, chosen_time):
        for time in self.map.keys():
            if time <= chosen_time:
                time_stamp_dict = self.map[time]
                time_stamp = time
        return time_stamp_dict, time_stamp
    def __str__(self):
        return str(self.map)
