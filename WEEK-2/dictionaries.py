# Dictionaries in Python. This is a special structure in Python that allows us to store information in what are called key value pairs.

# A program here will be created which will allow us to convert a 3 digit month name into the full month name. 
# For example 
# Jan -> January
# Mar -> March


# Creating the dictionary
# FIrst thing to do is to give it a specific name. 

monthCOnversions = { # Adding the Key and the Value 
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}


print(monthCOnversions["Mar"]) 

# Using a get Function
print(monthCOnversions.get("Luv", "Not a valid Key")) # When trying to get a key that is not in the dictionary