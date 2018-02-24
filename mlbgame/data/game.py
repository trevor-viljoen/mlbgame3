#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mlbgame functions for the games API endpoints.

This module's functions gets the JSON payloads for the mlb.com games API
endpoints.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

from mlbgame.data import request


def get_boxscore(game_pk, params=None):
    """This endpoint allows you to pull the boxscore for a game.
    Args:
        game_pk (int): The game primary key
        params (dict): Contains the timecode and fields parameters described
            below.

    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: integer? #string elsewhere in documentation
      timecode
        Description: Use this parameter to return a snapshot of the data at the
            specified time.
        Format: YYYYMMDD_HHMMSS
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
    return request(4, 'boxscore', primary_key=game_pk, params=params)

def get_color(game_pk, params=None):
    """
    This API can return very large payloads. It is STRONGLY recommended that
    clients ask for diffs and use "Accept-Encoding: gzip" header.

    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: string
      timecode
        Description: Use this parameter to return a snapshot of the data at the
            specified time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]
    """
    return request(4, 'feed/color', primary_key=game_pk, params=params)

def get_color_diff(game_pk, params=None):
    """
    This API can return very large payloads. It is STRONGLY recommended that
    clients ask for diffs and use "Accept-Encoding: gzip" header.

    startTimecode and endTimecode can be used for getting diffs.

    Expected usage:
      1) Request full payload by not passing startTimecode or endTimecode. This
         will return the entire color feed up till the current time.
      2) Find the latest timecode in this response.
      3) Wait X seconds
      4) Use the timecode from 2 as the startTimecode. This will give you a
         diff of everything that has happened since startTimecode.
      5) If no data is returned, wait X seconds and do the same request.
      6) If data is returned, get a new timeStamp from the response, and use
         that for the next call as startTimecode.

    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: string
      startTimecode
        Description: Start time code will give you everything since that time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      endTimecode
        Description: End time code will give you a snapshot at that specific
            time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
    """
    return request(4, 'feed/color/diffPatch', primary_key=game_pk,
                   params=params)

def get_color_timestamps(game_pk, params=None):
    """
    This can be used for replaying games. Endpoint returns all of the timecodes
    that can be used with diffs for mlbgame.data.get_color.

    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: string
    """
    return request(4, 'feed/color/timestamps', primary_key=game_pk,
                   params=params)

def get_content(game_pk, params=None):
    """
    Retrieve game content such as highlights.

    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: integer? #string elsewhere in documentation
      highlightLimit:
        Description: Number of results to return
        Parameter Type: query
        Data Type: integer
    """
    return request(4, 'content', primary_key=game_pk, params=params)

def get_context_metrics(game_pk, params=None):
    """
    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: integer? #string elsewhere in documentation
      timecode
        Description: Use this parameter to return a snapshot of the data at the
            specified time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]
    """
    return request(4, 'contextMetrics', primary_key=game_pk, params=params)

def get_linescore(game_pk, params=None):
    """
    This endpoint allows you to pull the linescore for a game.
    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: integer? #string elsewhere in documentation
      timecode
        Description: Use this parameter to return a snapshot of the data at the
            specified time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]
    """
    return request(4, 'linescore', primary_key=game_pk, params=params)

def get_live(game_pk, params=None):
    """
    This API can return very large payloads. It is STRONGLY recommended that
    clients ask for diffs and use "Accept-Encoding: gzip" header.
    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: string
      timecode
        Description: Use this parameter to return a snapshot of the data at the
            specified time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]
    """
    return request(4, 'feed/live', primary_key=game_pk, params=params)

def get_live_diff(game_pk, params=None):
    """
    This endpoint allows comparison of game files and shows any differences or
    discrepancies between the two.

    Diff/Patch System: startTimecode and endTimecode can be used for getting
        diffs.

    Expected usage:
      1) Request full payload by not passing startTimecode or endTimecode. This
         will return the most recent game state.
      2) Find the latest timecode in this response.
      3) Wait X seconds
      4) Use the timecode from 2 as the startTimecode. This will give you a
         diff of everything that has happened since startTimecode.
      5) If no data is returned, wait X seconds and do the same request.
      6) If data is returned, get a new timeStamp from the response, and use
         that for the next call as startTimecode.

    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: string
      startTimecode
        Description: Start time code will give you everything since that time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      endTimecode
        Description: End time code will give you a snapshot at that specific
            time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
    """
    return request(4, 'feed/live/diffPatch', primary_key=game_pk, params=params)

def get_live_timestamps(game_pk, params=None):
    """
    This can be used for replaying games. Endpoint returns all of the timecodes
    that can be used with diffs for mlbgame.game.live_diff.

    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: string
    """
    return request(4, 'feed/live/timestamps', primary_key=game_pk, params=params)

def get_play_by_play(game_pk, params=None):
    """This endpoint allows you to pull the play by play for a game.
    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: integer? #string elsewhere in documentation
      timecode
        Description: Use this parameter to return a snapshot of the data at
            the specified time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]
    """
    return request(4, 'playByPlay', primary_key=game_pk, params=params)

def get_win_probability(game_pk, params=None):
    """
    params:
      game_pk (required)
        Description: Unique Primary Key Representing a Game
        Parameter Type: path
        Data Type: integer? #string elsewhere in documentation
      timecode
        Description: Use this parameter to return a snapshot of the data at the
            specified time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]
    """
    return request(4, 'winProbability', primary_key=game_pk, params=params)
