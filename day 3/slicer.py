temperature = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

print("First reading :" , temperature[0])
print("Last reading :" , temperature[-1])

afternoon_peak = temperature[3:6]
print("Afternoon Peak Readings:", afternoon_peak)

last_3_hours = temperature[-3:]
print("Last 3 Hours Readings:", last_3_hours)
