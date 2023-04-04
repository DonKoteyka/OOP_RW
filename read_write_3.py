def write_file(string):
    with open('text.txt', 'a') as f:
        f.write(f'{string}\n')
lenght = dict()
file1 = ['1.txt','2.txt','3.txt']
for i in file1:
    with open(i, 'rt') as f:
        lines = list(map(lambda x: x.strip('\n, \t'), f.readlines()))
        lenght[len(lines)] = {'lines': lines, 'file': i}
keys = sorted(lenght)
open('text.txt', 'w')
for key in keys:
    print(lenght[key]['file'])
    print(key)
    for x in lenght[key]['lines']:
        print(x)
    write_file(lenght[key]['file'])
    write_file(key)
    for x in lenght[key]['lines']:
        write_file(x)

