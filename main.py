from kivy.app import App
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from moviecollection import MovieCollection
from movie import Movie


SORT_FIELDS = {'Year': "year", 'Title': "title", 'Category': "category", 'Watched': "is_watched"}
CATEGORY_LIST = ['Action', 'Comedy', 'Documentary', 'Drama', 'Fantasy', 'Thriller']
WATCHED_COLOR = [1, 1, 0, 1]
UHWATCHED_COLOR = [0, 10, 225, 0.5]

class MoviesToWatchApp(App):
    bottom_status = StringProperty()
    top_status = StringProperty()
    current_sort_field = StringProperty()
    sort_field_codes = ListProperty()
    """ MoviesToWatchApp class """

    def build(self):
        """ Build Kivy app from the kv file """
        self.title = "Movie"
        self.root = Builder.load_file('app.kv')
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies('movies.csv')
        self.create_entry_buttons()
        self.sort_field_codes = sorted(SORT_FIELDS.keys())
        self.current_sort_field = self.sort_field_codes[0]
        self.sort_movies(self.current_sort_field)
        self.get_top_status()
        return self.root

    def create_entry_buttons(self):
        """ Create the entry buttons and add them to the GUI :return: None """
        for movie in self.movie_collection.movies:
            # create a button for each movie entry
            if movie.is_watched:
                temp_button = Button(text=movie.__str__(), background_color=WATCHED_COLOR)
            else:
                temp_button = Button(text=movie.__str__(), background_color=UHWATCHED_COLOR)
            temp_button.movie = movie
            temp_button.bind(on_release=self.press_movie)
            self.root.ids.entries_box.add_widget(temp_button)

    def get_top_status(self):
        """ Get top status to show in top of the right"""
        self.top_status = f"To watch: {self.movie_collection.number_unwatched_movies()} Watched: {self.movie_collection.number_watched_movies()}"

    def sort_movies(self, key):
        """ Handle change of spinner selection, to sort list movies """
        value = SORT_FIELDS.get(key)
        if value:
            self.movie_collection.sort(value)
            self.current_sort_field = key
        self.root.ids.entries_box.clear_widgets()
        self.create_entry_buttons()

    def press_clear(self):
        """ Handle clear button click event"""
        self.handle_clear()

    def handle_clear(self):
        """ Clear all text in the input fields and the status label """
        self.root.ids.title.text = ""
        self.root.ids.category.text = ""
        self.root.ids.year.text = ""
        self.bottom_status = ""

    def press_movie(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update bottom_status text and top_status text
        if instance.movie.is_watched:
            instance.background_color = UHWATCHED_COLOR
            self.bottom_status = instance.movie.unwatched_movie()
        else:
            instance.background_color = WATCHED_COLOR
            self.bottom_status = instance.movie.watched_movie()
        instance.text = instance.movie.__str__()
        self.get_top_status()

    def press_add(self, title, category, year):
        """ Handler for adding new movie """
        # validate data
        if not title or not category or not year:
            self.bottom_status = 'All fields must be completed'
            return
        try:
            year = int(year)
            if year < 0:
                self.bottom_status = 'Year must be >= 0'
                return
        except ValueError:
            self.bottom_status = 'Please enter a valid year'
            return
        if category not in CATEGORY_LIST:
            self.bottom_status = 'Category must be one of Action, Comedy, Documentary, Drama, Fantasy, Thriller'
            return

        movie = Movie(title=title, category=category, year=year)
        self.movie_collection.add_movie(movie=movie)

        # update top_status text and sort list movies again
        self.get_top_status()
        self.handle_clear()
        self.sort_movies(self.current_sort_field)

    def on_stop(self):
        """ Handler for stop program and save movies to csv file """
        self.movie_collection.save_movies('movies.csv')

if __name__ == '__main__':
    MoviesToWatchApp().run()
