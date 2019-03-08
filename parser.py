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

supported_questions_str_list = ['what','which','who','where']
sen_words = ['between', 'not', 'do']

stop_words = set(stopwords.words("english"))

parser_grammar = 'grammar/sql_grammar.fcfg'

# Method for tokenizing the queries and eliminating stop words
def parse_sentence(parser_grammar, sent, trace = 0):
    try:
        if is_question(sent) < 1:
            return Exception("Only one questions is allowed. Questions should start with ",
                            supported_questions_str_list)
        sent = senitize_question(sent)
        words = word_tokenize(sent)
        sent = ' '.join([w for w in words if not w in stop_words 
                        or w in supported_questions_str_list 
                        or w in sen_words])
        parser = load_parser(parser_grammar, trace)
        parser_trees = list(parser.parse(sent.split()))
        answer = parser_trees[0].label()['SEM']
        answer = [s for s in answer if s ]
        answer_str = ' '.join(answer)
    except IndexError as e:
        log.error('Cannot find string match from grammar. Error: {}'.format(e))
        raise e('String match error')

    return answer_str

def senitize_question(sent):
    sent = sent.replace('?', '').replace("\'s","").replace("\'re","").replace("\n't"," not ")
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

# Method that onverts parse trees created from grammar to SQL statements
def organize_sql_statment(sent):
    try:
        sent = sent.replace(" (","(") 
    except ValueError as e:
        raise e
    qq = re.split("(BREAK_S | BREAK_F | BREAK_W)", sent)

    sen_s = 'SELECT '
    sen_f = 'FROM '
    sen_w = 'WHERE '
    bool_w = False # To check if there is a where clause or not
    
    for item in qq:
        if 'select' in item.lower():
            sen_s += item.lower().replace('select','')+', '
        elif 'from' in item.lower():
            sen_f += str(item.lower().replace('from',''))+', '
        elif 'where' in item.lower():
            bool_w = True
            sen_w += str(item.lower().replace('where',''))+' and '
    if bool_w:
        sql_query = sen_s[:-2]+' '+sen_f[:-2]+' '+sen_w[:-4]
        if 'TMP_1'.lower() in sql_query.lower():
            sql_query = sql_query.replace('TMP_1'.lower(), filter(None, sen_f.split(' '))[1].replace(',','') )
    else:
        sql_query = sen_s[:-2]+' '+sen_f[:-2]
    if 'max' in sql_query.lower():
        tmp = re.split('(\(|\))', sql_query)
        value = tmp[2]
        tmp = tmp[0] +''+tmp[-1]
        if ',' in tmp:
            comma = ','
        else:
            comma = ''
        sql_query = tmp.lower().replace('max', value+comma) + ' order by '+value+' DESC limit 1'
    if 'min' in sql_query.lower():
        tmp = re.split('(\(|\))', sql_query)
        value = tmp[2]
        tmp = tmp[0] +''+tmp[-1]
        if ',' in tmp:
            comma = ','
        else:
            comma = ''
        sql_query = tmp.lower().replace('min', value+comma)+ ' order by '+value+' ASC limit 1'

    return sql_query


# Method that gets/scans user query from terminal
def get_query():
    try:
        user_query = raw_input("[SQL_DB] [world.db] [root] Enter your query: ")
    except NameError:
        user_query = input("[SQL_DB] [world.db] [root] Enter your query: ")

    return str(user_query)

# Main

def parse_query(query, *args, **kwargs):
    try:
        parsed = parse_sentence(parser_grammar, query)
        output = organize_sql_statment(parsed)
    except Exception as e:
        print 'Error in converting input to SQL query. ERROR: {}'.format(e)
        log.error('SQL Parsing error')
        raise e
    return output

def show_parse_tree(grammar, input, trace=0):
    sent = senitize_question(input)
    words = word_tokenize(sent)
    sent = ' '.join([w for w in words if not w in stop_words 
                        or w in supported_questions_str_list 
                        or w in sen_words])
    parser = load_parser(grammar, trace=1)
    parser_trees = list(parser.parse(sent.split()))
    for tree in parser_trees:
        print tree


def main():
    user_input = get_query()
    print 'Converting input to MySQL query...'
    time.sleep(3)
    get_parse = parse_query(user_input)
    print "Result: {}".format(get_parse)
    parsed = parse_sentence(parser_grammar, user_input)
    time.sleep(3)
    print 'Generating parse tree...'
    show_parse_tree(parser_grammar, user_input)


if __name__ == '__main__':
    main()



