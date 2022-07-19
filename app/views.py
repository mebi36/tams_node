"""
Handles the requests of the app to the server
"""
import json
import os
import requests
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tams_node.settings")
application = get_wsgi_application()

SERVER_ENDPOINT = 'node-devices/backup/'  # TODO: update the url


# method to sync the user data in the server to the node device
def first_time_sync(ip: str, port: int, protocol: str = "http"):
    server_url = f'{protocol}://{ip}:{port}/{SERVER_ENDPOINT}'
    backup_file = 'server_backup.json'
    x = requests.get(server_url).json()

    # Serializing json response
    json_object = json.dumps(x, indent=2)

    # Writing to back up file
    with open(backup_file, "w") as outfile:
        outfile.write(json_object)

    # load the data into node's database
    call_command('loaddata', backup_file)


if __name__ == '__main__':
    first_time_sync("127.0.0.1", 8080)