from main.Maze import Maze
from main.Agent import Agent
from main.mysolution.MyQLearning import MyQLearning
from main.mysolution.MyEGreedy import MyEGreedy
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import sys


    ##################################
## README: We are passing the file name as an argument so you may need to
## put the file path of the maze in the configuration arguments.
## We also commented out the parts that were used for the plots.
## Please read our comments as well, as we still keep the values, statements and conditions to test out some of the other exercises.
## READ ABOVE READ ABOVE READ ABOVE #################

def runme(maze, robot, selection, learn):


    step_count = 0
    trials = 0
    total_steps_before_reset = 0
    each_trial = [] # stores the number of steps per each trial, used to calculate the average number of steps per trial
    epsilon = 0.1

    stop = False

    # keep learning until you decide to stop
    while not stop:


        # the robot reaches its goal, gets reseted ##
        if (robot.x == 9 and robot.y == 9) : # comment out if you wanna test toy maze
        #if robot.x == 24 and robot.y == 14: # comment out if you wanna test easy maze
            print("robot resetting, ")
            each_trial.append(total_steps_before_reset)
            total_steps_before_reset = 0
            robot.reset()
            trials = trials + 1


        # the robot still hasn't completed the stopping criterion, so continues to update Q values
        #elif trials < 50: to plot the average steps per trial
        elif step_count < 30000:
            action = selection.get_egreedy_action(robot, maze, learn, epsilon)
            state = robot.get_state(maze)
            next_state = robot.do_action(action, maze)

            new_q = learn.update_q(state, action, maze.get_reward(next_state), next_state, maze.get_valid_actions(robot), 0.7, 0.9)
            learn.set_q(state, action, new_q)

            step_count = step_count + 1
            total_steps_before_reset = total_steps_before_reset + 1
            continue

        # the robot stops once it reaches its goal
        else:
            stop = True


    sum = 0
    for x in each_trial:
        sum = sum + x

    average_steps_per_trial = sum/len(each_trial)

    return each_trial, average_steps_per_trial


if __name__ == "__main__":

    # load the maze
    file = sys.argv[1]

    maze = Maze(file)

    # Set the reward at the bottom right to 10
    maze.set_reward(maze.get_state(9, 9), 10) # comment out if you want to test toy maze
    #maze.set_reward(maze.get_state(24, 14), 10) # comment out if you want to test easy maze
    #maze.set_reward(maze.get_state(9, 0), 5) # comment out if you want to test new reward

    # create a robot at starting and reset location (0,0) (top left)
    robot = Agent(0, 0)

    # make a selection object (you need to implement the methods in this class)
    selection = MyEGreedy()

    # make a Qlearning object (you need to implement the methods in this class)
    learn = MyQLearning()

    runme(maze, robot, selection, learn)

'''''
### FOR THE PLOTS
    steps_per_trial_ = np.zeros((10, 50)) # for the plot


    for i in range(10):
        robot = Agent(0, 0) # reset the robot and Q matrix for each run
        selection = MyEGreedy()
        learn = MyQLearning()
        each_trial, average = runme(maze, robot, selection, learn)
        steps_per_trial_[i] = each_trial
        print(average)


    trial_averages = np.average(steps_per_trial_, 0)
    plt.ylabel("Average of steps taken at each trial, averaged in 10 runs")
    plt.xlabel("Trial numbers, 1st trial is the first time the robot faces the maze")
    plt.title("How the robot learns the toy maze while alfa = 0.7, epsilon = 0.1, gamma = 0.9")
    plt.plot(trial_averages)
    plt.show()
### FOR THE PLOTS
'''''



