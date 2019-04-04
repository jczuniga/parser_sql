from nltk import load_parser, grammar, parse
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import sys
import parser
import time, sys
import logging
from sql_connect import DB

file_handler = logging.FileHandler(filename='test.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(name)s: %(levelname)s : %(message)s',
                    handlers=handlers
                    )

log = logging.getLogger(__name__)

log = logging.getLogger(__name__)
database = DB()
user_query = parser.get_query()
query = parser.parse_query(user_query)
time.sleep(2)
log.info("Converting input to MySQL query....")
time.sleep(3)
log.info("Result: {}".format(query))
time.sleep(3)
log.info("Retrieving results from database...")
time.sleep(3)
result = database.query_pretty(query)
log.info(result)
