# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0 for i in range(n)]
    smallest_time = 0
    index = 0
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        time = data[i]
        smallest_time = threads[0]
        for j in range(n):
            if threads[j] < smallest_time:
                index = j
                smallest_time = threads[index]
#               print(smallest_time)
#               print(index)
        output.append((index, smallest_time))
        threads[index] = threads[index] + time
#       print(threads)
        index = 0

    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    first_line = list(map(int, input().split()))
    n = first_line[0]
    m = first_line[1]
  
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i,j in result:
        print(i,j)



if __name__ == "__main__":
    main()
