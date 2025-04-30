import json

# JSON data as a string
json_data = """
{
    "AFL": [
        {"team_name": "Melbourne Demons", "wins": 10, "losses": 5, "city": "Melbourne"},
        {"team_name": "Sydney Swans", "wins": 8, "losses": 7, "city": "Sydney"},
        {"team_name": "Brisbane Lions", "wins": 12, "losses": 3, "city": "Brisbane"},
        {"team_name": "West Coast Eagles", "wins": 6, "losses": 9, "city": "Perth"},
        {"team_name": "Adelaide Crows", "wins": 7, "losses": 8, "city": "Adelaide"},
        {"team_name": "Gold Coast Suns", "wins": 9, "losses": 6, "city": "Gold Coast"}
    ],
    "NFL": [
        {"team_name": "New York Giants", "wins": 11, "losses": 4, "city": "New York"},
        {"team_name": "Los Angeles Rams", "wins": 5, "losses": 10, "city": "Los Angeles"},
        {"team_name": "Chicago Bears", "wins": 9, "losses": 6, "city": "Chicago"},
        {"team_name": "Houston Texans", "wins": 8, "losses": 7, "city": "Houston"},
        {"team_name": "Arizona Cardinals", "wins": 12, "losses": 3, "city": "Phoenix"},
        {"team_name": "Philadelphia Eagles", "wins": 10, "losses": 5, "city": "Philadelphia"},
        {"team_name": "San Antonio Commanders", "wins": 7, "losses": 8, "city": "San Antonio"}
    ]
}
"""

# Parse the JSON string
data = json.loads(json_data)
print("===",data['AFL'][0])
print (len(data['AFL']))
print("============>>>>>>")


#  # Access the 3rd element from both the NFL and AFL lists
# third_afl_team = data['AFL'][2]
# third_nfl_team = data['NFL'][2]
#
# # Print the 3rd element of both NFL and AFL
# print("3rd AFL Team:", third_afl_team)
# print("3rd NFL Team:", third_nfl_team)
#
# # Calculate total games played for each team and update the JSON data
for team in data['AFL']:
    team['total_games'] = team['wins'] + team['losses']

for team in data['NFL']:
    team['total_games'] = team['wins'] + team['losses']

#Print the updated data to verify
print(json.dumps(data, indent=4))

# Save the modified data to a file
with open('modified_data.json', 'w') as file:
     json.dump(data, file, indent=4)
