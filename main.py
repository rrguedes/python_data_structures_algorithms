import time

fishes = ["nemo" for nemo in range(10000)]


def find_nemo(fishes):
    for fish in fishes:
        if fish == "nemo":
            print("I've found Nemo")


if __name__ == "__main__":
    t0 = time.perf_counter()
    find_nemo(fishes)
    elapsed_time = time.perf_counter() - t0
    print("Elapsed time {:0.6f}".format(elapsed_time))
