sumsquare = 0
for x in range(1, 101):
    sumsquare = sumsquare + x * x


n = 0
for y in range(1, 101):
    n = n + y
squaresum = n * n

ans = squaresum - sumsquare
print(ans)

# oneliner
print(sum(k for k in range(1, 101)) ** 2 - sum(l ** 2 for l in range(1, 101)))