from main.QLearning import QLearning


class MyQLearning(QLearning):

    def update_q(self, state, action, r, state_next, possible_actions, alfa, gamma):
        # TODO Auto-generated method stub

        best_action_q = self.get_q(state_next, possible_actions[0])

        for i in possible_actions:
            if(best_action_q < self.get_q(state_next, i)):
                best_action_q = self.get_q(state_next, i)

        new_q = self.get_q(state, action) + alfa*(r + (gamma*best_action_q) - self.get_q(state, action))

        #print(new_q)
        return new_q

