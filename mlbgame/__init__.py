#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import mlbgame.version
import mlbgame.data.game
import mlbgame.data.gameday
import mlbgame.game
import mlbgame.gameday

VERSION = mlbgame.version.__version__
TODAY = datetime.now().strftime("%m/%d/%Y")

def info(game_pk, params=None):
    data = mlbgame.data.game.get_boxscore(game_pk, params)
    return mlbgame.game.Info(data['info'])

def linescore(game_pk, params=None):
    data = mlbgame.data.game.get_linescore(game_pk, params)
    return mlbgame.game.LineScore(data)

def play_by_play(game_pk, params=None):
    data = mlbgame.data.game.get_playbyplay(game_pk, params)
    return data
    #return mlbgame.game.PlayByPlay(data)

def schedule(params={'sportId': 1, 'date': TODAY}):
    data = mlbgame.data.gameday.get_schedule(params)
    return data
    # Schedule not yet parsed or ready for an object
    #return mlbgame.gameday.Schedule(data)
