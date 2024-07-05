import json
import requests
import datetime

import argparse
from pathlib import Path

from newscover.newsapi import fetch_latest_news

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--api_key", required=True, help="your api key")
    parser.add_argument("-b", "--lookback_days", type=int, help="number of days to lookback on")
    parser.add_argument("-i", "--input_file", required=True, help="the input json file containg keywords")
    parser.add_argument("-o", "--output_dir", required=True, help="the directory location of the search results")
    
    args = parser.parse_args()

    # structure: for each key in the dictionary, we go through extraction process
    with open(args.input_file, 'r') as input:
        data = json.load(input)

        # for loop - for each key
        for key in data:
            value = data[key]
            # problem: this returns a json file 
            return_file = fetch_latest_news(args.api_key, value, args.lookback_days)
            
            # create output file as in output directory
            output_dir = Path(__file__).parent / args.output_dir
            output_dir.mkdir(parents=True, exist_ok=True)
            
            filename = key + ".json"
            output_file = Path(__file__).parent / output_dir / filename
            
            write_news_json(return_file, output_file)


# functions only need to create output file path?
def write_news_json(return_file, output_file):
    # write all news to output file 
    with open(output_file, 'w') as f:
        json.dump(return_file,f,indent=4)


if __name__ == "__main__":
    main()

# run as python -m newscover.collector -k 16cdf7eca940497aa59d4d41beadeea7 -b 10 -i input_file.json -o output_dir