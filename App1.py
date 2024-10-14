# By chamikamunithunga
# munithungac@gmail.com

from flask import Flask, render_template, request

app = Flask(__name__)

# Population data based on 2023-2024 estimates
population_data = {
    "total_population": 22000000,  # Estimated total population of Sri Lanka (22 million)
    "over_18": {
        "total_population": 15200000,  # Approximate population over 18 years
        "percentage_of_population": (15200000 / 22000000) * 100  # Calculate the percentage
    },
    "below_18": {
        "total_population": 6800000,  # Approximate population below 18 years
        "percentage_of_population": (6800000 / 22000000) * 100  # Calculate the percentage
    }
}

# Function to get population data
def get_population_data(age_group):
    if age_group == "over_18":
        return population_data["over_18"]
    elif age_group == "below_18":
        return population_data["below_18"]
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/population', methods=['POST'])
def population():
    age_group = request.form['age_group']
    data = get_population_data(age_group)
    if data:
        return render_template('index.html', total_population=data['total_population'], percentage=data['percentage_of_population'], age_group=age_group)
    else:
        return render_template('index.html', error="Invalid age group selection.")


if __name__ == '__main__':
    app.run(debug=True)
