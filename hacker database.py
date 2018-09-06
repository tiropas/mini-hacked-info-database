import time
print('Welcome to hacked emails database!');
time.sleep(3);

command = input('What do you like to do today?R/A? \n>>>>>>>_____________________\`-._\n>>>>>>>                     /.-                  ');

print (command);
read_file = open('hacker database.txt','r')
write_file = open('hacker database.txt','a')
if command == 'R':
    print(read_file.read());
    read_file.close();


if command == 'A':
    time.sleep(2);
    email = input('enter the email of your victim \n>>>>>>>_____________________\`-._\n>>>>>>>                     /.-                  ');
    write_file.write('\n \n')
    write_file.write(email)
    time.sleep(2);
    password = input('enter the password of your victim \n>>>>>>>_____________________\`-._\n>>>>>>>                     /.-                  ');
    write_file.write('               ')
    write_file.write(password)
    write_file.close();

print('all done');
    
