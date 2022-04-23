"""
Movie program
"""

class Movie:
    """Movie class for storing details of a movie."""

    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self) -> str:
        if self.is_watched:
            return '{} ({} from {}) watched'.format(self.title, self.category, self.year)
        return '{} ({} from {})'.format(self.title, self.category, self.year)

    def watched_movie(self):
        self.is_watched = True
        return 'You have watched {}'.format(self.title)

    def unwatched_movie(self):
        self.is_watched = False
        return 'You need to watch {}'.format(self.title)
