#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mlbgame functions for the people API endpoints.

This module's functions gets the JSON payloads for the mlb.com games API
endpoints.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

import mlbgame.data


def get_person(person_id, params=None):
    """This endpoint allows you to pull the information for a player.
    Args:
        person_id (int): Unique Player Identifier
        params (dict): Contains the person_ids, season, group, and fields
            parameters described below.

    params:
      person_id (required)
        Description: Unique Player Identifier
        Parameter Type: path
        Data Type: integer
      person_ids
        Description: Comma delimited list of person ID.
        Format: 1234, 2345
        Parameter Type: query
        Data Type: array[integer]
      season
        Description: Season of play
        Parameter Type: query
        Data Type: string
      group *may not yet do anything
        Description: Category of statistics to return. 0: hitting, 1: pitching,
            2: fielding, 3: running
        Format: 0, 1, 2, 3
        Parameter Type: query
        Data Type: array[string]
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]

    Returns:
        json
    """
    return mlbgame.data.request(7, primary_id=person_id, params=params)

def get_current_game_stats(person_id, params=None):
    """This endpoint allows you to pull the current game status for a given
    player.
    Args:
        person_id (int): Unique PLayer Identifier
        params (dict): Contains the person_ids, season, group, and fields
            parameters described below.

    params:
      person_id (required)
        Description: Unique Player Identifier
        Parameter Type: path
        Data Type: integer
      group *may not yet do anything
        Description: Category of statistics to return. 0: hitting, 1: pitching,
            2: fielding, 3: running
        Format: 0, 1, 2, 3
        Parameter Type: query
        Data Type: array[string]
      timecode
        Description: Use this parameter to return a snapshot of the data at the
            specified time.
        Format: YYYYMMDD_HHMMSS
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]

    Returns:
        json
    """
    return mlbgame.data.request(7, 'stats/game/current', person_id, params)

