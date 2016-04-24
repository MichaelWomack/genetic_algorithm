import random

class Population(object):
    """ class to create a population and reproduce and mutate it """

    def __init__(self, population_size, max_generations, p_mutation):
        self.population = self.init_population(population_size)
        self.fitnesses = []
        self.max_generations = max_generations
        self.p_mutation = p_mutation
        self.global_optimum = (0, 0, 0) # individual, fitness, generation

    def init_population(self, size):
        bits = ['0', '1']
        population = []

        for i in range(size):
            bit_str = ''
            for bit_index in range(3):
                bit_str = random.choice(bits) + bit_str
            population.append('00' + bit_str)

        return population

    def reproduce(self, parent1, parent2):
        crossover = random.randint(0, len(parent1) - 1)
        child1 = parent1[:crossover] + parent2[crossover:]
        child2 = parent2[:crossover] + parent1[crossover:]
        return [child1, child2]

    def mutate(self, individual):
        rand_index = random.randint(0, len(individual) - 1)
        split = list(individual)

        if split[rand_index] == '0':
            split[rand_index] = '1'
        else:
            split[rand_index] = '0'

        return ''.join(split)

    def to_decimal(self, bit_str):
        return int(bit_str, base=2)

    def fitness_func(self, string):
        value = self.to_decimal(string)
        return value * value

    def random_mate_select(self, population):
        parent1 = random.choice(population)
        population.remove(parent1)
        parent2 = random.choice(population)
        return [parent1, parent2]

