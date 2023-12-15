class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        elif hasattr(self, "title"):
            raise Exception("Title cannot be changed")
        elif not len(title) > 0:
            raise Exception("Title cannot be empty string")
        else:
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(
            set([result.player for result in Result.all if result.game == self])
        )

    def average_score(self, player):
        score_list = [result.score for result in Result.all if result.game == self]
        if score_list:
            return sum(score_list) / len(score_list)
        else:
            return "0"


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not isinstance(username, str):
            raise Exception("Username must be a string")
        elif not 2 <= len(username) <= 16:
            raise Exception("Username must be between 2 and 16 characters")
        else:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(
            set([result.game for result in Result.all if result.player == self])
        )

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        game_played = game
        if game_played in self.games_played():
            return len(
                [
                    result.game
                    for result in Result.all
                    if result.game == game_played and result.player == self
                ]
            )
        else:
            return 0


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise Exception("Score must be an integer")
        elif hasattr(self, "score"):
            raise Exception("Score cannot be changed")
        else:
            self._score = score
