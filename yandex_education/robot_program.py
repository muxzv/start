def is_num(s):
    if len(s) == 0:
        return False
    return s.isdigit()

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
    if 'move_right' in s:
        return 'R', get_command_param(s)
    elif 'move_left' in s:
        return 'L', get_command_param(s)
    elif 'move_down' in s:
        return 'D', get_command_param(s)
    elif 'move_up' in s:
        return 'U', get_command_param(s)
    elif 'for' in s:
        return 'F', get_command_param(s)
    else:
        return None

def command_in_cycle(s):
    return len(s) > 0 and (s[0]==' ' or s[0]=='\t')

def run_command(x, y, cmd):
    c, p = cmd[0], cmd[1]
    if c == 'R':
        return x + p, y
    elif c == 'L':
        return x - p, y
    elif c == 'D':
        return x, y - p
    elif c == 'U':
        return x, y + p

def print_res(c, p):
    s = c + '('
    if p > 1:
        s += str(p)
    print(s + ')')
    
def run_commands(x, y, commands, n):
    #print(commands)
    for i in range(n):
        for c in commands:
            if type(c[1]) == str:
                c1 = c[0], i
                x, y = run_command(x, y, c1)
            else:
                x, y = run_command(x, y, c)
    return x, y

x_start, y_start = 0, 0
x, y = x_start, y_start

in_cycle = False

while True:
    s = input()
    
    if len(s) == 0:
        continue
    
    if s[0] == '#':
        break
    
    cmd = get_command(s)
    
    if cmd is None:
        continue
    
    if cmd[0] == 'F':
        cycle_n = cmd[1]
        in_cycle = True
        cycle_commands = []
        continue
    
    if in_cycle:
        if command_in_cycle(s):
            cycle_commands.append(cmd)
        else:
            x, y = run_commands(x, y, cycle_commands, cycle_n)
            in_cycle = False
            
    if not in_cycle:
        x, y = run_command(x, y, cmd)
    
    #print(s, cmd, x, y)

if in_cycle:
    x, y = run_commands(x, y, cycle_commands, cycle_n)
    
move_x = x - x_start
move_y = y - y_start

print(move_x, move_y)

if move_x != 0 or move_y != 0:
    if move_x > 0:
        print_res('move_right', move_x)
    elif move_x < 0:
        print_res('move_left', -move_x)
        
    if move_y > 0:
        print_res('move_up', move_y)
    elif move_y < 0:
        print_res('move_down', -move_y)
