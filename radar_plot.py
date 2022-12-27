import matplotlib.pyplot as plt

# Set the chart data
ski_resorts = ['Woodward', 'Snowbird', 'Alta', 'Park City', 'Solitude', 'Brighton', 'Deer Valley', 'Snowbasin', 'Nordic Valley', 'Powder Mountain', 'Sundance', 'Cherry Peak', 'Beaver', 'Eagle Point', 'BrianHead']
price = [1, 3, 2, 3, 2, 2, 3, 3, 1, 2, 2, 1, 1, 1, 1]
location = [27, 29, 32, 32, 33, 35, 38, 45, 51, 55, 55, 99, 114, 204, 213]
terrain_parks = [8, 0, 0, 7, 0, 3, 0, 3, 1, 0, 3, 0, 2, 2, 2]
beginner_terrain = [36, 27, 15, 8, 6, 23, 25, 20, 20, 25, 21, 37, 35, 21, 32]
intermediate_terrain = [45, 38, 31, 41, 43, 39, 43, 50, 30, 40, 32, 47, 40, 36, 35]
advanced_terrain = [18, 35, 53, 51, 51, 38, 32, 31, 50, 35, 47, 16, 25, 44, 32]
ikon = ['N', 'L', 'L', 'N', 'Y', 'L', 'L', 'L', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
free_skiing_max_age = [0, 6, 0, 6, 4, 6, 0, 4, 12, 6, 5, 5, 5, 6, 12]
snowfall = [150, 500, 540, 360, 500, 500, 300, 300, 300, 500, 300, 322, 400, 350, 360]

# Set the chart options
categories = ['Price', 'Location', 'Terrain Parks', '% Beginner Terrain', '% Intermediate Terrain', '% Advanced Terrain', 'Ikon', 'Free Skiing Max Age', 'Snowfall']

# Create the chart
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set the angle of each axis
angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
angles += angles[:1]

# Set the values for each axis
values = [price, location, terrain_parks, beginner_terrain, intermediate_terrain, advanced_terrain, ikon, free_skiing_max_age, snowfall]
values += values[:1]

# Set the labels for each axis
ax.set_thetagrids(angles * 180/pi, categories)

# Plot the chart
ax.plot(angles, values)
ax.fill(angles, values, alpha=0.1)

# Set the title and show the chart
plt.title('Ski Resort Comparison')
