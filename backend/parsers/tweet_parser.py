import re

PAT_USER = r'[\s^]@([\d]*)'


def get_users(content):
    return re.findall(PAT_USER, content)