command = input("Enter the windows command: ")
customCMD = input("Enter the custom command: ")
arguments = int(input("Enter the number of arguments: "))

text = '''@START '''
for i in command.split():
    #print(i)
    text = text + '''"''' + i + '''" '''

for i in range(0, arguments):
    text = text + '''"%''' + str(i+1) + '''" '''

print(text)
fileName = customCMD + '.bat'
filePath = "C:\\Windows\\System32\\"
file = open(fileName, 'w')
file.write(text)
file.close()

print("Move folder to ", filePath)