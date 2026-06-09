# ask information abt person
#remove whitespace from str always and make everything start from capital
name = input('whats your name? ').strip().title()
age = input('how old are you? ')
status = input('Are you single or in a relationship? ')

def hello(to):
    print('hello ', to )
#check if person filled all the information correctly
hello()
print (", confirm the information ", name , age , status , sep =" :) " )
check = input('I confirm (yes/no): ')
#answer based on answer
if check == 'yes':
        print('thank you for confirmation,we will reach out to you soon ')
elif check == 'no':
        print("please restart")
