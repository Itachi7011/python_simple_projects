import random

import matplotlib.pyplot as plt


class MarkovChain:

    def __init__(self, transition_probabilities):

        self.transition_probabilities = transition_probabilities

        self.states = list(transition_probabilities.keys())


    def next_state(self, current_state):

        probabilities = self.transition_probabilities[current_state]

        r = random.random()

        cumulative_probability = 0.0

        for next_state, probability in probabilities.items():

            cumulative_probability += probability

            if r < cumulative_probability:

                return next_state

        return None


    def simulate(self, initial_state, num_steps):

        current_state = initial_state

        states = [current_state]

        for _ in range(num_steps):

            current_state = self.next_state(current_state)

            states.append(current_state)

        return states


    def stationary_distribution(self, num_iterations=10000):

        state_counts = {state: 0 for state in self.states}

        current_state = random.choice(self.states)

        for _ in range(num_iterations):

            current_state = self.next_state(current_state)

            state_counts[current_state] += 1

        stationary_distribution = {state: count / num_iterations for state, count in state_counts.items()}

        return stationary_distribution


    def plot_stationary_distribution(self, stationary_distribution):

        plt.bar(stationary_distribution.keys(), stationary_distribution.values())

        plt.xlabel("State")

        plt.ylabel("Stationary Probability")

        plt.title("Stationary Distribution")

        plt.show()


    def plot_simulation(self, states):

        plt.plot(states)

        plt.xlabel("Step")

        plt.ylabel("State")

        plt.title("Markov Chain Simulation")

        plt.show()


# Example usage:

transition_probabilities = {

    'A': {'A': 0.5, 'B': 0.3, 'C': 0.2},

    'B': {'A': 0.4, 'B': 0.3, 'C': 0.3},

    'C': {'A': 0.2, 'B': 0.5, 'C': 0.3}

}


markov_chain = MarkovChain(transition_probabilities)

initial_state = 'A'

num_steps = 100

states = markov_chain.simulate(initial_state, num_steps)


print("Markov chain simulation:")

print(" -> ".join(states))


stationary_distribution = markov_chain.stationary_distribution()

print("Stationary distribution:")

print(stationary_distribution)


markov_chain.plot_simulation(states)

markov_chain.plot_stationary_distribution(stationary_distribution)