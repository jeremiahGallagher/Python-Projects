# Parsing XML with Python
# Jeremiah Gallagher
# CSIS 354: Week 4

# xmlParse.py


# Calling arguments: plant_catalog.xml plantName percentChange
import xml.etree.ElementTree as ET
import sys

# test for the correct amount of arguments in command line call
if len(sys.argv) < 3:
    print("You did not provide the name and percentage!")
    exit(1)
elif len(sys.argv) < 4:
    print("You did not provide the percentage!")
    exit(1)
elif len(sys.argv) > 4:
    print("you provided too many arguments!")
    exit(1)

# input parameters
searchName = sys.argv[2]               # receive plant name from command-line argument #2
percent = int(sys.argv[3])           # receive percentage to change from command-line argument #3

# range check the percent and ask for a valid number if it isn't
while percent < -90 or percent > 100:
    percent = int(input("The number provided is not valid.  Please enter a number between -90 and 100. A "
                        "Negative percentage will reduce price, a positive will increase it"))

# change negative inputs into positive
if percent < 0:
    percent = 100 - abs(percent)

# add 100 to positive nums so they are will be a 1.+ multiplier
if percent > 0:
    percent += 100
print(percent)
# convert percent into valid decimal representation
percent *= .01


searchName = searchName.lower()                     # set the plant name to all lowercase

# parse XML data file
tree = ET.parse(sys.argv[1])           # receive the file to parse as command-line argument #1

root = tree.getroot()

for plant in root.findall('PLANT'):      # loop over the root and inspect the 'PLANT' elements
    name = plant.find('COMMON').text     # assign the 'COMMON' sub-element value to a variable
    name = name.lower()                         # set it to all lowercase for comparison
    if name == searchName:                             # compare the name variable to the searchName variable
        price = float(plant.find('PRICE').text)        # capture and convert the price to a variable
        price = round(price*percent, 2)                # calculate the new price, round and reduce precision
        plant.find("PRICE").text = str(price)          # convert the price back to string and input to field.


tree.write("plant_catalog.xml.bak")                               # output the results to a new file.
