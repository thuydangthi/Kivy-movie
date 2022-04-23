from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)

    # TODO: Write tests to show this initialisation works
    assert initial_movie.title == "Thor: Ragnarok"
    assert initial_movie.category == "Comedy"
    assert initial_movie.year == 2017
    assert initial_movie.is_watched

    # TODO: Add more tests, as appropriate, for each method
    assert initial_movie.__str__() == 'Thor: Ragnarok (Comedy from 2017) watched'
    assert initial_movie.watched_movie() == 'You have watched Thor: Ragnarok'
    assert initial_movie.is_watched == True
    assert initial_movie.unwatched_movie() == 'You need to watch Thor: Ragnarok'
    assert initial_movie.is_watched == False


run_tests()
