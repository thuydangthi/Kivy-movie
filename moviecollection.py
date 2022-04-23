"""
MovieCollection program
"""

import sys, csv
from movie import Movie


class MovieCollection:
    """MovieCollection class for storing a collection of movies."""

    def __init__(self) -> None:
        self.movies = []

    def load_movies(self, file_name):
        try:
            movie_file = open(file_name)
        except FileNotFoundError:
            print('File {} does not exist.'.format(file_name))
            sys.exit(1)

        csv_reader = csv.reader(movie_file, delimiter=',')
        movies = []
        for row in csv_reader:
            is_watched = True if row[3].strip().upper() == 'W' else False
            movie = Movie(title=row[0], year=int(row[1]), category=row[2], is_watched=is_watched)
            movies.append(movie)
        self.movies = movies
        movie_file.close()

    def add_movie(self, movie):
        self.movies.append(movie)

    def sort(self, key):
        self.movies = sorted(self.movies, key=lambda movie: (getattr(movie, key), movie.title))

    def save_movies(self, file_name):
        movie_file = open(file_name, 'w', newline='')

        writer = csv.writer(movie_file)
        for movie in self.movies:
            writer.writerow([movie.title, movie.year, movie.category, 'W' if movie.is_watched else 'U'])
        movie_file.close()

    def number_watched_movies(self):
        nubmer = sum(map(lambda movie : movie.is_watched, self.movies))
        return nubmer

    def number_unwatched_movies(self):
        nubmer = sum(map(lambda movie : not movie.is_watched, self.movies))
        return nubmer
