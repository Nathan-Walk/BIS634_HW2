
import time
import numpy as np
import multiprocessing as mp

def par_merge(left,right):
    if len(data) <= 1:
        return data
    else:
        split = len(data) // 2
        sorted_left = par_merge(data[:split])
        sorted_right = par_merge(data[split:])
        return (sorted_left, sorted_right)

def merge_sort(data):
    if len(data) <= 0:
        return data
    else:
        split = len(data) // 2
        left = data[:split]
        right = data[split:]
        pool = mp.Pool(processes=4)
        sorted_left, sorted_right = pool.map(par_merge, left, right)

        result = [None] * len(data)
        i = j = k = 0
        l_left, l_right = len(sorted_left), len(sorted_right)
        while k < len(data):
            if i < l_left:
                if j < l_right:
                    if sorted_left[i] < sorted_right[j]:
                        result[k] = sorted_left[i]
                        i += 1
                    else:
                        result[k] = sorted_right[j]
                        j += 1
                else:
                    result[k] = sorted_left[i]
                    i += 1
            else:
                result[k] = sorted_right[j]
                j += 1
            k += 1
        return result

# def lorenz(n=1000000, sigma=10, rho=28, beta=8/3, dt=0.01, x=1, y=1, z=1):
#     state = np.array([x, y, z], dtype=float)
#     for _ in range(n):
#         x, y, z = state
#         state += dt * np.array([sigma*(y-x), x*(rho-z), x*y-beta*z])
#         yield state[0] + 30

if __name__ == "__main__":
    #data = list(lorenz())
    data = [2,4,5,1,9,10,87,45,34,98]
    start = time.perf_counter()
    final_data = merge_sort(data)
    end = time.perf_counter()
    elapsed_time=end-start
    print(final_data)
# a = data[10]
# b = data[353237]
# print("The 10th number is {}, and the 353,237th number is: {}".format(a,b))
# print(f"Time elapsed: {elapsed_time}")
