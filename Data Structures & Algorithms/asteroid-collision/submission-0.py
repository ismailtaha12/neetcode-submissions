from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while stack and stack[-1] > 0 and asteroid < 0:
                previous_size = stack[-1]
                current_size = abs(asteroid)

                if previous_size > current_size:
                    alive = False
                    break

                elif current_size > previous_size:
                    stack.pop()

                else:
                    stack.pop()
                    alive = False
                    break

            if alive:
                stack.append(asteroid)

        return stack