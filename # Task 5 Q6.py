# Task 5 Q6

f = open('sample.txt', 'w')
f.write('Hello I am a file\n')
f.write('where you need to return the data\n')
f.write('which is of even length\n')
f.write('make sure you return the contect in the same link\n')
f.close()    


f = open('sample.txt', 'r')
f.readline()         
'Hello I am a file\n'
f.readlines()        
['where you need to return the data\n', 'which is of even length\n', 'make sure you return the contect in the same link\n']
f.readline()        
''
f.close()


f = open('sample.txt', 'r')
f.read()              
'Hello I am a file\nwhere you need to return the data\nwhich is of even length\nmake sure you return the contect in the same link\n'
f.close()

# Read line-by-line using readline() in a while-loop
f = open('sample.txt')
line = f.readline()   
while line:
        line = line.rstrip()  
       
        print(line)
        line = f.readline()
'''Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present.'''
f.close()