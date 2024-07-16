import json

# Data structure with 10 entries
data = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "phone_number": "123-456-7890",
        "test_scores": {
            "test1": 85,
            "test2": 92,
            "test3": 78
        }
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "phone_number": "234-567-8901",
        "test_scores": {
            "test1": 88,
            "test2": 79,
            "test3": 91
        }
    },
    {
        "id": 3,
        "first_name": "Alice",
        "last_name": "Johnson",
        "phone_number": "345-678-9012",
        "test_scores": {
            "test1": 90,
            "test2": 85,
            "test3": 88
        }
    },
    {
        "id": 4,
        "first_name": "Bob",
        "last_name": "Lee",
        "phone_number": "456-789-0123",
        "test_scores": {
            "test1": 76,
            "test2": 80,
            "test3": 89
        }
    },
    {
        "id": 5,
        "first_name": "Charlie",
        "last_name": "Brown",
        "phone_number": "567-890-1234",
        "test_scores": {
            "test1": 95,
            "test2": 94,
            "test3": 99
        }
    },
    {
        "id": 6,
        "first_name": "Diana",
        "last_name": "Prince",
        "phone_number": "678-901-2345",
        "test_scores": {
            "test1": 87,
            "test2": 88,
            "test3": 85
        }
    },
    {
        "id": 7,
        "first_name": "Eve",
        "last_name": "White",
        "phone_number": "789-012-3456",
        "test_scores": {
            "test1": 92,
            "test2": 91,
            "test3": 90
        }
    },
    {
        "id": 8,
        "first_name": "Frank",
        "last_name": "Green",
        "phone_number": "890-123-4567",
        "test_scores": {
            "test1": 78,
            "test2": 82,
            "test3": 84
        }
    },
    {
        "id": 9,
        "first_name": "Grace",
        "last_name": "Black",
        "phone_number": "901-234-5678",
        "test_scores": {
            "test1": 80,
            "test2": 85,
            "test3": 87
        }
    },
    {
        "id": 10,
        "first_name": "Hank",
        "last_name": "Hill",
        "phone_number": "012-345-6789",
        "test_scores": {
            "test1": 89,
            "test2": 92,
            "test3": 93
        }
    }
]


# Function to calculate the average of three test scores
def calculate_average(scores):
    return sum(scores.values()) / len(scores)


# Iterate through each entry and print the required information
for person in data:
    id = person["id"]
    first_name = person["first_name"]
    last_name = person["last_name"]
    test_scores = person["test_scores"]
    average_score = calculate_average(test_scores)

    print(f"ID: {id}, {first_name} {last_name} has an average score of {average_score:.2f}")
