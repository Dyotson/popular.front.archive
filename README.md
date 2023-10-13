# Popular Front Archive

## About

Popular Front Archive is a webapp developed with Django, it uses a packaged called [Instaloader](https://instaloader.github.io/) to download Instagram posts and stories of Popular Front. The app is hosted on [Render](https://render.com/) and uses [PostgreSQL](https://www.postgresql.org/) as a database. It uses [Cron-Job](https://console.cron-job.org) to run the `get_post` view every 5 minutes.

In theory, this webapp could be used with any Instagram account, but it was developed with Popular Front in mind.

## Installation

### Requirements

To install all requirements, install Poetry and run `poetry install` in the root directory of the project. Then, you can use Poetry to run the app with `poetry run python manage.py runserver`.

In other side, please create a `.env` file in the root directory of the project with the following variables:

- `SECRET_KEY`: The secret key of the Django app.

Remember that DEBUG comes set to `True` by default, so you should change it to `False` in production.

## Docs

### Views (in `views.py`)

- `index`: The main page of the webapp, it shows the latest posts and stories.
- `get_post`: Downloads the latest posts from Instagram and saves them to the database. It's important to note that this view needs a GET request with the key of the API, otherwise it will return a 404 error. Here you can change the Instagram account that the app will download from.

### Models (in `models.py`)

- `Post`: Stores the data of a post. The things that saves are:
  - `code`: a CharField with a maximum length of 100 characters, which will store a unique code for the post.
  - `content`: a TextField that will store the main content of the post.
  - `image`: a TextField that will store the URL of an image associated with the post.
  - `created_at`: a DateTimeField that will store the date and time when the post was created. This field will be automatically set to the - current date and time when a new post is created.
  - `published_at`: a DateTimeField that will store the date and time when the post was published. This field can be set to null=True to allow for posts that have not yet been published.


### Templates (in `templates/`)

- `head.html`: The base template of the webapp, it contains the navbar and the header.
- `index.html`: The main page of the webapp, it shows the latest posts and stories.
- `about.html`: The about page of the webapp, it shows information about the project.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.