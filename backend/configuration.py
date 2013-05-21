"""
configuration.py
This module defines the configuration for the Backend server.
"""
import hashlib

# MongoDB Configuration
DATABASE_NAME = "twitto"

# Security Configuration
COOKIE_SECRET = "@llURB4s3RB3l0ng2us"
ADMIN_PASSWORD = "DEADBABE"

# User password Configuration
PASSWORD_SALT_LENGTH = 32  # for sha256
PASSWORD_HASH_FUNCTION = hashlib.sha256

# Application Configuration
APP_PORT = 8888
