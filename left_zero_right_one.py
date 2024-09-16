import json
import pytest
import logging
import os


# Configure logging
logging.basicConfig(
    filename='students_average.log',  # Log file name
    level=logging.INFO,               # Logging level (INFO captures calculations)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to calculate the average score for a student
def calculate_average(test_scores):
    return sum(test_scores) / len(test_scores)

# Load the JSON file before running the tests
@pytest.fixture
def load_students_data():
    with open('students_data.json', 'r') as file:
        students = json.load(file)
    return students

# Expected average scores for each student (fill in with correct values based on your test scores)
expected_averages = {
    "John Doe": 85.0,
    "Jane Smith": 87.67,
    "Emily Johnson": 88.0,
    "Michael Brown": 76.33,
    "Sarah Davis": 92.67,
    "David Wilson": 83.0,
    "Sophia Martinez": 90.33
}

# Test function to verify the average for each student
def test_students_average(load_students_data):
    print("\n=====================================")
    print("Current working directory:", os.getcwd())
    print("=====================================")
    if not os.access('.', os.W_OK):
        print("Directory is not writable.")
    else:
        print("Directory is writable.")
    students = load_students_data
    for student in students:
        name = f"{student['first_name']} {student['last_name']}"
        test_scores = student['test_scores']
        calculated_average = calculate_average(test_scores)

        # Log the calculation
        logging.info(f"Calculating average for {name}: Test scores = {test_scores}, Calculated average = {calculated_average:.2f}")

        # Compare calculated average with the expected average, rounded to 2 decimal places
        expected_average = expected_averages[name]
        assert round(calculated_average, 2) == expected_average, f"Average for {name} is incorrect"

        # Log the result
        logging.info(f"Expected average for {name}: {expected_average:.2f}, Test passed.")
