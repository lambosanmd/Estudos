import requests
import json

textos = [
    "ex", 3, 15,
    "ex", 3, 18,
]

def get_data(abbrev, chap, verse):
    response = requests.get("https://abibliadigital.api.br/api/verses/nvt/" + abbrev + "/" + str(chap) + "/" + str(verse))
    data = json.loads(response.text)
    final = data["book"]["name"] + " " + str(chap) + "." + str(verse) + "\n" + data["text"]
    return final

def main():
    for i in range(0, len(textos), 3):
        print(get_data(textos[i], textos[i + 1], textos[i + 2]))
        print("\n")
    print("\n\n...\n")

if __name__ == "__main__":
    main()
