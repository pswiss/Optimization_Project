import os

# Configure the write location
direct = os.path.dirname(os.path.abspath(__file__))+'\\folder\\'
os.makedirs(direct)

filename = 'hi.txt'

# Start the file
ffile = open(direct+filename,"a")
ffile.write('this is a test')
ffile.close()
