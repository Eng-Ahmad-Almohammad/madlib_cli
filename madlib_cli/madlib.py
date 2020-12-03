import re
answers = []
def welcome():
    print('Welcom to madlib ')
    print('*****************************************')
    print('**    Welcome to the Snakes Cafe!      **')
    print('** Please answer all questions below   **')
    print('**                                     **')
    print('**   You will get a funny sentence     **')
    print('*****************************************')

    

def read_template():
     with open('assetes/madlib.txt','r') as f:
        content= f.read().strip()
     return content



def parse(string):
    """
    If you want to to test parse function you should to comment the lins 31 and 32
    """


    data = re.findall(r"\{(.*?)\}",string)
    j = 0
    
    for i in data:
        # user_data= input(f'Please add a/an {i} ')
        # answers.append(user_data)
        string = string.replace(i,f'{j}',1).strip()
        j +=1

    return string


def merge(string):
    reslut = string.format(*answers)
    with open('assetes/userIn.txt','w') as f:
        content = f.write(reslut)
    return reslut

if __name__ == "__main__":
    welcome()
    print(merge(parse(read_template())))
    print(answers)






