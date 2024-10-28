class Solution(object):
    def carFleet(self, target, position, speed):
        cars = zip(position, speed)
        sorted_cars = sorted(cars, key=lambda car: car[0], reverse=True)    
        fleet_count = 0
        latest_fleet_time = 0

        for pos,spd in sorted_cars:
            time_to_reach_target = float(target - pos) / spd
            if time_to_reach_target > latest_fleet_time :
                fleet_count += 1
                latest_fleet_time = time_to_reach_target
        return fleet_count