import json

class Players(object):
  def __init__(self):
    self.reset()

  def add(self, sid, name):
    self.players[sid] = name

  def remove(self, sid):
    self.toggle_spymaster(sid, False)
    del self.players[sid]

  def toggle_spymaster(self, sid, state):
    if state:
      self.spymasters.add(sid)
    else:
      if sid in self.spymasters:
        self.spymasters.remove(sid)

  def reset(self):
    self.players = {}
    self.spymasters = set()

  def as_dict(self):
    return {
      "players": self.players,
      "spymasters": list(self.spymasters)
    }
