import webbrowser
import os
import re

# Styles and scripting for the page
page_head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Movie Library!</title>
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
        <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
        <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Reem+Kufi" rel="stylesheet">
        <style type="text/css">
            body
            {
                background: #2D3740;
                background: -webkit-linear-gradient(left top, #2D3740, #8B9492);
                background: -o-linear-gradient(bottom right, #2D3740, #8B9492); 
                background: -moz-linear-gradient(bottom right, #2D3740, #8B9492); 
                background: linear-gradient(to bottom right, #2D3740, #8B9492);
                background-repeat: no-repeat;
            }
            .logo
            {
                cursor:pointer;
            }
            a
            {
                cursor: pointer;
            }
            .primary-color
            {
                color: #00a180;
            }
            .nav
            {
                color: #fff;
                font-family: 'Reem Kufi', sans-serif;
                width: 80%;
                margin: 0 auto;
                display: block;
            }
            .poster-wrapper img
            {
                height: 310px;
                width: 200px;
                overflow: none;
            }
            .tile-wrapper
            {
                padding-top: 25px;
            }
            .movie-tile
            {
                display: flex;
                margin-top:25px;
                margin-bottom:25px;
            }
            .poster
            {
                box-shadow: 0 16px 24px 2px rgba(0,0,0,0.5), 
                            0 6px 30px 5px rgba(0,0,0,0.5), 
                            0 8px 10px -5px rgba(0,0,0,.5);
                transition: all .2s ease-in-out;
                overflow: hidden;
            }
            .poster:hover
            {
                transform: scale(1.1);
            }
            .poster-wrapper
            {
                display: inline-block;
            }
            .details-wrapper
            {
                display: inline-block;
                margin: 0px;
                width: calc(100% - 200px);
                padding-left: 25px;
            }
            .movie-title
            {
                text-transform: uppercase;
                color:#00a180;
                cursor: pointer;
                margin-top:0px;
                margin-bottom: 10px;
            }
            .movie-title:hover
            {
                color:#fff;
            }
            .certification
            {
                background-color: #00a180;
                color: #fff;
                padding: 5px 10px;
                font-weight: bold;
            }
            .movie-story
            {
                color: #e2e2e2;
            }
            .row-name
            {
                color: #000;
                padding: 6px 0px;
                width:90px;
                font-weight: bolder;
            }
            .row-value
            {
                color:#f5f6f0;
            }
            .movie-details-table
            {
                margin-top:20px;
            }
            .action-center
            {
                bottom:10px;
                position: absolute;
            }
            .action-btn
            {
                color: #fff;
                text-decoration: none;
                background: #00a180;
                text-decoration: none;
                padding: 10px 20px;
                font-weight: bold;
                text-transform: uppercase;
                cursor: pointer;
                transition: all .3s ease-in-out;

            }
            .action-btn:hover
            {
                text-decoration: none;
                color: #00a180;
                background-color: #fff;
            }
            #trailer .modal-dialog 
            {
                margin-top: 200px;
                width: 640px;
                height: 480px;
            }
            .scale-media 
            {
                padding-bottom: 56.25%;
                position: relative;
            }
            .scale-media iframe 
            {
                border: none;
                height: 100%;
                position: absolute;
                width: 100%;
                left: 0;
                top: 0;
                background-color: white;
            }
            .hanging-close 
            {
                position: absolute;
                top: -12px;
                right: -12px;
                z-index: 9001;
            }

        </style>

        <script type="text/javascript" charset="utf-8">
            // Pause the video when the modal is closed
            $(document).on('click', '.hanging-close, .modal-backdrop, .modal-dialog', function (event) {
                // Remove the src so the player itself gets removed, as this is the only
                // reliable way to ensure the video stops playing in IE
                $("#trailer-video-container").empty();
            });
            
            // Start playing the video whenever the trailer modal is opened
            $(document).on('click', '.showTrailer', function (event) {
                var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
                var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
                $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                'id': 'trailer-video',
                'type': 'text-html',
                'src': sourceUrl,
                'frameborder': 0
                }));
            });

            // Animate in the movies when the page loads
            $(document).ready(function () {
                $('.movie-tile').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });
        </script>
    </head>
'''


# The main page layout
page_content = '''
    <body>
    <!-- Trailer Modal -->
        <div class="modal" id="trailer" data-backdrop="static" data-keyboard="false">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                    </a>
                    <div class="scale-media" id="trailer-video-container">
                    </div>
                </div>
            </div>
        </div>


        <div class="nav">  <!-- Navigation -->
            <h2 class="logo">trailer<span class="primary-color">Library 
                <span class="glyphicon glyphicon-play" aria-hidden="true"></span>
                </span></h2>
        </div>

        <div class="container tile-wrapper">
            {movie_tiles}
        </div>
    </body>
</html>
'''


# Movie Tile Template 
movie_tile_content='''
<div class="movie-tile col-md-6 col-lg-6">
                <div class="poster-wrapper">
                    <a class="showTrailer" data-toggle='modal' data-target='#trailer' data-dismiss='modal' data-trailer-youtube-id="{trailer_youtube_id}">
                        <img src="{poster_image_url}" alt="poster" class="poster"/>
                    </a>
                </div>
                <div class="details-wrapper">
                    <h3 class="movie-title">{movie_title}</h3>
                    <span class="certification">{movie_rating}</span>
                    <table class="movie-details-table">
                        <tr>
                            <td class="row-name"><b>Release:</b></td>
                            <td class="row-value">{movie_release_date}</td>
                        </tr>
                        <tr>
                            <td class="row-name"><b>Director:</b></td>
                            <td class="row-value">{movie_director}</td>
                        </tr>
                        <tr>
                            <td class="row-name"><b>Genre:</b></td>
                            <td class="row-value">{movie_genre}</td>
                        </tr>
                        <tr>
                            <td class="row-name"><b>Language:</b></td>
                            <td class="row-value">{movie_language}</td>
                        </tr>
                        <tr>
                            <td class="row-name"><b>Duration:</b></td>
                            <td class="row-value">{movie_duration} minutes</td>
                        </tr>
                    </table>
                    <div class="action-center">
                        <a class="action-btn showTrailer" data-toggle='modal' data-target='#trailer' data-dismiss='modal' data-trailer-youtube-id="{trailer_youtube_id}">
                        <span class="glyphicon glyphicon-play-circle" aria-hidden="true"></span> Watch Trailer</a>
                    </div>
                </div>
            </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_release_date=movie.release_date,
            movie_director=movie.director,
            movie_rating=movie.rating,
            movie_genre=movie.genre,
            movie_language=movie.language,
            movie_duration=movie.duration
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('trailer_library.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)