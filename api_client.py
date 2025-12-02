import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None

        users = response.json()
        for i in range(min(num_users, len(users))):
            user = users[i]
            try:
                print(f"\nName: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"City: {user['address']['city']}")
            except KeyError:
                print("Error: Missing expected user information.")
                return None

        if num_users > len(users):
            print(f"\nOnly {len(users)} users available.")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

if __name__ == "__main__":
    print("Fetching 5 users:")
    fetch_and_display_users(5)

    print("\nFetching 11 users:")
    fetch_and_display_users(11)
