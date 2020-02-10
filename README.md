# Pitch

## Author

[Chepkirui Betty](https://github.com/chepkiruibetty)

# Description

This is an application that allows users to sign in or sign up and post one minute pitches.It also allows the to upvote and downvote on different pitches.

## User Story

- Comment on the different pitches posted py other uses.
- See the pitches posted by other uses.
- Vote on s pitch they have viwed by giving it a upvote or a downvote.
- Register to be allowed to log in to the application
- View pitches from the different categories.
- Submit a pitch to a specific category of their choice.

## BDD

| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                               Get all posts, Select between signup and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app pitches based on categories and commenting section |
| Select comment button |             **Comment**             |                                             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |

## Development Installation

To get the code..

1. Cloning the repository:

```bash
https://github.com/chepkiruibetty/blog-post
```

2. Move to the folder and install requirements

```bash
cd pitcher
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3.6 app.py server
```

Open the application on your browser `127.0.0.1:5000`.

## Technology used

- [Python3.6](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Heroku](https://heroku.com)

## Contact Information

chepkiruibetty@gmail.com

## Live Link To Project

https://instantpitch.herokuapp.com/


## codebeat

### codebeat

[![codebeat badge](https://codebeat.co/badges/9f12d78d-24b2-47bd-9967-0e909c237bd7)](https://codebeat.co/projects/github-com-chepkiruibetty-pitch-master)

## License
 
 Licensed under[MIT license](license)


