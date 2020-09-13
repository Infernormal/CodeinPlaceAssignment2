import random
NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100
def main():
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM,MAX_RANDOM))
    pass


if __name__ == '__main__':
    main()