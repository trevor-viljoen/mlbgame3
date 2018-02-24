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

TODAY = datetime.now().strftime("%m/%d/%Y")

def get_schedule(params={'sportId': 1, 'date': TODAY}):
    return request(8, 'schedule', params=params)
