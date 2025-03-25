import requests

def get_token():
    url = "http://localhost/api/v1/auth/jwt/login"
    payload = {
        "grant_type": "password",
        "username": "admin@admin.com",
        "password": "12345678",
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()
    return response.json()["access_token"]

def get_logs():
    token = get_token()
    url = "http://localhost/api/v1/status/logs"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    while True:
        print("Select the operation:")
        print("1. Get logs")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            logs = get_logs()
            print(logs)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
