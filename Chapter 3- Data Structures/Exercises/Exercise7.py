Trip = ['Swtizerland', 'Netherlands', 'Japan', 'Canada', 'Finland']
# Original
print(Trip)

# Alphabetical
print(sorted(Trip))

# Reverse
print(sorted(Trip, reverse = True))

# Original
print(Trip)

# Reversed (Not sorted)
Trip.reverse()
print(Trip)

# Reverse (To put back on the original pattern)
Trip.reverse()
print(Trip)

# Sort (Alphabetical)
Trip.sort()
print(Trip)

# Sort (Alphabetical Reversed)
Trip.sort(reverse=True)
print(Trip)

