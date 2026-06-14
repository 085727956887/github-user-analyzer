import github_api

print("-" * 50)
print("=== Pencari Profile Github ===")

username = input("Masukkan username Github: ")
profile = github_api.get_github_profile(username)
github_api.display_profile(profile)
github_api.analyze_profile(profile)

print("-" * 50)