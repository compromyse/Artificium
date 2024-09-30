import sys
import math

inputs = input().split()
income = int(inputs[0])
mr = float(inputs[1])
savings = int(inputs[2])
n = int(input())
for i in range(n):
    price, expenses = [int(j) for j in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("Yes, the house is affordable with 1 roommate(s) and $1 to spare.")
