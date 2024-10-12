import requests

# Function to fetch the count of active army personnel
def fetch_army_count():
    url = "https://api.example.com/military/sri-lanka/army"  # Replace with actual API endpoint
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['active']
    else:
        print("Error fetching army count")
        return None

# Function to fetch the count of active navy personnel
def fetch_navy_count():
    url = "https://api.example.com/military/sri-lanka/navy"  # Replace with actual API endpoint
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['active']
    else:
        print("Error fetching navy count")
        return None

# Function to fetch the count of active air force personnel
def fetch_air_force_count():
    url = "https://api.example.com/military/sri-lanka/air-force"  # Replace with actual API endpoint
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['active']
    else:
        print("Error fetching air force count")
        return None

# Function to analyze the total count of active forces
def analyze_forces():
    army_count = fetch_army_count()
    navy_count = fetch_navy_count()
    air_force_count = fetch_air_force_count()

    if army_count is not None and navy_count is not None and air_force_count is not None:
        total_active_forces = army_count + navy_count + air_force_count
        print(f"Active Army Personnel: {army_count}")
        print(f"Active Navy Personnel: {navy_count}")
        print(f"Active Air Force Personnel: {air_force_count}")
        print(f"Total Active Forces Count in Sri Lanka: {total_active_forces}")
    else:
        print("Could not calculate total active forces due to data fetching errors.")

# Main function to run the analysis
def main():
    analyze_forces()

# Run the program
if __name__ == "__main__":
    main()
