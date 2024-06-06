# Twitter Trending Topics Scraper

This project scrapes the top 5 trending topics from Twitter's "What’s Happening" section using Selenium and ProxyMesh for IP rotation. The scraped data is stored in a MongoDB database. A simple HTML interface is provided to trigger the scraping process and display the results.

## Prerequisites

- Python 3.x
- MongoDB
- WebDriver for your browser (e.g., ChromeDriver)
- ProxyMesh account
- Twitter account

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/kowshik-04/TwitterTrends_using_Selenium-script.git
   cd twitter-trending-scraper
   ```

2. **Install required Python packages:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up MongoDB:**
   - Ensure MongoDB is installed and running on your local machine or server.
   - Update the MongoDB connection URI in the `config.py` file.

4. **Configure ProxyMesh:**
   - Update the ProxyMesh details (username, password, etc.) in the `config.py` file.

5. **Configure Twitter credentials:**
   - Update your Twitter login credentials in the `config.py` file.

## Configuration (`config.py`)

Create a `config.py` file with the following content:

```python
MONGO_URI = "mongodb://localhost:27017/twitter_trends"
PROXYMESH_URL = "http://your_proxymesh_username:your_proxymesh_password@proxy.proxyMesh.com:31280"
TWITTER_USERNAME = "your_twitter_username"
TWITTER_PASSWORD = "your_twitter_password"
```

## Running the Script

1. **Run the Selenium script to scrape trending topics:**
   ```sh
   python twitter_scraper.py
   ```

2. **Start the Flask app for the web interface:**
   ```sh
   python app.py
   ```

## HTML Interface

The HTML page provides a button to run the Selenium script and display the results.

1. **Navigate to the HTML page:**
   Open your web browser and go to `http://localhost:5000`.

2. **Click the button to run the script:**
   - The page will display the top 5 trending topics along with the IP address used for the query.
   - A JSON extract of the record from the MongoDB database will also be displayed.


## Notes

- Ensure that the WebDriver executable (e.g., `chromedriver`) is in your system's PATH.
- ProxyMesh usage might require additional configuration based on your subscription plan and usage limits.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
