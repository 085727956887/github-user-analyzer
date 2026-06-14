import requests

LEVEL_LABEL = "Level:"


def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(
        url,
        headers={"User-Agent": "GitHub-User-Analyzer"}
    )

    if response.status_code == 200:
        return response.json()

    print(f"Error Profile API: {response.status_code}")
    return None


def get_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"

    response = requests.get(
        url,
        headers={"User-Agent": "GitHub-User-Analyzer"}
    )

    if response.status_code == 200:
        return response.json()

    print(f"Error Repositories API: {response.status_code}")
    return []


def display_profile(profile):
    if not profile:
        print("Profil tidak ditemukan.")
        return

    print(f"Nama: {profile.get('name', 'N/A')}")
    print(f"Username: {profile.get('login', 'N/A')}")
    print(f"Bio: {profile.get('bio', 'N/A')}")
    print(f"Lokasi: {profile.get('location', 'N/A')}")
    print(f"Repositori Publik: {profile.get('public_repos', 0)}")
    print(f"Followers: {profile.get('followers', 0)}")
    print(f"Following: {profile.get('following', 0)}")


def analyze_profile(profile):
    if not profile:
        print("Profil tidak ditemukan.")
        return

    public_repos = profile.get("public_repos", 0)

    if public_repos < 10:
        print(f"{LEVEL_LABEL} Pemula")
        print("Repository publik masih di bawah 10.")

    elif public_repos < 50:
        print(f"{LEVEL_LABEL} Aktif")
        print("Sudah memiliki cukup banyak repository publik.")

    else:
        print(f"{LEVEL_LABEL} Power User")
        print("Memiliki banyak repository publik.")


def display_repositories(repositories):
    if not repositories:
        print("Tidak ada repositori publik.")
        return

    print(f"\nTotal Repositori: {len(repositories)}")
    print("Repositori Publik:")

    for repo in repositories:
        print(f"- {repo['name']}: {repo['html_url']}")


def analyze_repositories(repositories):
    if not repositories:
        print("Tidak ada repositori untuk dianalisis.")
        return

    total_stars = sum(
        repo.get("stargazers_count", 0)
        for repo in repositories
    )

    total_forks = sum(
        repo.get("forks_count", 0)
        for repo in repositories
    )

    languages = {}

    for repo in repositories:
        language = repo.get("language")

        if language:
            languages[language] = (
                languages.get(language, 0) + 1
            )

    print(f"\nTotal Stars: {total_stars}")
    print(f"Total Forks: {total_forks}")

    print("\nBahasa Utama Repository:")

    if not languages:
        print("- Tidak diketahui")
        return

    for language, count in sorted(
        languages.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(f"- {language}: {count} repo")