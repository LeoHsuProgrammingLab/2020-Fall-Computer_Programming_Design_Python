i = 7
def f(arg=i):
 print(arg)
i = 6
f()
#python can fill all the parameters. Meanwhile, without all is accepted可填可不填
def ask_ok(prompt,retries=4,reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?',2)
ask_ok('OK to overwrite the file?',2,'Come on, only yes or no!')