from quicktimer import Timer

class Probe:

    def __init__(self, vel_x, vel_y, range_x, range_y):

        self.x = 0
        self.y = 0
        self.velocity_x = vel_x
        self.velocity_y = vel_y

        self.target_range_x = range_x
        self.target_range_y = range_y
        self.max_y = -1000000

    def step(self):

        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_y -= 1  # Gravity on the y-axis

        # Drag on the x-axis.
        if self.velocity_x > 0:
            self.velocity_x -= 1
        elif self.velocity_x < 0:
            self.velocity_x += 1
        else:
            pass  # no change if it's at zero.

        self.max_y = self.y if self.y > self.max_y else self.max_y  # Update max_y

        # print(f"Position {self.x},{self.y}")
        return self.check_target()

    def check_target(self):
        if self.x in self.target_range_x and self.y in self.target_range_y:
            return "On target."
        elif self.x > max(self.target_range_x):
            return "Overshot X"
        elif self.y < min(self.target_range_y):
            return "Overshot Y"
        else:
            # print("Still travelling...")
            return None


T = Timer()
T.take_time()

successful_pairs = []
targetx1 = 111
targetx2 = 161
targety1 = -154
targety2 = -101

# brute-force approach within possible limits.
# Range of velocity-X: cannot shoot backwards, maximum forward-velocity is the max value in the x-target-range.
# Range of velocity-Y: can shoot downwards to minimum of y-target-range (otherwise overshot instantly) and
# maximum upwards of
for velx in range(0, targetx2+1):
    for vely in range(targety1, abs(targety1)):
        p = Probe(velx, vely, list(range(targetx1, targetx2+1)), list(range(targety1, targety2+1)))

        while True:
            res = p.step()

            if res == "On target.":
                successful_pairs.append((velx, vely))
                break
            elif res is None:
                continue
            else:  # Overshot an axis.
                break


print(f"TASK2 solution: Number of successful pairs: {len(successful_pairs)}")

# get pair with max y-velocity and run the probe again.
t = max(successful_pairs, key=lambda x:x[1])
p = Probe(t[0], t[1], list(range(targetx1, targetx2)), list(range(targety1, targety2)))
while True:
    res = p.step()
    if res == "On target.":
        print(f"TASK1 solution pair: On target with values {t[0]} and {t[1]}.")
        print(f"TASK1 solution max_y: Max value on y-axi is {p.max_y} ")
        break

T.take_time()
T.fancy_print()