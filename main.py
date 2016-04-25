from population import Population
import random


def continue_run():
    try:
        num_gens = int(input("How many more generations would you like to run? (0 to stop)\n"))
        return num_gens
    except Exception:
        print('invalid input')
        return continue_run()


if __name__ == "__main__":

    population_size = 4
    num_generations = 6
    p_mutation = .2
    ga = Population(population_size, num_generations, p_mutation)

    current_generation = 0
    while current_generation < ga.max_generations:
        # Fitness Function

        for individual in ga.population:
            fitness = ga.fitness_func(individual)
            ga.fitnesses.append(fitness)

        highest_fitness = max(ga.fitnesses)
        max_individual = ga.population[ga.fitnesses.index(highest_fitness)]

        if highest_fitness > ga.global_optimum[1]:
            ga.global_optimum = (max_individual, highest_fitness, current_generation)

        avg = sum(ga.fitnesses) / len(ga.fitnesses)

        print("Gen: {}\tPopulation: {}\tFitnesses: {}\tAverage Fitness: {}"
              .format(current_generation, ga.population, ga.fitnesses, avg))

        # Selection at random for mating
        lowest_fitness_index = ga.fitnesses.index(min(ga.fitnesses))
        del ga.population[lowest_fitness_index]
        del ga.fitnesses[lowest_fitness_index]

        # Crossover/Repr
        parents = ga.random_mate_select(ga.population)
        children = ga.reproduce(parents[0], parents[1])

        parents2 = ga.random_mate_select(ga.population)
        children = children + ga.reproduce(parents2[0], parents2[1])

        # Mutation with small independent probability
        for child in children:
            if random.random() < ga.p_mutation:
                children[children.index(child)] = ga.mutate(child)

        ga.population = children
        ga.fitnesses.clear()
        current_generation += 1

        if current_generation == ga.max_generations:
            print("\nGlobal Optimum: ")
            print("Individual: {}\tFitness: {}\tGeneration: {}\n"
                .format(ga.global_optimum[0], ga.global_optimum[1], ga.global_optimum[2]))

            num_gens = input("How many more generations would you like to run? (0 to stop)\n")
            ga.max_generations += int(num_gens)