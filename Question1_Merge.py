  
# Python program for implementation of MergeSort

import time
 
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
 
# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 

arr = [359, 990, 324, 750, 449, 264, 382, 608, 363, 305, 269, 290, 707, 7, 641, 466, 963, 620, 888, 207, 116, 46, 873, 691, 645, 412, 181, 742, 622, 544, 548, 821, 783, 518, 967, 18, 448, 417, 468, 68, 14, 36, 820, 503, 684, 486, 523, 414, 644, 323, 442, 256, 76, 905, 541, 685, 142, 950, 429, 98, 88, 759, 343, 538, 25, 582, 682, 547, 892, 22, 375, 646, 716, 931, 369, 834, 498, 27, 139, 658, 71, 801, 365, 930, 623, 259, 80, 850, 953, 157, 405, 904, 283, 34, 338, 631, 957, 674, 415, 455, 924, 989, 436, 113, 590, 496, 232, 697, 433, 182, 753, 72, 206, 661, 737, 725, 829, 105, 64, 401, 833, 517, 563, 70, 920, 240, 184, 364, 495, 92, 956, 127, 576, 423, 726, 189, 399, 867, 828, 507, 919, 610, 805, 4, 267, 667, 840, 145, 489, 109, 450, 618, 485, 362, 670, 695, 121, 439, 250, 711, 676, 128, 688, 304, 766, 534, 60, 162, 443, 717, 732, 988, 228, 947, 687, 747, 424, 668, 624, 878, 565, 372, 384, 366, 102, 837, 176, 809, 453, 205, 345, 767, 689, 133, 62, 78, 939, 73, 632, 286, 459, 168, 431, 584, 526, 396, 877, 24, 148, 371, 601, 280, 724, 361, 212, 86, 807, 925, 270, 387, 728, 327, 532, 311, 321, 663, 627, 571, 322, 522, 248, 516, 508, 589, 169, 591, 763, 413, 84, 860, 846, 96, 657, 335, 948, 306, 555, 553, 51, 282]

# Time using clock_highres
timeit = time.perf_counter()
mergeSort(arr)

timeit = time.perf_counter() - timeit

print("\nSorted array is ", arr)
print("Time taken for merge sort: ", timeit)
 
# This code is contributed by Mayank Khanna

print(time.get_clock_info('time'))