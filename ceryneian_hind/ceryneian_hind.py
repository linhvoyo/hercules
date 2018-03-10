import os
import sys
import requests


def usage():
    """
    Error handling for params
    """
    if len(sys.argv) != 2:
        print "<usage> python ceryneian_hind.py file"
        sys.exit(1)
    try:
        os.environ["client_id"]
    except KeyError:
        print "client_id doesn't exist"
        sys.exit(1)
    try:
        os.environ["client_secret"]
    except KeyError:
        print "client_secret doesn't exist"
        sys.exit(1)

def connect_to_api():
    """
    Connect to 42 api
    """
    credentials = [
        'grant_type=client_credentials',
        'client_id=' + os.environ["client_id"],
        'client_secret=' + os.environ["client_secret"],
        ]
    try:
        response = requests.post("https://api.intra.42.fr/oauth/token?%s" % ("&".join(credentials)))
    except requests.exceptions.RequestException as error_message:
        print error_message
        response = 0
        return response, 0
    if response.status_code == 200:
        return response, 1
    elif response.status_code == 401:
        print "invalid credentials..."
        return response, 1
    return response, 0

def locate_student(intra_id):
    """
    Use intra_id to locate student
    """
    try:
        location = requests.get("https://api.intra.42.fr/v2/users/" + intra_id + \
        "/locations?%s&%s" % ('access_token=' + RESPONSE.json()['access_token'], \
                        'token_type=' + RESPONSE.json()['token_type']) \
                        + "&filter[active]=true")
    except requests.exceptions.RequestException:
        return 0
    if location.status_code == 200:
        if not location.json():
            print intra_id + " is not in"
        else:
            print intra_id + " is currently at %s" % (location.json()[0]['host'])
        return 1
    elif location.status_code == 404:
        print intra_id + "is an invalid intra_id ..."
        return 1
    else:
        print "failed to get location... status code: " + location.status_code
    return 0

usage()
INPUT_FILE = open(sys.argv[1])
for i in INPUT_FILE:
    RESPONSE, status = connect_to_api()
    while status != 1:
        print "trying to reconnect to api..."
        RESPONSE, status = connect_to_api()
    LOCATION = locate_student(i.rstrip())
    while LOCATION != 1:
        print "trying to search for student..."
        LOCATION = locate_student(i.rstrip())
