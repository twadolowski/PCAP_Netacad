from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53, 0)

# 2020/11/04 14:53:00
print(dt.strftime("%Y/%m/%d %H:%M:%S"))

# 20/November/04 14:53:00 PM
print(dt.strftime("%y/%B/%d %I:%M:%S %p"))

# Wed, 2020 Nov 04
print(dt.strftime("%a, %Y %b %d"))

# Wednesday, 2020 November 04
print(dt.strftime("%A, %Y %B %d"))

# Weekday: 3
print("Weekday:", dt.strftime("%w"))

# Day of the year: 309
print("Day of the year:", dt.strftime("%j"))

# Week number of the year: 44
print("Week number of the year:", dt.strftime("%U"))
