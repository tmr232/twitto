import re

PAT_USER = r'@([\d]*)'


def get_users(content):
    return re.findall(PAT_USER, content)