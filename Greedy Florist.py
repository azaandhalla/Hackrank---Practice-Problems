A group of k friends want to buy n flowers where each flower i has some base cost, ci. The florist wants to maximize his number of new customers, so he increases the price of flowers purchased by repeat customers; more precisely, if a customer has already purchased x flowers, the price, p, for flower i is pi= (x + 1) * ci.

Given n, k, and the base cost for each flower, find and print the minimum cost for the group to purchase n flowers.

import sys

n, k = [int(x) for x in input().strip().split(' ')]
c = sorted([int(x) for x in input().strip().split(' ')][:n], reverse=True)
b = []

count = 1
while(count <= n/k):
    b.extend([count] * k)
    count += 1

b.extend([count] * (n % k))
print(sum([x*z for x,z in zip(c,b)]))
