

'''create-express-app.

Usage:
    create-express-app.py (-h | --help)
    create-express-app.py --version
    create-express-app.py check 
    create-express-app.py create <params>


Options:
    -h --help   Show this screen
    --version   Show Version 

'''

def check():
    print("Hello World")

def create(params):
    import os 
    import subprocess
    os.mkdir(params)
    path = './'+params
    os.chdir(path)
    os.system("npm init -y")
    os.system("type nul > app.js")
    os.system("npm i express body-parser")
    os.system("code ..")


from docopt import docopt 

if __name__ == '__main__':
    arguments = docopt(__doc__,version='1.0.0')
    if arguments['check'] == True:
        check()
    elif arguments['create'] == True:
        create(arguments['<params>'])
    
    
        