#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import mlbgame.version

#TEST_URL = "https://statsapi.mlb.com/api/v1/game/447440/boxscore"
API_VERSION = "v1"
API = ("conference", "config", "division", "draft", "game", "homerunderby", "league", "person",
       "schedule", "season", "sports", "standings", "stats", "team", "venue")

def request(pos, endpoint, game_pk=None, params=None):
    """This method takes a game_pk, an API endpoint, and optionally a dictionary of params passed as
    a query to the API endpoint.

    Args:
        pos (int): An int corresponding to a position in the the API tuple.
        game_pk (int): The game primary key
        endpoint (string): The API endpoint
        params (dict): An optional dictionary of key/value pairs described in the mlbgame.game
            methods passed to this method.

    Returns:
        dict: The returned object is the json payload from the API endpoint.

    Raises:
        urllib.error.HTTPError: If a 401, 403, or 404 error is returned from the request.

    """
    """ game_pk not used in schedule endpoint """
    if game_pk:
        base_url = "https://statsapi.mlb.com/api/{0}/{1}/{2}/{3}"
        api_url = base_url.format(API_VERSION, API[pos], endpoint, game_pk)
    else:
        base_url = "https://statsapi.mlb.com/api/{0}/{1}"
        api_url = base_url.format(API_VERSION, API[pos])
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
            json_data = api_request.json()
        except json.decoder.JSONDecodeError as e:
            print('{0}'.format(api_request.url))
            raise e
    except requests.exceptions.RequestException as e:
        print('{0}'.format(e))
        raise e
    return dict(json_data)

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
