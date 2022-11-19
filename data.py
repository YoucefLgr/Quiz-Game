import requests
parameters = {
    "amount": 30,
    "type": "boolean"
}
questions = requests.get(url="https://opentdb.com/api.php", params=parameters)
questions.raise_for_status()
data = questions.json()
question_data = data["results"]
