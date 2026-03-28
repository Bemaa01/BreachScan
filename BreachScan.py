import requests 
import hashlib 
import sys

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    print(res)  
    if res.status_code !=200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again")
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pawned_api_check(password): 
#Convert Password to SHA1
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_five_char, tail = sha1password[:5], sha1password[5:] #First 5 characters and the rest
    response = request_api_data(first_five_char) #Pass the first 5 characters to the API
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pawned_api_check(password)
        if count:
            print(f"{password} was found {count} times... you should probably change your password")
        else:
            print(f"{password} was not found. Carry on!")
    return "Done!" 

if  __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
