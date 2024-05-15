def reverse(seq):
    
    n = len(seq)
    for x in range(n//2):
        seq[x], seq[n - x - 1] = seq[n - x - 1], seq[x] 

    return seq
if __name__ == "__main__":
    seq = ['?', 'you', 'are', 'how', 'world', 'hello']
    print(reverse(seq))