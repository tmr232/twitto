import re

PAT_USER = r'@([\d]*)'


def get_users(content):
    return [int(number) for number in re.findall(PAT_USER, content)]