with open('input.txt') as file:
    commands_count = int(file.readline())
    stack_size = int(file.readline())

    for i in range(commands_count):
        line = file.readline().strip().split()
        command = line[0]
        parameter = int(line[1]) if len(line) > 1 else None
        print('("' + command + '", ' + str(parameter) + '), ', end='')
