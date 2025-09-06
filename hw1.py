import requests
import json

url = 'https://student-info-api.netlify.app/.netlify/functions/submit_student_info?UCID=dbp&section=103'

data = {
    "UCID": "dbp",
    "first_name": "Dave",
    "last_name": "Persaud",
    "github_username": "persaucee",
    "discord_username": "Dave Persaud",
    "favorite_cartoon": "SpongeBob SquarePants",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Forrest Gump",
    "section": "103"
}

response = requests.get(url)

# Error handling
if response.status_code == 200:
    print("All actions Completed.")
else:   
    print("Error status:" , response.status_code)
print("Body:" , response.json())