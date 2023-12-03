import time

def main():

    def stopwatch(n):
        start_time = time.time()
        time.sleep(n)
        stop_time = time.time()
        cur_time = stop_time - start_time
        print(cur_time)
    
    n = int(input("Input wait time: "))
    stopwatch(n)
main()