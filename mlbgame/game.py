#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import mlbgame.object

class Info(object):

    def __init__(self, data):
        for d in data:
            if d['label'] == 'Umpires':
                setattr(self, 'umpires', Info.umpires(d['value']))
            if d['label'] == 'WP':
                setattr(self, 'wp', d['value'].rstrip('.'))
            if d['label'] == 'IBB':
                ibb_list = Info.str_to_list(d['value'])
                setattr(self, 'ibb', ibb_list)
            if d['label'] == 'HBP':
                hbp_list = Info.str_to_list(d['value'])
                setattr(self, 'hbp', hbp_list)
            if d['label'] == 'Batters faced':
                bf_list = Info.str_to_list(d['value'])
                setattr(self, 'batters_faced', Info.list_to_dict(bf_list))
            if d['label'] == 'Groundouts-flyouts':
                gofo_list = Info.str_to_list(d['value'])
                gofo_list = Info.list_to_dict(gofo_list)
                go_list = []
                fo_list = []
                for i in gofo_list:
                    for k,v in i.items():
                        go_list.append({k: v[0]})
                        fo_list.append({k: v[1]})
                setattr(self, 'groundouts', go_list)
                setattr(self, 'flyouts', fo_list)
            if d['label'] == 'Pitches-strikes':
                ps_list = Info.str_to_list(d['value'])
                ps_list = Info.list_to_dict(ps_list)
                p_list = []
                s_list = []
                for i in ps_list:
                    for k,v in i.items():
                        p_list.append({k: v[0]})
                        s_list.append({k: v[1]})
                setattr(self, 'pitches', p_list)
                setattr(self, 'strikes', s_list)
            if d['label'] == 'T':
                timestr = d['value'].rstrip('.')
                setattr(self, 'duration', Info.str_to_timedelta(timestr))
            if d['label'] == 'First pitch':
                setattr(self, 'first_pitch', d['value'].rstrip('.'))
            if d['label'] == 'Att':
                attendance = int(d['value'].replace(',','').rstrip('.'))
                setattr(self, 'attendance', attendance)
            if d['label'] == 'Venue':
                setattr(self, 'venue', d['value'])
            if d['label'] == 'Weather':
                setattr(self, 'weather', d['value'])
            if d['label'] == 'Wind':
                setattr(self, 'wind', d['value'])
            if 'value' not in d:
                gamedate = datetime.strptime(d['label'].rstrip('.'), "%B %d, %Y")
                setattr(self, 'date', gamedate)

    @staticmethod
    def list_to_dict(data):
        players = []
        for p in data:
            player = p.rsplit(' ', 1)
            try:
                players.append({player[0]: int(player[1])})
            except ValueError:
                try:
                    players.append({player[0]: [int(p) for p in player[1].split('-')]})
                except:
                    players.append({player[0]: player[1]})
        return players

    @staticmethod
    def str_to_list(data):
        return [p.rstrip('.') for p in data.split('; ')]

    @staticmethod
    def str_to_timedelta(timestr):
        t = datetime.strptime(timestr, "%H:%M")
        return timedelta(hours=t.hour, minutes=t.minute)

    @staticmethod
    def umpires(data):
        umpires = []
        temp_list = data.split('. ')
        for val in temp_list:
            ump_role = val.split(': ')
            ump = {ump_role[0]: ump_role[1].rstrip('.')}
            umpires.append(Umpire(ump))
        return umpires


class Umpire(object):
    def __init__(self, data):
        for ass, name in data.items():
            setattr(self, 'assignment', ass)
            setattr(self, 'name', name)
#class Game(mlbgame.object.Object):
#    """ Game object class """
#    def __init__(self, data):

class Color(mlbgame.object.Object):
    pass

class ColorTimestamps(mlbgame.object.Object):
    pass

class ColorDiff(mlbgame.object.Object):
    pass

class Content(mlbgame.object.Object):
    pass

class ContextMetrics(mlbgame.object.Object):
    pass

class LineScore(mlbgame.object.Object):
    pass

class Live(mlbgame.object.Object):
    pass

class LiveDiff(mlbgame.object.Object):
    pass

class LiveTimestamps(mlbgame.object.Object):
    pass

class Status(mlbgame.object.Object):
    pass

class PlayByPlay(mlbgame.object.Object):
    pass

class WinProbability(mlbgame.object.Object):
    pass
