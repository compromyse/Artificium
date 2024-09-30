def compute_partitions(max_n):
    partitions = [0] * (max_n + 1)
    partitions[0] = 1
    
    for i in range(1, max_n + 1):
        for j in range(i, max_n + 1):
            partitions[j] += partitions[j - i]
    
    return partitions

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    queries = [int(data[i]) for i in range(1, T + 1)]
    
    max_n = 100
    partitions = compute_partitions(max_n)
    
    results = [str(partitions[n]) for n in queries]
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
