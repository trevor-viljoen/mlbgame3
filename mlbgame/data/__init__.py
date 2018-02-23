#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import mlbgame.version
import mlbgame.exceptions

#TEST_URL = "https://statsapi.mlb.com/api/v1/game/447440/boxscore"
API_VERSION = "v1"
API = ("conference", "config", "division", "draft", "game", "homerunderby",
       "league", "people", "schedule", "season", "sports", "standings",
       "stats", "team", "venue")

def request(pos, endpoint=None, primary_id=None, params=None):
    """This method takes a primary_id, an API endpoint, and optionally a
    dictionary of params passed as a query to the API endpoint.

    Args:
        pos (int): An int corresponding to a position in the the API tuple.
        primary_id (int): The primary key, ex: game_pk, person_id
        endpoint (string): The API endpoint
        params (dict): An optional dictionary of key/value pairs described in
            the mlbgame.game methods passed to this method.

    Returns:
        dict: The returned object is the json payload from the API endpoint.

    Raises:
        requests.exceptions.RequestException
    """
    """ primary_id not used in schedule endpoint """
    if pos == 4:
        base_url = "https://statsapi.mlb.com/api/{0}/{1}/{2}/{3}"
        api_url = base_url.format(API_VERSION, API[pos], endpoint, primary_id)
    elif pos == 7:
        if endpoint:
            base_url = "https://statsapi.mlb.com/api/{0}/{1}/{2}/{3}"
            api_url = base_url.format(API_VERSION, API[pos], primary_id,
                                      endpoint)
        else:
            base_url = "https://statsapi.mlb.com/api/{0}/{1}/{2}"
            api_url = base_url.format(API_VERSION, API[pos], primary_id)
    elif pos == 8:
        base_url = "https://statsapi.mlb.com/api/{0}/{1}"
        api_url = base_url.format(API_VERSION, API[pos])
    else:
        error = 'The {0} API is not yet implemented.'.format(API[pos])
        raise mlbgame.exceptions.ImplementationException(error)

    headers = {
        'User-Agent': 'mlbgame/{0}'.format(mlbgame.version.__version__),
        'Accept-encoding': 'gzip'
    }
    try:
        if params:
            api_request = requests.get(api_url, params=params, headers=headers)
        else:
            api_request = requests.get(api_url, headers=headers)
        try:
            json_data = dict(api_request.json())
            if 'message' in json_data:
                error = 'message number {0}: {1}'.format(
                                                    json_data['messageNumber'],
                                                    json_data['message'])
                raise mlbgame.exceptions.ObjectNotFoundException(error)
        except json.decoder.JSONDecodeError as e:
            print('{0}'.format(api_request.url))
            raise e
    except requests.exceptions.RequestException as e:
        print('{0}'.format(e))
        raise e
    return json_data

# Not yet implemented
#
#class GameDay(object):
#    """ Scoreboard object class """
#    @property
#    def schedule(params={'date': datetime.now().strftime("%m/%d/%Y")}):
#        return data.request(date, 'schedule')



#class League(object):
#""" League object class """
#    @property
