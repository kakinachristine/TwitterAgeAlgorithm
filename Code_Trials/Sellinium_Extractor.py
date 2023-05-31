from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the search input field to be visible



# # Create a new instance of the Firefox driver
# driver = webdriver.Firefox(executable_path='C:/Program Files/geckodriver.exe')
# Specify the path to geckodriver
geckodriver_path = 'C:/Program Files/geckodriver.exe'

# Create a service object with the geckodriver path
service = Service(geckodriver_path)

# Create a new instance of the Firefox driver using the service
driver = webdriver.Firefox(service=service)

# Function to scrape tweet and user details
def scrape_tweet_and_user_details(query, count, csv_filename):
    # Open CSV file for writing
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Bio', 'Location', 'Followers Count', 'Friends Count', 'Tweet Content'])

        # Navigate to Twitter
        driver.get("https://twitter.com/")

        # Wait for the page to load
        time.sleep(3)

        # Find the search input field
        wait = WebDriverWait(driver, 10)
        # Create a WebDriverWait instance with the desired timeout
        wait = WebDriverWait(driver, timeout=30)

        # Wait for the search input element to be clickable
        search_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')))

        # search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')), timeout=30)

        # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
        # # Switch to iframe if necessary
        # driver.switch_to.frame('iframe_name_or_id')
        #
        # # Locate the search input element
        # search_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')

        # Switch back to the default content
        driver.switch_to.default_content()

        # Enter the query in the search input field
        search_input.send_keys(query)

        # search_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')

        # Enter the query and press Enter to search
        # search_input.send_keys(query)
        # search_input.send_keys(Keys.ENTER)

        # Wait for the search results to load
        time.sleep(3)

        # Scroll down to load more tweets
        body = driver.find_element_by_tag_name("body")
        for _ in range(count // 10):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)

        # Find the tweets and extract details
        tweets = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        for tweet in tweets:
            username_element = tweet.find_element_by_xpath('.//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')
            username = username_element.text

            bio_element = tweet.find_element_by_xpath('.//div[@class="css-1dbjc4n r-156q2ks"]')
            bio = bio_element.text

            location_element = tweet.find_element_by_xpath('.//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]')
            location = location_element.text

            followers_count_element = tweet.find_element_by_xpath('.//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]')
            followers_count = followers_count_element.text

            friends_count_element = tweet.find_element_by_xpath('.//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]')
            friends_count = friends_count_element.text

            tweet_content_element = tweet.find_element_by_xpath('.//div[@class="css-1dbjc4n r-156q2ks"]')
            tweet_content = tweet_content_element.text

            # Write details to the CSV file
            writer.writerow([username, bio, location, followers_count, friends_count, tweet_content])

# Search query for friendships
friendship_query = 'relationships with loved ones OR friends OR friendship OR best friends OR bffs OR ' \
                   'friends forever OR friendship goals OR true friends OR friendship quotes OR friendship day OR ' \
                   'squad goals'

# Scrape tweets for friendships
scrape_tweet_and_user_details(friendship_query, 15000, '../friendship_tweets.csv')

# Search query for love
love_query = 'relationships with loved ones OR dating OR breakups OR relationship milestones OR love languages OR ' \
             'relationship goals OR online dating OR LGBTQ+ relationships OR relationship advice OR relationship ' \
             'humor OR intimacy and romance OR relationship self-care OR relationship red flags OR love OR romance ' \
             'OR couple goals OR soulmate OR true love OR relationship goals OR happy couple OR love quotes OR ' \
             'love story'

# Scrape tweets for love
scrape_tweet_and_user_details(love_query, 15000, 'love_tweets.csv')

# Search query for family
family_query = 'relationships with loved ones OR family OR family time OR family love OR family goals OR ' \
               'family first OR family is forever OR family matters OR family bonds OR family memories OR ' \
               'family quotes'

# Scrape tweets for family
scrape_tweet_and_user_details(family_query, 15000, 'family_tweets.csv')

# Close the browser
driver.quit()
