#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import mlbgame.version
import mlbgame.exceptions

#TEST_URL = "https://statsapi.mlb.com/api/v1/game/447440/boxscore"
API_VERSION = "v1"
API_URL = "https://statsapi.mlb.com/api/{}".format(API_VERSION)


# Endpoint constants point to the endpoint method name.
class Endpoint(object):
    ATTENDANCE = "attendance"
    AWARDS = "awards"
    CONFERENCE = "conferences"
    DIVISION = "division"
    DRAFT = "draft"
    GAME = "game"
    GAMEPACE = "gamePace"
    HIGHLOW = "highLow"
    HOMERUNDERBY = "homeRunDerby"
    JOB = "jobs"
    LEAGUE = "league"
    PERSON = "people"
    SCHEDULE = "schedule"
    SEASON = "seasons"
    SPORTS = "sports"
    STANDINGS = "standings"
    STATS = "stats"
    TEAM = "teams"
    VENUE = "venues"

# Endpoints that include configuration information that likely won't change
class EndpointConfig(object):
    BASEBALL_STATS = "baseballStats"
    EVENT_TYPES = "eventTypes"
    GAME_STATUS = "gameStatus"
    GAME_TYPES = "gameTypes"
    HIT_TRAJECTORIES = "hitTrajectories"
    JOB_TYPES = "jobTypes"
    LANGUAGES = "languages"
    LEAGUE_LEADER_TYPES = "leagueLeaderTypes"
    LOGICAL_EVENTS = "logicalEvents"
    METRICS = "metrics"
    PITCH_CODES = "pitchCodes"
    PITCH_TYPES = "pitchTypes"
    PLATFORMS = "platforms"
    POSITIONS = "positions"
    REVIEW_REASONS = "reviewReasons"
    ROSTER_TYPES = "rosterTypes"
    SCHEDULE_EVENT_TYPES = "scheduleEventTypes"
    SITUATION_CODES = "situation_codes"
    SKY = "sky"
    STANDINGS_TYPES = "standingsTypes"
    STAT_GROUPS = "statGroups"
    STAT_TYPES = "statTypes"
    WIND_DIRECTION = "windDirection"


def request(pos, endpoint=None, primary_key=None, secondary_key=None,
            params=None):
    """This method takes a primary_key, an API endpoint, and optionally a
    dictionary of params passed as a query to the API endpoint.

    Args:
        pos (int): An int corresponding to a position in the the API tuple.
        primary_key (int): The primary key, ex: game_pk, person_id
        endpoint (string): The API endpoint
        params (dict): An optional dictionary of key/value pairs described in
            the mlbgame.game methods passed to this method.

    Returns:
        dict: The returned object is the json payload from the API endpoint.

    Raises:
        requests.exceptions.RequestException
    """

    api_url = get_api_url(pos, endpoint, primary_key, secondary_key, params)
    headers = {
        'User-Agent': 'mlbgame/{0}'.format(mlbgame.version.__version__),
        'Accept-encoding': 'gzip',
        'Connection': 'close'
    }
    try:
        if params:
            api_request = requests.get(api_url, params=params, headers=headers)
        else:
            api_request = requests.get(api_url, headers=headers)
        try:
            json_data = api_request.json()
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

def get_api_url(method, endpoint=None, primary_key=None, secondary_key=None, params=None):
    if method == Endpoint.GAME:
        return "{0}/{1}/{2}/{3}".format(API_URL, method, primary_key, endpoint)

    elif method == Endpoint.PERSON:
        if endpoint:
            if secondary_key:
                return "{0}/{1}/{2}/{3}/{4}".format(API_URL, method, primary_key, endpoint, secondary_key)
            else:
                return "{0}/{1}/{2}/{3}".format(API_URL, method, primary_key, endpoint)
        else:
            return "{1}/{2}/{3}".format(API_URL, method, primary_key)

    elif method == Endpoint.SCHEDULE:
        return "{0}/{1}".format(API_URL, method)

    else:
        error = 'The {0} API is not yet implemented.'.format(method)
        raise mlbgame.exceptions.ImplementationException(error)

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
