# Function to calculate the probability of HIV infection
def calculate_hiv_probability(population, hiv_cases):
    # Probability is calculated as the ratio of HIV cases to total population
    probability = hiv_cases / population
    return probability

# Main function
def main():
    # Input the population and number of HIV cases
    population = int(input("Enter the population of Sri Lanka: "))
    hiv_cases = int(input("Enter the number of HIV cases: "))

    # Calculate the probability
    probability = calculate_hiv_probability(population, hiv_cases)

    # Print the probability in percentage
    print(f"The estimated probability of HIV infection is: {probability * 100:.6f}%")

# Run the program
if __name__ == "__main__":
    main()
