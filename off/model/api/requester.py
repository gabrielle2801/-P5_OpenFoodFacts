import requests
from off.constants import OFF_API, OFF_API_WORLD


def request_off(url, params=None):
    """Request to the Openfoodfacts Api

    Parameters:
        url (STR): adress write on off_client.py
        params (None, optional): queries write on get_products function
            locate on off_client.py

    Returns:
        LIST : if the status is 200 all products or categories
    """
    response = requests.get(OFF_API + url, params=params)
    print(response)
    print(response.url)

    if response.status_code != 200:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        response = requests.get(OFF_API_WORLD + url, params=params)
        if response.status_code != 200:
            print('[!] [{0}] Authentication Failed'.format(
                response.status_code))
        else:
            return response
    else:
        return response
