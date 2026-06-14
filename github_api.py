import requests

l = "Level:"

def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def display_profile(profile):
    if profile:
        print(f"Nama: {profile.get('name', 'N/A')}")
        print(f"Username: {profile.get('login', 'N/A')}")
        print(f"Bio: {profile.get('bio', 'N/A')}")
        print(f"Lokasi: {profile.get('location', 'N/A')}")
        print(f"Repositori Publik: {profile.get('public_repos', 'N/A')}")
        print(f"Followers: {profile.get('followers', 'N/A')}")
        print(f"Following: {profile.get('following', 'N/A')}")
    else:
        print("Profil tidak ditemukan.")

def analyze_profile(profile):
    if profile:
        public_repos = profile.get('public_repos', 0)
        if public_repos < 10:
            print(f"{l} Pemula\nRepository publik masih di bawah 10.")
        elif public_repos > 10 and public_repos < 50:
            print(f"{l} Aktif\nSudah memiliki cukup banyak repository publik.")
        else:
            print(f"{l} Power User\nMemiliki banyak repository publik.")
    else:
        print("Profil tidak ditemukan.")
