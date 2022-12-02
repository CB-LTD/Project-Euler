import time
# Runtime: --- 0.0039637088775634766 seconds ---

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Question 1:
# Find the sum of all the multiples of 3 or 5 below 1000.

# This is for timing run time
start_time = time.time()

IntList = []
i = 0

while i < 999:  # 999 as we don't want i to reach 1000.
    i += 1

    if i % 3 == 0:
        IntList.append(i)
    elif i % 5 == 0:
        IntList.append(i)

# print(IntList)
answer  = sum(IntList)

print('Answer to part 1:', answer)

print("--- %s seconds ---" % (time.time() - start_time))