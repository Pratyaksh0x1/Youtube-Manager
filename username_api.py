import requests
def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        location = user_data["location"]["country"]
        return user_name, location
    else:
        raise Exception("Failed to fetch user data")