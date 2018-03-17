__count__ = 0
class game:
    def __init__(self, creator_id, count, amount_players):
        self.id = __count__
        self.users = []
        self.users.append(creator_id)
        self.count = count
        self.amount_players = amount_players
    def add_player(self, player):
        if(len(self.users) < self.amount_players):
            self.users.append(player)
        else:
            self.start()
            return -1
    def start():
        #TODO : add start function