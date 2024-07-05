import json
import requests
import datetime
import unittest

from newscover.newsapi import fetch_latest_news

# test A: No Keywords
class FetchLatestNewsTestsNoKeywords(unittest.TestCase):
    
    # test 1: fetch_latest_news fails when no keywords are provided
    def test_no_keywords1(self):
        api_key = "16cdf7eca940497aa59d4d41beadeea7"
        news_keywords = ""
        with self.assertRaises(Exception): 
            fetch_latest_news(api_key, news_keywords)
    
    # test 2: fetch_latest_names passes when keywords are provided
    def test_no_keywords2(self):
        api_key = "16cdf7eca940497aa59d4d41beadeea7"
        news_keywords = ""
        with self.assertRaises(Exception): 
            fetch_latest_news(api_key, news_keywords)

# test B: when lookback days is set that it doesn't produce articles outside this timeframe
class FetchLatestNewsTestsLookbackDays(unittest.TestCase):
    # test 1: lookback days is set
    def test_lookback_days1(self):
        api_key = "16cdf7eca940497aa59d4d41beadeea7"
        news_keywords = "Taylor Swift"
        lookback_days = 7
    
    # test 2: lookback days not set
    def test_lookback_days1(self):
        api_key = "16cdf7eca940497aa59d4d41beadeea7"
        news_keywords = "Travis Kelce"
        lookback_days = 5

# test C: fetch_latest_news fails when a keyword contains a non-alphanumeric character
class FetchLatestNewsTestsNonAlphanumericKeywords(unittest.TestCase):
    # test 1: assert exception 
    def test_non_alphanumeric_keyword1(self):
        api_key = "16cdf7eca940497aa59d4d41beadeea7"
        news_keywords = "m&m!"
        with self.assertRaises(Exception): 
            fetch_latest_news(api_key, news_keywords)
    
    # test 2: assert exception
    def test_non_alphanumeric_keyword2(self):
        api_key = "16cdf7eca940497aa59d4d41beadeea7"
        news_keywords = ":)"
        with self.assertRaises(Exception): 
            fetch_latest_news(api_key, news_keywords)

if __name__ == "__main__":
    unittest.main()

