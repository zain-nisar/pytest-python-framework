from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import yaml


class ValidateAuthentication:

  def get_api_connection(self, url, api_key, parameters=None):
    try:
      headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
      }
      session = Session()
      session.headers.update(headers)

      response = session.get(url, params=parameters)

      return json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)