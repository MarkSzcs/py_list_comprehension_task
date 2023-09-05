if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    #xs = [x for x in range(0, x+1)]
    #ys = [y for y in range(0, y+1)]
    #zs = [z for z in range(0, z+1)]
    
    #equals_n = [[x, y, z] for x in range(0, x+1) for y in range(0, y+1) for z in range(0, z+1) if x + y + z == n]
    noteq_n = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b + c != n]
    print(noteq_n)
