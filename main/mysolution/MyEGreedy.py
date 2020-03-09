import random
import numpy as np

class MyEGreedy:

    def __init__(self):
        print("Made EGreedy")

    def get_random_action(self, agent, maze):
        """Selects a random action."""
        possible_actions = maze.get_valid_actions(agent)
        random_int = np.random.randint(len(possible_actions))
        #print("chose random action", possible_actions[random_int])
        return possible_actions[random_int]

    def get_best_action(self, agent, maze, q_learning):
        """Select the best action based on QLearning."""
        possible_actions = maze.get_valid_actions(agent)
        action_values = q_learning.get_action_values(agent.get_state(maze), possible_actions)
        best_index = 0
        best_act_val = 0
        best_indexes_arr = []
        for i in range(len(action_values)):
            if(action_values[i] > best_act_val):
                best_indexes_arr = []
                best_act_val = action_values[i]
                best_indexes_arr.append(i)
            elif(action_values[i] == best_act_val):
                best_indexes_arr.append(i)
        random_best_action = np.random.randint(len(best_indexes_arr))
        #print("chose best action;", possible_actions[best_indexes_arr[random_best_action]])
        return possible_actions[best_indexes_arr[random_best_action]]

    def get_egreedy_action(self, agent, maze, q_learning, epsilon):
        """Selects the best action with probability epsilon or a random action with probability (1 - epsilon)."""
        rand = random.uniform(0, 1)

        if (rand < epsilon):
            action = self.get_random_action(agent, maze)
        else:
            action = self.get_best_action(agent, maze, q_learning)
        return action
