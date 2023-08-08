# Exploring Success Rates for Renting the Best Flat - README

## Introduction
This code is part of a YouTube video exploring the 37% algorithm by assessing the success rates for renting the best flat given a certain exploration phase cut-off percentage. The video: [The 37% Algorithm: Cracking Tokyo's Flat-Hunt Code](https://youtu.be/rhCNlTL71yo)



## Requirements
To run this code, you need to have Python 3 installed along with the following libraries:
- random
- matplotlib
- numpy

## How to Use
1. Clone or download this repository to your local machine.
2. Make sure you have the required libraries installed.
3. Open a terminal or command prompt and navigate to the directory containing the code.
4. Open the script file `the_37_algorithm.py` in a text editor of your choice.
5. Modify the following variables in the script to match your preferences:
   - `number_of_flats`: The number of flats in the simulation.
   - `min_cut_off`: The minimum exploration phase cut-off percentage.
   - `max_cut_off`: The maximum exploration phase cut-off percentage.
   - `number_of_iterations`: The number of simulations to run.
6. Save the changes to the script.
7. Run the script by executing the following command: `python the_37_algorithm.py`.

## Code Explanation
The script consists of two main functions:

### 1. `evaluate_success_rate(cut_off, num_flats, num_simulations)`
This function simulates the hiring process with customizable parameters:

- `cut_off`: The exploration phase cut-off percentage.
- `num_flats`: The number of flats in the simulation.
- `num_simulations`: The number of simulations to run.

### 2. `plot_distribution(data)`
This function plots the distribution of success rates for different exploration phase cut-off percentages.

- `data`: A list of lists containing exploration phase cut-off percentages and their corresponding success rates.



## YouTube Video
Please find the YouTube video related to this code at the following link: [The 37% Algorithm: Cracking Tokyo's Flat-Hunt Code](https://youtu.be/rhCNlTL71yo)

## License
This code is released under the [MIT License](LICENSE). Feel free to use and modify it as needed.

## Author
This code was created by Mohammed Habboub. 

