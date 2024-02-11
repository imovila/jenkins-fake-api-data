import requests
import yaml


# API
def get_random_users():
    try:
        response = requests.get("https://random-data-api.com/api/v2/users")
        data = response.json()
        return data
    except Exception as e:
        print("Error:", e)


# Appel de la fonction pour obtenir les utilisateurs aléatoires
random_users = get_random_users()

# Conversion en YAML
random_users_yaml = yaml.dump(random_users)

# Affichage des données YAML dans la console
print(random_users_yaml)