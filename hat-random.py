import copy
import random

class Hat:
    # Build the contents of the balls
    def __init__(self, **args):
        self.contents = [color for color, num in args.items() for _ in range(num)]

    # Draw the random balls to use to formulate the probability
    def draw(self, amount):
        # Return array if amount of draws is larger than the amount of balls we have
        if amount > len(self.contents):
            return [self.contents.pop(0) for i in range(len(self.contents))]
        else:
            return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(amount)]
 
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0

    # Run through the number of experiments
    for _ in range(num_experiments):
        # Keep a copy to not override the original contents
        copied_hat = copy.deepcopy(hat)
        retrievedBalls = copied_hat.draw(num_balls_drawn)
        passes = True

        # Compare expected with the balls we retrieved
        for color, amount in expected_balls.items():
            if amount > retrievedBalls.count(color):
                passes = False
                break

        # Add match amount if the expected_balls matches the random generated balls from Hat.draw()
        if passes:
            match += 1

    # Return the calculated probability based on matches to number of tries
    return match / num_experiments
