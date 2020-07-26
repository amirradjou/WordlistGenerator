def generator(comb, dic, temp, mf):
    if comb == 0:
        mf.write(temp + ',' + '\n')
    else:
        for item in dic:
            generator(comb - 1, dic, temp + item, mf)


print("Please enter filegname!")
file_name = input()
print('Please enter combination times!')
comb_time = input()
print("Please enter words for creating your word list")
print('Enter \'-\' when it is Done ')

s = []
word = ''
while True:
    word = input()
    if word == '-':
        break
    s.append(word)

file = open(file_name + '.txt', 'w')

generator(int(comb_time), s, '', file)

print("Your csv file generated!")
