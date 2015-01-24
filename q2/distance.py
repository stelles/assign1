

def distance(target, source, insertcost, deletecost, replacecost):
    n = len(target) + 1
    m = len(source) + 1

    #set up dist and initialize values

    dist = [[ 0 for j in range(m)] for i in range(n)]

    for i in range(1,n):
        dist[i][0] = dist[i-1][0] + insertcost

    for j in range(1,m):
        dist[0][j] = dist[0][j-1] + deletecost

    #align source and target strings

    line1 = ""
    line2 = ""
    line3 = ""

    for j in range(1,m):
        for i in range(1,n):
            insertions = insertcost + dist[i-1][j]
            deletions = deletecost + dist[i][j-1]
            if (source[j-1] == target[i-1]): 
                add = 0
            else:
                add = replacecost
            substcost = add + dist[i-1][j-1]
            dist[i][j] = min(insertions, deletions, substcost)


    i = len(target)
    j = len(source)
    mn = dist[i][j]
    while i > 0 and j > 0:
        delete = dist[i][j-1]
        insert = dist[i-1][j]
        sub = dist[i-1][j-1]
        mn = min(insert, delete, sub)

        if insert == mn:
            line1 += target[i-1]
            line2 += " "
            line3 += "_"
            i -= 1
        elif delete == mn:
            line1 += "_"
            line2 += " "
            line3 += source[j-1]
            j -= 1
        else:
            if sub == dist[i][j]:
                line2 += "|"
            else:
                line2 += " "
            
            line1 += target[i-1]
            line3 += source[j-1]
            i-=1
            j-=1
    
    print (line1[::-1])
    print (line2[::-1])
    print (line3[::-1])
    print ("Levenshtein distance = " + str(dist[n-1][m-1]))

if __name__=="__main__":
    from sys import argv
    
    if len(argv) > 2:
        distance(argv[1], argv[2], 1, 1, 2)




