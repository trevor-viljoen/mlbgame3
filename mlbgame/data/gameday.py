#!/usr/bin/env python3

from datetime import datetime
import mlbgame.data

TODAY = datetime.now().strftime("%m/%d/%Y")

def get_schedule(params={'sportId': 1, 'date': TODAY}):
    return mlbgame.data.request(8, 'schedule', params=params)
