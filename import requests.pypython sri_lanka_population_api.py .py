import requests

def get_population_of_sri_lanka():
    # REST Countries API URL for Sri Lanka
    url = "https://restcountries.com/v3.1/name/sri lanka"

    try:
        # Make a GET request to the API
        response = requests.get(url)

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the population
            population = data[0]['population']
            print(f"The estimated population of Sri Lanka is approximately {population:,}.")
        else:
            print(f"Error: Unable to fetch data (Status code: {response.status_code})")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
get_population_of_sri_lanka()
