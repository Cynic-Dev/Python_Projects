import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = [i for i, j in kwargs.items() for x in range(j)]

    def draw(self, n):
        if n <= len(self.contents):
            rand = []
            for i in range(n):
                rand.append(
                    self.contents.pop(random.choice(range(len(self.contents)))))
            return rand
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob = 0
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        draws = new_hat.draw(num_balls_drawn)

        ins = 0
        for i, j in expected_balls.items():
            if draws.count(i) >= j:
                ins += 1

        if ins == len(expected_balls):
            prob += 1

    return prob / num_experiments
