import webbrowser

class Movie():
	"""This class stores information about movies"""

	def __init__(self, movie_title, movie_story, movie_poster, movie_trailer,
	 movie_release_date, movie_director, movie_genre, movie_language, 
	 movie_duration, movie_rating):
		"""Initializes the instance of class
	
			Arguments 
			movie_title -- The title of the movie
			movie_story -- The story line of the movie
			movie_poster -- URL for the poster of the movie
			movie_trailer -- Youtube URL of trailer of the movie
			movie_release_date -- The release date of the movie
			movie_director -- The Director of the movie
			movie_genre -- Genre of the movie
			movie_language -- Language of the movie
			movie_duration -- Duration of the movie in minutes
			movie_rating -- Rating or Certification of movie

		"""

		self.title = movie_title		# Title of Movie
		self.story_line = movie_story		# Story Line of Movie
		self.poster_image_url = movie_poster	# Poster of Movie
		self.trailer_youtube_url = movie_trailer	# Trailer of Movie
		self.release_date = movie_release_date		# Release Date of Movie
		self.director = movie_director		# Director of Movie
		self.genre = movie_genre		# Genre of Movie
		self.language = movie_language		# Language of Movie
		self.duration = movie_duration		# Duration of Movie in minutes
		self.rating = movie_rating		# Rating of Movie

	def showTrailer(self):
		"""Plays the trailer of the movie in browser"""
		webbrowser.open(self.trailer_youtube_url)
