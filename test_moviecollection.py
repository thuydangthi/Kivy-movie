from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    print("Test sorting - year:")
    movie_collection.sort("year")
    print(movie_collection)

    # TODO: Add more sorting tests
    movie1 = Movie(title='A', year=2021, category='Action', is_watched=True)
    movie2 = Movie(title='D', year=2019, category='Comedy', is_watched=False)
    movie3 = Movie(title='C', year=2019, category='Horror', is_watched=False)
    initial_movie_collection = MovieCollection()
    initial_movie_collection.add_movie(movie1)
    initial_movie_collection.add_movie(movie2)
    initial_movie_collection.add_movie(movie3)
    assert initial_movie_collection.movies == [movie1, movie2, movie3]

    # Test sorting - year
    initial_movie_collection.sort("year")
    assert initial_movie_collection.movies == [movie3, movie2, movie1]

    # Test sorting - title
    initial_movie_collection.sort("title")
    assert initial_movie_collection.movies == [movie1, movie3, movie2]

    # Test sorting - category
    initial_movie_collection.sort("category")
    assert initial_movie_collection.movies == [movie1, movie2, movie3]

    # Test sorting - is_watched
    initial_movie_collection.sort("is_watched")
    assert initial_movie_collection.movies == [movie3, movie2, movie1]

    # TODO: Test saving movies (check CSV file manually to see results)
    initial_movie_collection.save_movies('movies_test.csv')

    # TODO: Add more tests, as appropriate, for each method
    # Test get number of unwatched movies
    assert initial_movie_collection.number_watched_movies() == 1

    # Test get number of unwatched movies
    assert initial_movie_collection.number_unwatched_movies() == 2


run_tests()
