import time

start = time.perf_counter()

for _ in range(1000):

    model(x)

end = time.perf_counter()

latency = (
    end-start
)/1000
