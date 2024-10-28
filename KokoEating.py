class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        valid_eating_speed = high

        while low <= high:
            mid = (low + high) // 2
            total_hrs = 0
            # Here, calculate the total hours needed if Koko eats at speed `mid`.

            for i in piles: 
                division_score = i // mid
                division_remaining = i % mid
                total_hrs += division_score 
                if division_remaining != 0 :
                    total_hrs += 1

            # Compare it with `h` to adjust `low` and `high` accordingly.
            if total_hrs <= h:
                valid_eating_speed = mid
                high = mid - 1
            else:
                low = mid + 1
        # Return the correct `k` after exiting the loop.
        return valid_eating_speed

