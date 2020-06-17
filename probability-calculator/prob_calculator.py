import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwarg):
        contents = []
        for key in kwarg.keys():
            for n in range(kwarg[key]):
                contents.append(key)

        self.contents = contents

    def draw(self, number):
        contents = self.contents
        if number >= len(contents):
            return contents

        hat = []

        for n in range(number):
            len_contents = len(contents)
            index = random.randrange(len_contents)
            ball = contents[index]
            hat.append(ball)
            contents = contents[0:index] + contents[index + 1:]

        return hat


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for n in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        sample = hat_copy.draw(num_balls_drawn)
        success = True
        for key in expected_balls.keys():
            if sample.count(key) < expected_balls[key]:
                success = False
                break
        if success:
            count += 1

    return count / num_experiments
