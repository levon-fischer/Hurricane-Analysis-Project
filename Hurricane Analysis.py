# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def update_damage(list):
  for index in range(len(list)):
    if list[index] == 'Damages not recorded':
      list[index] = 'Damages not recorded'
    elif 'M' in damages[index]:
      list[index] = float(damages[index][:-1]) * 1000000
    else:
      list[index] = float(damages[index][:-1]) * 1000000000
  return list
# test function by updating damages
update_damage(damages)

# 2 
# Create a Table
hurricanes = {}
for index in range(len(names)):
  hurricanes.update({names[index]: {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": damages[index], "Deaths": deaths[index]}})
# Create and view the hurricanes dictionary

# 3
# Organizing by Year
hurricanes_by_year = {}
def organize_by_year():
  for h_name, h_info in hurricanes.items():
    current_year = h_info['Year']
    current_cane = h_info
    if current_year not in hurricanes_by_year:
      hurricanes_by_year.update({current_year: [current_cane]})
    else:
      hurricanes_by_year[current_year].append(current_cane)
organize_by_year()

# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas
affected_areas = {}
def count_affected_areas():
  for h_name, h_info in hurricanes.items():
    h_areas = h_info["Areas Affected"]
    for area in h_areas: 
      if area not in affected_areas:
        affected_areas.update({area: 1})
      else:
        affected_areas[area] += 1
count_affected_areas()

# create dictionary of areas to store the number of hurricanes involved in

# 5 
# Calculating Maximum Hurricane Count
def most_affected_area():
  max_area = 'Temp'
  max_area_count = 0
  for area, count in affected_areas.items():
    if count < max_area_count:
      continue
    elif count == max_area_count:
      max_area.append(area)
    else:
      max_area_count = count
      max_area = area
  print(max_area + " was affected " + str(max_area_count) + " times; the most of any area.")
# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane():
  max_cane = 'temp'
  max_deaths = 0
  for h_name, h_info in hurricanes.items():
    if h_info['Deaths'] > max_deaths:
      max_deaths = h_info['Deaths']
      max_cane = h_name
  print(max_cane + " caused " + str(max_deaths) + " deaths; the most of any hurricane.")

# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality
mortality_scale = {1: [], 2: [], 3: [], 4: [], 5: []}
def generate_mortality_scale():
  for h_name, h_info in hurricanes.items():
    if h_info['Deaths'] <= 100:
      mortality_scale[1].append({h_name: h_info})
    elif h_info['Deaths'] <= 500:
      mortality_scale[2].append({h_name: h_info})
    elif h_info['Deaths'] <= 1000:
      mortality_scale[3].append({h_name: h_info})
    elif h_info['Deaths'] <= 10000:
      mortality_scale[4].append({h_name: h_info})
    else:
      mortality_scale[5].append({h_name: h_info})

# categorize hurricanes in new dictionary with mortality severity as key
generate_mortality_scale()


# 8 Calculating Hurricane Maximum Damage
def most_destructive_hurricane():
  max_cane = 'temp'
  max_damage = 0
  for h_name, h_info in hurricanes.items():
    if h_info['Damage'] == 'Damages not recorded':
      continue
    elif h_info['Damage'] > max_damage:
      max_damage = h_info['Damage']
      max_cane = h_name
  print(max_cane + " caused $" + str(max_damage) + " in damage; the most of any hurricane.")
# find highest damage inducing hurricane and its total cost
most_destructive_hurricane()

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
damage_cats = {1: [], 2: [], 3: [], 4: [], 5: [], 'Not Recorded': []}
def generate_damage_scale():
  for h_name, h_info in hurricanes.items():
    if h_info['Damage'] == 'Damages not recorded':
      damage_cats['Not Recorded'].append({h_name: h_info})
    elif h_info['Damage'] <= damage_scale[1]:
      damage_cats[1].append({h_name: h_info})
    elif h_info['Damage'] <= damage_scale[2]:
      damage_cats[2].append({h_name: h_info})
    elif h_info['Damage'] <= damage_scale[3]:
      damage_cats[3].append({h_name: h_info})
    elif h_info['Damage'] <= damage_scale[4]:
      damage_cats[4].append({h_name: h_info})
    else:
      damage_cats[5].append({h_name: h_info})
# categorize hurricanes in new dictionary with damage severity as key
generate_damage_scale()
print(damage_cats)