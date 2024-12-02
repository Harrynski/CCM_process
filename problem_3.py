import random
def main(N):
    rain, dry = 0, 0
    for _ in range(N):
        is_lie1 = random.randint(1, 3) == 1
        is_lie2 = random.randint(1, 3) == 1
        is_lie3 = random.randint(1, 3) == 1
        if sum([is_lie1, is_lie2, is_lie3]) == 0:
            rain += 1
        elif sum([is_lie1, is_lie2, is_lie3]) == 3:
            dry += 1
    return(rain / (rain + dry))

trials = [10,100,100000,1000000]    

for N in trials:
    print(N, "      :        ", main(N))