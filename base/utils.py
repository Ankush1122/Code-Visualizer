import subprocess
import select


def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)


def read(process):
    ready, _, _ = select.select([process.stdout], [], [], 0)
    if ready:
        return process.stdout.readline().decode("utf-8").strip()
    else:
        return ""


def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()


def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)

def debug_code():
    f = open("test.py", 'r')
    lines = f.readlines()
    f.close()
    num_lines = len(lines)


    variables = []
    for line in lines:
        if "=" in line:
            var = line.split("=")[0].replace(" ", "")
            if var not in variables:
                variables.append(var)
    print(variables)

    lines = []
    process = start(["python3", "-m", "pdb", "test.py"])


    while True:
        out = read(process)
        if (out == ""):
            break
        print(out)
        lines.append(out)

    break_status = False
    reading = True
    var_values = []

    while reading:
        write(process, "next")

        while True:
            out = read(process)
            if (out == ""):
                break

            print(out)

            if (break_status and '(Pdb)' in out):
                reading = False
                break
            if ("<module>()->None" in out):
                break_status = True
            lines.append(out)

        # temp = {}
        # for var in variables:
        #     write(process, "p " + var)
        #     out = read(process)
        #     if ("NameError" in out):
        #         temp[var] = "Not Defined"
        #     else:
        #         temp[var] = out
        # var_values.append(temp)
    print("3")

    lines[0] = "(Pdb) "+lines[0]

    line_order = []
    split_num = -1


    x = 0
    for line in lines:
        if ("test.py" in line and "Breakpoint" not in line):
            if (split_num == -1):
                split_num = x
            c = line.split("test.py")[1].split(")")[0]
            c = c.replace('(', "")
            line_order.append(int(c))
        x += 1

    if (split_num != -1):
        lines = lines[split_num:]
    print(split_num)

    for line in lines:
        print(line)
    print()
    print()


    outputs = ['']*len(line_order)
    count = 0
    
    for line in lines:
        if ("--Return--" in line):
            break
        if ("test.py" in line and "Breakpoint" not in line):
            count += 1
        if ("(Pdb)" in line and "test.py" not in line):
            c = line.split("(Pdb) ")[1]
            outputs[count] = c

    return {"line_order":line_order, "outputs":outputs}
