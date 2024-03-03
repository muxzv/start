def is_num(s):
    if len(s) == 0:
        return False
    return s.isdigit()

def command_in_cycle(s):
    return len(s) > 0 and (s[0]==' ' or s[0]=='\t')

def get_command_param(s):
    i1 = s.index('(')
    i2 = s.index(')')
    if i1 + 1 == i2:
        return 1
    p = s[i1 + 1 : i2]
    if is_num(p):
        return int(p)
    else:
        return p

def get_command(s):
    if len(s) == 0:
        return None
    elif s[0] == '#':
        return 0, '#', 0
    elif 'move_right' in s:
        return command_in_cycle(s), 'R', get_command_param(s)
    elif 'move_left' in s:
        return command_in_cycle(s), 'L', get_command_param(s)
    elif 'move_down' in s:
        return command_in_cycle(s), 'D', get_command_param(s)
    elif 'move_up' in s:
        return command_in_cycle(s), 'U', get_command_param(s)
    elif 'for' in s:
        return command_in_cycle(s), 'F', get_command_param(s)
    else:
        return None

def run_command(x, y, cmd):
    c_name, c_param = cmd[1], cmd[2]
    if c_name == 'R':
        return x + c_param, y
    elif c_name == 'L':
        return x - c_param, y
    elif c_name == 'D':
        return x, y - c_param
    elif c_name == 'U':
        return x, y + c_param

def print_res(c, p):
    s = c + '('
    if p > 1:
        s += str(p)
    print(s + ')')
    
def run_commands(x, y, commands, n):
    #print(commands)
    for i in range(n):
        for c in commands:
            if type(c[2]) == str:
                c1 = c[0], c[1], i
                x, y = run_command(x, y, c1)
            else:
                x, y = run_command(x, y, c)
    return x, y

x_start, y_start = 0, 0
x, y = x_start, y_start

in_cycle = False

while True:
    cmd = get_command(input())
    
    if cmd is None:
        continue
    
    c_in_cycle, c_name, c_param = cmd[0], cmd[1], cmd[2]

    if c_name == '#':
        break
    
    if in_cycle:
        if c_in_cycle:
            cycle_commands.append(cmd)
        else:
            x, y = run_commands(x, y, cycle_commands, cycle_n)
            in_cycle = False
            
    if not in_cycle: # not elif!
        if c_name == 'F':
            cycle_n = c_param
            in_cycle = True
            cycle_commands = []
        else:
            x, y = run_command(x, y, cmd)
    
    #print(s, cmd, x, y)

if in_cycle:
    x, y = run_commands(x, y, cycle_commands, cycle_n)
    
move_x = x - x_start
move_y = y - y_start

#print(move_x, move_y)

if move_x != 0 or move_y != 0:
    if move_x > 0:
        print_res('move_right', move_x)
    elif move_x < 0:
        print_res('move_left', -move_x)
        
    if move_y > 0:
        print_res('move_up', move_y)
    elif move_y < 0:
        print_res('move_down', -move_y)
