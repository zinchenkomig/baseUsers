import os

db_address = os.getenv('BASE_USERS_DB_ADDRESS')
db_user = os.getenv('BASE_USERS_DB_USER')
db_password = os.getenv('BASE_USERS_DB_PASSWORD')
db_name = os.getenv('BASE_USERS_DB_NAME')

PASSWORD_ENCODING_SECRET = os.getenv('BASE_USERS_PASS_ENCODING_SECRET')
# to get a string like this run:
# openssl rand -hex 32


if None in (db_address, db_name, db_user, db_password, PASSWORD_ENCODING_SECRET):
    raise ValueError("Some ENV variable is not set")
