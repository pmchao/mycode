import json

# This script calculates the average test score for each student in a JSON dataset.
# It then adds an "average_score" entry to each student's dictionary and prints the updated list.

# Sample JSON data
data = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "test_scores": [85, 92, 78]
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "test_scores": [88, 91, 84]
    },
    {
        "first_name": "Emily",
        "last_name": "Johnson",
        "test_scores": [90, 85, 89]
    },
    {
        "first_name": "Michael",
        "last_name": "Brown",
        "test_scores": [76, 81, 72]
    },
    {
        "first_name": "Sarah",
        "last_name": "Davis",
        "test_scores": [95, 89, 94]
    },
    {
        "first_name": "David",
        "last_name": "Wilson",
        "test_scores": [82, 87, 80]
    },
    {
        "first_name": "Sophia",
        "last_name": "Martinez",
        "test_scores": [88, 90, 93]
    }
]

# Calculate average and add to each entry
for student in data:
    average_score = sum(student["test_scores"]) / len(student["test_scores"])
    student["average_score"] = round(average_score, 2)

# Print updated data
print(json.dumps(data, indent=4))
