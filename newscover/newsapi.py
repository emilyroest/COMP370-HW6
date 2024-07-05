import json
import requests
import datetime

# queries the NewsAPI and returns a python list of english news articles (represented as dictionaries)
# containing these keywords and published within the last lookback_days (default 10)

# language is english - placed in template
NEWS_QUERY_STRING_TEMPLATE = "https://newsapi.org/v2/everything?q={}&from{}&to={}&language=en&apiKey={}"

# my api key is 16cdf7eca940497aa59d4d41beadeea7
def fetch_latest_news(api_key, news_keywords, lookback_days=10):

    # check type to concatenate
    if type(news_keywords) is list:
        separator = "+"
        news_keywords = separator.join(news_keywords)
    
    if type(news_keywords) is str:
        news_keywords = news_keywords.replace(" ", "+")
    
    # verify non-alphanumeric characters - doing this because of the "+"
    num_check = news_keywords
    news_keywords = news_keywords.replace("+","")
    
    if news_keywords.isalnum() == False:
        raise Exception("Keywords contain non-alphanumeric character(s). Please try again")
    
    news_keywords = num_check
    
    # set up placeholder values
    to_date = datetime.date.today()
    from_date = to_date - datetime.timedelta(days=lookback_days)
    
    # insert placeholders
    query_string = NEWS_QUERY_STRING_TEMPLATE.format(news_keywords, from_date, to_date, api_key)
    
    # call the requests
    response = requests.get(query_string)

    # ensure no errors
    if response.status_code != 200:
        raise Exception("Unable to fetch news articles. Please verify parameters")

    return response.json()

# test function - see if it writes properly
def write_news(api_key, news_keywords, json_file, lookback_days=10):
    news = fetch_latest_news(api_key, news_keywords, lookback_days)
    
    # write all news to output file 
    with open(json_file, 'w') as f:
        json.dump(news,f,indent=4)


if __name__ == '__main__':
    #fetch_latest_news("16cdf7eca940497aa59d4d41beadeea7", "Taylor Swift")
    write_news("16cdf7eca940497aa59d4d41beadeea7", "Donald Trump", "news_test.json")