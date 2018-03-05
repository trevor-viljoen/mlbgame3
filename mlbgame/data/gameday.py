#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mlbgame functions for the games API endpoints.

This module's functions gets the JSON payloads for the mlb.com games API
endpoints.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

from datetime import datetime
from mlbgame.data import request
import mlbgame.exceptions

TODAY = datetime.now().strftime("%m/%d/%Y")

def get_schedule(params={'sportId': 1, 'date': TODAY}):
    """
    This endpoint allows you to pull shedules.
    params:
      calendarTypes
        Description: Comma delimitd list of type of events
        Parameter Type: query
        Data Type: array[string]
      teamId
        Description: Unique Team Identifier.
        Format: 141, 147, etc.
        Parameter Type: query
        Data Type: array[integer]
      leagueId
        Description: Unique League Identifier
        Parameter Type: query
        Data Type: array[integer]
      sportId
        Description: Top level organization of a sport
        Format: SportId is 1 for MLB
        Parameter Type: query
        Data Type: array[integer]
      gamePk
        Description: Unique Primary Key representing a game
        Parameter Type: query
        Data Type: integer
      gamePks
        Description: Comma delimited list of unique primary keys
        Parameter Type: query
        Data Type: array[integer]
      eventIds
        Description: A unique identifier for non-game event
        Parameter Type: query
        Data Type: array[integer]
      venueIds
        Description: Unique Venue Identifier
        Parameter Type: query
        Data Type: array[integer]
      performerIds
        Description: A unique identifier for non-team event performers
        Parameter Type: query
        Data Type: array[integer]
      gameType
        Description: Type of Game. Available types in api/v1/gameTypes
        Parameter Type: query
        Data Type: array[string]
      gameTypes
        Description: Comma delimited list of type of Game.
        Parameter Type: query
        Data Type: array[string]
      season
        Description: Season of play
        Parameter Type: query
        Data Type: array[string]
      seasons
        Description: Comma delimited list of seasons of play
        Parameter Type: query
        Data Type: array[string]
      date
        Description: Date of Game
        Format: MM/DD/YYYY
        Parameter Type: query
        Data Type: LocalDate
      startDatem
        Description: Start date for range of data. Must be used with end date.
        Format: MM/DD/YYYY
        Parameter Type: query
        Data Type: LocalDate
      endDate
        Description: End date for range of data. Must be used with start date.
        Format: MM/DD/YYYY
        Parameter Type: query
        Data Type: LocalDate
      timecode
        Description: Use this parameter to return a snapshot of the data at
          the specified time.
        Format: YYYYMMDD_HHMMSS
        Parameter Type: query
        Data Type: string
      useLatestGames
        Description: userLatestGames???
        Parameter Type: query
        Data Type: boolean
      opponentId
        Description: A unique identifier for the opposing team. Must be usted
          with teamId.
        Parameter Type: query
        Data Type: integer (Documentation says array[integer])
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]
    """
    if 'startDate' in params.keys():
        if 'endDate' not in params.keys():
            error = 'Query contains startDate with no endDate.'
            raise mlbgame.exceptions.ScheduleParamaterException(error)
    if 'endDate' in params.keys():
        if 'startDate' not in params.keys():
            error = 'Query contains endDate with no startDate.'
            raise mlbgame.exceptions.ScheduleParamaterException(error)
    if 'opponentId' in params.keys():
        if 'teamId' not in params.keys():
            error = 'Query contains opponentId with no teamId.'
            raise mlbgame.exceptions.ScheduleParamaterException(error)
    return request(8, 'schedule', params=params)
