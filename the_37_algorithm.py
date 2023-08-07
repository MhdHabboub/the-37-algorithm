import random

import matplotlib.pyplot as plt
import numpy as np


def evaluate_success_rate(cut_off,num_flats, num_simulations):
    success_count = 0

    for _ in range(num_simulations):
        flats = list(range(1, num_flats + 1))
        random.shuffle(flats)

        best_flat_ever = min(flats)
        best_flat_index_ever = flats.index(best_flat_ever)

        cutoff = int(np.ceil ((cut_off / 100) * num_flats))

        best_flat = min(flats[:cutoff])
        rented_flat_index = len(flats) - 1

        for i, flat in enumerate(flats[cutoff:], cutoff):
            if flat < best_flat:
                rented_flat_index = i
                break

        if rented_flat_index == best_flat_index_ever:
            success_count += 1

    success_rate = (success_count / num_simulations)*100
    return success_rate

def plot_distribution(data):
    populations = [inner_list[0] for inner_list in data]
    success_rates = [inner_list[1] for inner_list in data]

    max_success_rate = max(success_rates)
    max_success_rate_index = success_rates.index(max_success_rate)
    max_success_rate_cutoff = populations[max_success_rate_index]

    plt.scatter(populations, success_rates)
    
    plt.legend()
    plt.xlabel('Exploration Phase Cut Off %')
    plt.ylabel('Success Rate %')
    plt.title('Distribution of Success Rates')
    plt.grid(True)
    plt.show()
 

if __name__ == "__main__":    
    
    number_of_flats = 3
    min_cut_off = 1
    max_cut_off = 100
    number_of_iterations= 10000

    cutoff_success_list = [] 
    for cut_off in range(min_cut_off, max_cut_off, 1):
        print(cut_off)
        success_rate = evaluate_success_rate(cut_off,number_of_flats, number_of_iterations)
        cutoff_success_list.append([cut_off, success_rate])

    plot_distribution(cutoff_success_list)