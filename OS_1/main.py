A = [20, 30, 10]
B = [40, 20, 10]
C = [10, 30, 20]


def cal_usage_rate(cpu_time, full_time):
    res = cpu_time / full_time
    return '{:.2%}'.format(res)


def cal_full_time(program_1, program_2, program_3):
    return sum(program_1) + sum(program_2) + sum(program_3)


def single(program_1, program_2, program_3):
    full_time = cal_full_time(program_1, program_2, program_3)
    print_full_time = f"CPU:A({program_1[0]})ms " + f"{program_1[1]}ms " + f"A({program_1[2]})ms " + \
                      f"B:({program_2[0]})ms " + f"{program_2[1]}ms " + f"B({program_2[2]})ms " + \
                      f"C({program_3[0]})ms " + f"{program_3[1]}ms " + f"C({program_3[2]})ms"
    print(print_full_time)

    print_io_time = f"IO:{program_1[0]}ms " + f"A({program_1[1]})ms " + f"{program_1[2] + program_2[0]}ms " + \
                    f"B({program_2[1]})ms " + f"{program_1[2] + program_2[0]}ms " + \
                    f"C({program_3[2]})ms"
    print(print_io_time)

    cpu_time = program_1[0] + program_1[2] + program_2[0] + program_2[2] + program_3[0] + program_3[2]

    print(cal_usage_rate(cpu_time, full_time))


def multiple(program_1, program_2, program_3):
    print_full_time = f"CPU:A({program_1[0]})ms " + f"B({program_2[0]})ms " + f"A({program_1[2]})ms " + \
                      f"C({program_3[0]})ms " + f"B({program_2[2]})ms " + f"{program_3[1]}ms " + \
                      f"C({program_3[2]})ms"
    print(print_full_time)

    print_io_time = f"IO:{program_1[0]}ms " + f"A({program_1[1]})ms " + f"{program_1[2]}ms " + \
                    f"B({program_2[1]})ms " + f"C({program_3[1]})ms"
    print(print_io_time)

    cpu_time = program_1[0] + program_1[2] + program_2[0] + program_2[2] + program_3[0] + program_3[2]
    full_time = program_1[0] + program_2[0] + program_1[2] + program_3[0] + program_2[2] + program_3[1] + program_3[2]
    print(cal_usage_rate(cpu_time, full_time))


multiple(A, B, C)
