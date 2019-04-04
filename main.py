from __future__ import print_function
from chatbot_util import Chat, reflections

pairs = (

    (r'name (.*)',
   ('Hello##username##! type your question.. or type help',
   'Hey there##username##! type your question.. or type help for options')),

  (r'(\bwhat|\bwhich|\bhow|\bwho|\bhow|\bwhat\'s|\bwhich|\'s\bhow\'s|\bwho\'s|\bhow\'s) (.*)',
   ('Ok ##username##! Let me think ... \n Cool! your sql statment is: \n\n ##sql_statment## \n\n ##sql_result##',
   'Cool! your sql statment is: \n\n ##sql_statment## \n\n.. hmm here is the result for that: \n\n ##sql_result##')),

 (r'help',
  ( "You can ask me questions like:"
        "\n\t * What are the countries in Africa?"
        "\n\t * What is the average population of all the cities?"
        "\n\t * Who is the leader of the country Argentina"
        "\n\t * What is the capital of the country Zimbabwe?"
        "\n\t * And many other questions that I could answer based on my knowledge!!"
        )),

  (r'quit',
  ( "Thank you for talking with me##username##.",
    "Good-bye##username##.",
    "Thank you, Have a good day!")),

  (r'(.*)',
  ( "##username## I didn\'t understand! Please ask a question!",
    "##username## That seems off topic. Please ask a question with which, what, who or how.",
    "I see, I don\'t have that in my database, can you make sure to use the correct format as directed."))
)

form_chat = Chat(pairs, reflections)

def form_chatbot():
    form_chat.converse()


def demo():
  form_chatbot()


if __name__ == "__main__":
    demo()