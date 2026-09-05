class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1: return 1
        pos_speed = zip(position,speed)
        ordered_pos_speed = sorted(pos_speed, key=lambda tup: tup[0], reverse=True)
        car_fleets = 0
        max_speed = 0
        for p,s in ordered_pos_speed:
            unobstructed_time = (target-p)/s
            
            # fleet_max_time = max(fleet_max_time, unobstructed_time)
            if unobstructed_time > max_speed:
                car_fleets += 1
                max_speed = unobstructed_time
            

        return car_fleets



