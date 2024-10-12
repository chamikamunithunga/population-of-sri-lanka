import requests

# Function to fetch population data from the API
def fetch_population():
    url = "https://api.example.com/population/sri-lanka"  # Replace with actual API endpoint
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['population']
    else:
        print("Error fetching population data")
        return None

# Function to fetch HIV cases data from the API
def fetch_hiv_cases():
    url = "https://api.example.com/hiv/cases/sri-lanka"  # Replace with actual API endpoint
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['hiv_cases']
    else:
        print("Error fetching HIV cases data")
        return None

# Function to calculate the probability of HIV infection
def calculate_hiv_probability(population, hiv_cases):
    if population > 0:
        probability = hiv_cases / population
        return probability
    return 0

# Main function
def main():
    population = fetch_population()
    hiv_cases = fetch_hiv_cases()

    if population is not None and hiv_cases is not None:
        # Calculate the probability
        probability = calculate_hiv_probability(population, hiv_cases)

        # Print the probability in percentage
        print(f"The estimated probability of HIV infection in Sri Lanka is: {probability * 100:.6f}%")
    else:
        print("Could not calculate probability due to data fetching errors.")

# Run the program
if __name__ == "__main__":
    main()
