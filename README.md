THIS PROJECT IS DEPRECATED AND UNMANAGED/UNMAINTAINED in favor of a rewrite at https://github.com/trevor-viljoen/mlbapi



# mlbgame v3

[![Join Slack](https://img.shields.io/badge/slack-join-blue.svg)](https://mlbgame-slack-invite.herokuapp.com/)

mlbgame v3 - python bindings for MLBAM's StatsAPI-based JSON API endpoints
mlbgame's data classes will return raw json data from the MLBAM's statsapi.
mlbgame's in `__init__.py` will return python objects from this data.

Examples
--------
Get the schedule for a given team during a given timeframe:

```python
import mlbgame

params = {'sportId': 1, 'startDate': '04/01/2018', 'endDate': '11/01/2018', 'teamId': 117}
astros_schedule = mlbgame.schedule(params)
```

Get the schedule for a given team for a given date:

```python
import mlbgame

params = {'sportId': 1, 'date': '03/05/2018', 'teamId': 117}
astros_schedule = mlbgame.schedule(params)
```

Get the game info such as attendance, weather, wind, and venue for a given game:

```python
import mlbgame

params = {'sportId': 1, 'date': '03/05/2018', 'teamId': 117}
astros_schedule = mlbgame.schedule(params)

game_pk = schedule['dates'][0]['games'][0]['gamePk']
game = mlbgame.info(game_pk)
attendance = game.attendance
weather = game.weather
wind = game.wind
venue = game.venue

print('attendance: {0}\nweather: {1}\nwind: {2}\nvenue: {3}'.format(attendance, weather, wind, venue))
```
