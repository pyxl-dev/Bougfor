# Brute Force Script

This script is an asynchronous brute force script that attempts to login to an endpoint using a given username and a wordlist.

## Prerequisites

- Python 3.7 or later
- aiohttp
- asyncio
- argparse
- colorama
- logging
- tqdm

## Usage

The script takes the following arguments:

- -u, --username: The username to use for the login attempt. Default is "foo@bar.com"
- -w, --wordlist: The wordlist to use for the brute force. Default is "wordlist.txt"
- -U, --url: The url of the website to target. Default is "https://foo.bar"
- -e, --endpoint: The endpoint to target for the login attempt. Default is "/account/login"
- -l, --log: The log file to store the results of the brute force. Default is "brute_force.log"

The script will try each password from the wordlist and log the results in the specified log file. If a successful login attempt is made, the script will stop and log the successful attempt.

It uses the `aiohttp` library to make the requests, which allows for a higher rate of requests than using the `requests` library. It also uses the `tqdm` library to display a progress bar, and the `logging` library to log the results of the brute force.

**Please be aware that this script is for educational purposes only and should not be used to commit any illegal or unauthorized actions. It is also important to note that this script may be detected as malicious by security systems and should be used with caution.**
