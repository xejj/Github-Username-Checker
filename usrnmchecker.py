import requests
import time
from itertools import product
from termcolor import colored

# --- CONFIG ---
PAT = ''  # Replace with your actual token
GITHUB_API_URL = "https://api.github.com/users/{}"
SIGNUP_CHECK_URL = "https://github.com/signup_check/username?suggestions=true&value={}"

def verify_registration(username):

    try:
        time.sleep(1.5)
        r = requests.get(SIGNUP_CHECK_URL.format(username))
        return r.status_code == 200
    except Exception as e:
        print(f"Error checking username {username}: {e}")
        return False

def check_username(username):

    headers = {'Authorization': f'token {PAT}'}
    
    try:
        response = requests.get(GITHUB_API_URL.format(username), headers=headers)
        if response.status_code == 403:
            reset = int(response.headers.get('X-RateLimit-Reset', time.time() + 60))
            wait = reset - int(time.time()) + 5
            print(f"\n[!] API Rate limit! Sleeping {wait}s...")
            time.sleep(max(0, wait))
            return check_username(username)
        return response.status_code
    
    except Exception as e:
        print(f"Error checking username {username}: {e}")
        return 500

def main():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    print(f"Searching for [Consonant-Vowel-Vowel-Consonant] usernames...")
    print("Yellow (name) = Ghost 404 (Taken). Green = TRULY AVAILABLE.\n")
    
    combinations = product(consonants, vowels, vowels, consonants)
    for combo in combinations:
        username = ''.join(combo)

        status = check_username(username)
        if status == 404:

            if verify_registration(username):
                print(colored(f"\n [!!!] CLAIMABLE: {username} ", 'white', 'on_green'))
                with open("claimable_names.txt", "a") as f:
                    f.write(f"{username}\n")

            else:
                print(colored(f"({username})", 'yellow'), end=' ', flush=True)
        else:
            print(colored(username, 'red'), end=' ', flush=True)

if __name__ == "__main__":
    main()
