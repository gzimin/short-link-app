import random
import string


def generate_random_link():
    link_len = 5
    return ''.join(random.choice(string.ascii_uppercase +
                                             string.ascii_lowercase +
                                             string.digits) for _ in range(link_len))

def check_url(source_link):
    protocols = ["http://", "https://"]
    for protocol in protocols:
        if source_link.startswith(protocol):
            return True
    return False
