import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        # **keyword arguments allow to work on the basis of a dictionary
        # include as many copies of the key as specified by the value
        contents = []
        for ball in balls:
            for index in range(0, balls[ball]):
                contents.append(ball)
        self.contents = contents

    def draw(self, num_balls_drawn):
        # preemptively terminate the function if the number of balls exceeds the available quantity
        # return the entire set
        contents = self.contents
        if(len(contents) <= num_balls_drawn):
            return contents

        # until balls has the input number of items, pick an item at random and add it to the list
        # ! be sure to remove it from the original array
        balls = []
        while len(balls) < num_balls_drawn:
            length = len(contents)
            index = random.randint(0, length - 1)
            content = contents[index]
            contents.remove(content)
            balls.append(content)
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # variable to compute the probability
    # each time we draw the specified balls, increment the counter
    success = 0
    for index in range(0, num_experiments):
        # create a copy of the hat object
        # this to effectively work on a different contents list
        # ! deepcopy instead of copy to consider the entire structure
        sample = copy.deepcopy(hat)
        balls = sample.draw(num_balls_drawn)
        # still need to research for..else
        # but the idea is to terminate the loop if there are no balls of the specified type
        # increment the counter otherwise
        for ball_to_draw in expected_balls:
            count = balls.count(ball_to_draw)
            if(count < expected_balls[ball_to_draw]):
                break
        else:
            success += 1
    return success / num_experiments
