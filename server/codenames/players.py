import json
import random

class Players(object):
  def __init__(self):
    self.all_players = set()
    self.reset()

  def add(self, sid, name):
    self.players[sid] = name if name else sid
    self.all_players.add(name if name else sid)

  def remove(self, sid):
    self.toggle_spymaster(sid, False)
    if sid in self.players:
      del self.players[sid]

  def toggle_spymaster(self, sid, state):
    if state:
      self.spymasters.add(sid)
    else:
      if sid in self.spymasters:
        self.spymasters.remove(sid)

  def reset_spymasters(self):
    self.spymasters = set()

  def reset(self):
    self.players = {}
    self.spymasters = set()

  def as_dict(self):
    return {
      "players": self.players,
      "spymasters": list(self.spymasters)
    }
