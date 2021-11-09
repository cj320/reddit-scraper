# :zap: Reddit Scraper

This script will allow one to scrape images from a Reddit subreddit
using the The Python Reddit API wrapper. It is a work in progress,
and will more options beyond pulling images as I continue development work. 

## :bulb: Instructions

To successfully use this script to pull images you will need to do the following:

1. Log into your Reddit account.
2. Click the down arrow to the right of your name, then click the Preferences button.
3. Click the app tab.
4. Populate your script with the required fields. Refer to the screen shot below:

![REGISTER-APPLICATION](docs/images/register_application.png)


5. Use the [*secrets-json*](secrets.json) to populate the following fields:
   * client_id
   * client_secret
   * user_agent (AKA the name of the app)

6. user the [*refreshtoken.py](refreshtoken.py) script to obtain a refresh token, and append it to the refresh_token key, in the secrets.json
7. Hide the secret.json file by renaming the file to *.secrets.json*

8.  import all of the Python libraries contained in the requirements.txt file, the [*reddit_pkg*](reddit_pkg/) directory.

## :bulb: Running the script:

The script can be run using by running the main.py script.
It will ask the user to enter the name of the subbreddit, validate that it exists, then pull the top 10 images from *hot* category if 
it contains a valid image file name.