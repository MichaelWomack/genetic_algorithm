import random


def init_population(size):
    bits = ['0', '1']
    population = []

    for i in range(size):
        bit_str = ''
        for bit_index in range(3):
            bit_str = random.choice(bits) + bit_str
        population.append('00' + bit_str)

    return population


def reproduce(parent1, parent2):
    crossover = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover] + parent2[crossover:]
    child2 = parent2[:crossover] + parent1[crossover:]
    return [child1, child2]


def mutate(individual):
    rand_index = random.randint(0, len(individual) - 1)
    split = list(individual)

    if split[rand_index] == '0':
        split[rand_index] = '1'
    else:
        split[rand_index] = '0'

    return ''.join(split)


def get_crossover():
    return random.randint(0, 3)


def to_decimal(bit_str):
    return int(bit_str, base=2)


def fitness_func(string):
    value = to_decimal(string)
    return value / 32


def random_mate_select(population):
    parent1 = random.choice(population)
    population.remove(parent1)
    parent2 = random.choice(population)
    return [parent1, parent2]


if __name__ == "__main__":
    print(to_decimal("11111"))

    fitness_threshold = .95  # Initial Population
    max_individual = 0
    population = init_population(4)
    print(population)
    highest_fitness = 0

    while highest_fitness < fitness_threshold:
        # Fitness Function
        fitnesses = []
        for individual in population:
            fitnesses.append(fitness_func(individual))
        print(fitnesses)
        highest_fitness = max(fitnesses)
        max_individual = population[fitnesses.index(highest_fitness)]

        # Selection at random for mating
        lowest_fitness_index = fitnesses.index(min(fitnesses))
        del population[lowest_fitness_index]
        del fitnesses[lowest_fitness_index]
        print(population)

        # Crossover/Repr
        parents = random_mate_select(population)
        #print("Mates selected")
        # print("Parents \n{}".format(parents))
        children = reproduce(parents[0], parents[1])
        # print("Children \n{}".format(children))

        parents2 = random_mate_select(population)
        children = children + reproduce(parents2[0], parents2[1])

        # Mutation with small independent probability
        for child in children:
            if random.random() < .3:
                children[children.index(child)] = mutate(child)

        population = children
        print(children)

print("Highest value: {} fitness: {}".format(max_individual, highest_fitness))
