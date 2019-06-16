import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as my_file:
    json_string = json.dumps(data, indent=4)
    print(json_string)