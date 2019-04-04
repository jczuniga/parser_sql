from nltk import load_parser, grammar, parse
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import logging
import time
import re
import sys

file_handler = logging.FileHandler(filename='parser_sql.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(name)s: %(levelname)s : %(message)s',
                    handlers=handlers
                    )

log = logging.getLogger(__name__)

supported_questions_str_list = ['what','which','who','where', 'how']
sen_words = ['between', 'not', 'do']

stop_words = set(stopwords.words("english"))

parser_grammar = 'grammar/sql.fcfg'

# Method for tokenizing the queries and eliminating stop words
def parse_sentence(parser_grammar, sent, trace = 0):
    try:
        if is_question(sent) < 1:
            return Exception("Only one questions is allowed. Questions should start with ",
                            supported_questions_str_list)
        sent = senitize_question(sent)
        words = word_tokenize(sent)
        remove_digit = [w for w in words if not w.isdigit()]
        sent = ' '.join([w for w in remove_digit if not w in stop_words 
                        or w in supported_questions_str_list 
                        or w in sen_words
                        ])
        parser = load_parser(parser_grammar, trace)
        parser_trees = list(parser.parse(sent.split()))
        answer = parser_trees[0].label()['SEM']
        answer = [s for s in answer if s]
        answer_str = ' '.join(answer)
        return answer_str
    except IndexError as e:
        log.error('Cannot find string match from grammar. Error: {}'.format(e))
        return 0
    except ValueError as e:
        log.error('Input words not found in grammar. Error: {}'.format(e))
        return 0

def get_digits_from_query(sent):
    try:
        sent = senitize_question(sent)
        tokenized = word_tokenize(sent)
        digits = [int(d) for d in tokenized if d.isdigit()]
        return digits
    except ValueError as e:
        log.info('Failed to get digits/numbers from query. Error: {}'.format(e))
        return None

def senitize_question(sent):
    sent = sent.replace('?', '').replace("\'s","").replace("\'re","").replace("\n't"," not ").replace(',', ' ')
    return sent

# Method for ensuring that only one question is entered per query 
def is_question(sent):
    words = word_tokenize(sent)
    is_q = [w for w in words if w.lower() in supported_questions_str_list ]
    number_of_questions = len(is_q)
    if number_of_questions < 1: 
        return -1 # means that query is not part of the supported questions
    elif number_of_questions > 1: # More than one question
        return 0
    return 1  


# Method that gets/scans user query from terminal
def get_query():
    try:
        user_query = raw_input("[SQL_DB] [world.db] [root] Enter your query: ")
    except NameError:
        user_query = input("[SQL_DB] [world.db] [root] Enter your query: ")

    return str(user_query)

# Main

def parse_query(query, *args, **kwargs):
    output = ""
    parsed = parse_sentence(parser_grammar, query)
    parsed = re.sub(r"\) \(", "), (", parsed)
    digits = get_digits_from_query(query)
    if digits is not None:
        if len(digits) > 1:
            dig = tuple(digits)
            str_dig = str(dig)
            output = parsed + " " + str_dig + ";"
        elif len(digits) == 1:
            for d in digits:
                str_dig = "{}".format(d)
                output = parsed + " " + str_dig + ";"
        else:
            output = parsed + ";"

    return output


def show_parse_tree(input, trace=0):
    sent = senitize_question(input)
    words = word_tokenize(sent)
    remove_digit = [w for w in words if not w.isdigit()]
    sent = ' '.join([w for w in remove_digit if not w in stop_words 
                        or w in supported_questions_str_list 
                        or w in sen_words])
    parser = load_parser(parser_grammar, trace=1)
    parser_trees = list(parser.parse(sent.split()))
    for tree in parser_trees:
        log.info(tree)


def main():
    user_input = get_query()
    print 'Converting input to MySQL query...'
    time.sleep(3)
    get_parse = parse_query(user_input)
    print "Result: {}".format(get_parse)
    time.sleep(3)
    print 'Generating parse tree...'
    time.sleep(3)
    try:
        show_parse_tree(parser_grammar, user_input)
    except ValueError as e:
        log.error("Could not generate parse tree. Error: {}".format(e))

if __name__ == '__main__':
    main()



