# BreachScan

A simple Python script to check whether passwords have appeared in the Have I Been Pwned (HIBP) password breach database using the Pwned Passwords API and k-anonymity.

## Features

- Converts password to SHA-1 hash
- Uses the first 5 hex characters (prefix) for anonymous API lookup
- Compares suffix to results from the Pwned Passwords API
- Reports number of times each password has appeared in known leaks

## Requirements

- Python 3.6+
- `requests` library

Install dependencies:

```bash
pip install requests
```

## Usage

From repository root:

```bash
python BreachScan.py password123 "mySecret!"
```

Output example:

- `password123 was found 1253098 times... you should probably change your password`
- `mySecret! was not found. Carry on!`

## How it works

1. `pawned_api_check(password)`:
   - SHA-1 hash of password
   - split into `first_five_char` and `tail`
2. `request_api_data(query_char)`:
   - GET `https://api.pwnedpasswords.com/range/{first_five_char}`
3. `get_password_leaks_count(response, tail)`:
   - parse response lines `hash_suffix:count`
   - return count for matching suffix

## Security notes

- Does not send the full password to the API.
- Uses the HIBP k-anonymity scheme, where only first 5 characters of SHA-1 are disclosed.
- Always run over HTTPS (the API endpoint is HTTPS by default).

## Error handling

- If the API returns a non-200 status code, the script raises a `RuntimeError`.


