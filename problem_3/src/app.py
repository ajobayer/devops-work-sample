import json
import logging
import boto3
import os
from datetime import datetime
from urllib.request import Request, urlopen

LOGGING_LEVEL = int(os.getenv('LOGGING_LEVEL', logging.INFO))
logging.basicConfig(level = LOGGING_LEVEL)
logger = logging.getLogger()
logger.setLevel(LOGGING_LEVEL)


def website_status_check(url):
    return urlopen(url).getcode()


def lambda_handler(event, context):
    """Website status check from: website-lists.json 

    Parameters
    ----------
    event: dict, required

    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------

    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    logger.debug('## ENVIRONMENT VARIABLES')
    #logger.debug(json.dumps(dict(os.environ)))
    website_lists = os.environ['WEBSITE_LISTS']

    # Read list of wesite urls from json file
    with open(website_lists, 'r') as f:
        urls = json.load(f)

    # check each of the website status
    for url in urls:
        url_link = url['website_url']
        logger.info(f'checking site url {url_link}')
        print('Website: {} Status: {}.............'.format(url_link, website_status_check(url_link)))


