class Player:
  def __init__(self, name, hp, attack, inventory):
    self.name = name
    self.hp = hp
    self.attack = attack
    self.inventory = inventory

  def __repr__(self) -> str:
    return f"=== STATS ===\nName: {self.name}\nHP: {self.hp}\nInventory: {self.inventory}\nAttack Power: {self.attack}"

class Enemy(Player):
  def __init__(self, name, hp, attack, art, inventory=None):
      super().__init__(name, hp, attack, inventory)
      self.art = art
