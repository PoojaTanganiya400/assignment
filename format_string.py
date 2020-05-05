# Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# Sample Output:
# WE, THE PEOPLE OF INDIA,
#      having solemnly resolved to constitute India into a SOVEREIGN, !
#            SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#            and to secure to all its citizens

string = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a\
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all\
its citizens"

formatted_string ="WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a\
SOVEREIGN,!\n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t and to secure to all\
its citizens"

print(formatted_string)