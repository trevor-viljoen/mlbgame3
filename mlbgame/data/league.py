#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mlbgame functions for the league API endpoints.

This module's functions get the JSON payloads for the mlb.com games API
endpoints.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

from mlbgame.data import request


def get_league(league_id, params=None):
    """This endpoint allows you to pull the information for a league.
    Args:
        league_id (int): Unique League Identifier
        params (dict): Contains the league_ids, season, seasons, expand, and
            fields parameters described below.

    params:
      league_id (required)
        Description: Unique League Identifier
        Parameter Type: path
        Data Type: integer
      league_ids
        Description: Comma delimited list of League IDs.
        Format: 1234, 2345
        Parameter Type: query
        Data Type: array[integer]
      season
        Description: Season of play
        Parameter Type: query
        Data Type: string
      seasons
        Description: Seasons of play
        Parameter Type: query
        Data Type: array[string]
      expand
        Description: ?
        Parameter type: query
        Data Type: array[string]
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]

    Returns:
        json
    """
    return request(6, primary_key=league_id, params=params)

def get_league_all_star_ballot(league_id, params=None):
    """This endpoint allows you to pull the all star ballots for a given league.
    Args:
        league_id (int): Unique League Identifier
        params (dict): Contains the group, and fields parameters described
            below.

    params:
      league_id (required)
        Description: Unique Player Identifier
        Parameter Type: path
        Data Type: integer
      league_ids
        Description: Comma delimited list of League IDs.
        Format: 1234, 2345
        Parameter Type: query
        Data Type: array[integer]
      season
        Description: Season of play
        Parameter Type: query
        Data Type: string
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]

    Returns:
        json
    """
    return request(6, 'allStarBallot', primary_key=league_id, params=params)
