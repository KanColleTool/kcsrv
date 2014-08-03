import string
import random

def generate_api_token():
	return ''.join(random.choice(string.hexdigits) for _ in range(40)).lower()
