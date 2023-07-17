def perfect_square(n):
    i = 1
    while(i*i <= n):

        if i*i == n:
            return "True"
        i += 1
    return "false"

n = int(input())
print(perfect_square(n))



