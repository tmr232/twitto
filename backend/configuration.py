"""
configuration.py
This module defines the configuration for the Backend server.
"""
import hashlib

DATABASE_NAME = "twitto"

COOKIE_SECRET = "@llURB4s3RB3l0ng2us"
PASSWORD_SALT_LENGTH = 32  # for sha256

PASSWORD_HASH_FUNCTION = hashlib.sha256

APP_PORT = 8888
