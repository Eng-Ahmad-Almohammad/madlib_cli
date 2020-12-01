import re

def welcome():
    print('Welcom to madlib ')
    print('*****************************************')
    print('**    Welcome to the Snakes Cafe!      **')
    print('** Please answer all questions below   **')
    print('**                                     **')
    print('**   You will get a funny sentence     **')
    print('*****************************************')

    first_adjective = input('Please input an Adjective ')
    second_adjective= input('Please input a new Adjective ')
    first_name = input('Please input A First Name ')
    past_tense_verb = input('Please input Past Tense Verb ')
    second_name = input('Please input A First Name ')
    third_adjective = input('Please input an Adjective ')
    fourth_adjective= input('Please input a new Adjective ')
    plural_noun = input('Please input a Plural Noun ')
    anwers= [first_adjective,second_adjective, first_name, past_tense_verb, second_name, third_adjective, fourth_adjective, plural_noun ]
    return anwers

def read_template():
     with open('assetes/madlib.txt','r') as f:
        content= f.read().strip()
     return content

print(read_template())

def parse(string):
    data = re.findall(r"\{(.*?)\}",string)
    j = 0
    for i in data:
        
        string = string.replace(i,f'{j}',1)
        j +=1

    return string


def merge(string):
    reslut = string.format(*welcome())
    with open('assetes/userIn.txt','w') as f:
        content = f.write(reslut)
    return reslut

if __name__ == "__main__":
    
    print(merge(parse(read_template())))






