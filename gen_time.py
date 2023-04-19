def gen_time(start: tuple, end: tuple, step: tuple):
    current_time = list(start)
    while True:
        if current_time[0] >= end[0]:
            if current_time[1] >= end[1]:
                if current_time[2] >= end[2]:
                    break

        for idx, time in enumerate(step):
            current_time[idx] += step[idx]

        if current_time[2] >= 60:
            current_time[1] += current_time[2] // 60
            current_time[2] %= 60

        if current_time[1] >= 60:
            current_time[0] += current_time[1] // 60
            current_time[1] %= 60

        if current_time[0] > 23:
            current_time[0] = 0

        yield tuple(current_time)

if __name__ == "__main__":
    iterable = gen_time((10, 30, 0), (13, 15, 0), (0, 13, 21))
    time = iter(iterable)
    for x in time:
        print(x)
        

