print(type(73))

print(73.73, int(73.73))
print(-41.91, int(-41.91))

print("""she exclaimed: "My God, he is pretty". Then walked away.""")

print(type(str(123.45)))
print(int(123.98))

message = "Hola Hej"
print(message)
print(type(message))
den = "Lundi"
print(den)
den = "Pondeli"
print(den)

print("""funkce "len" ti spocita pismena stringu""")
print(len("chemistry"))
print(2 + 6)
pismena = len("chemistry")
print(pismena)

print(6 / 4)
print(6 // 4)
print(-6 // 4)
print(6 // -4)
# // posouvá vysledek vzdy k nejblizsimu mensimu int - tedy k nejblizsimu int nalevo na ciselne ose
print(9 // 4)
print(9 % 4)
# % ti vyhodi zbytek deleni pomoci //
total_secs = 6666
hours = total_secs // 3600
remaining_secs = total_secs % 3600
print(hours)
print(remaining_secs)
remaining_minutes = remaining_secs // 60
print(remaining_minutes)
finally_remaining_secs = remaining_secs % 60
print(finally_remaining_secs)
# 6666 je 1 h 51 min 6 s
# jupiiiiii

# Ted mi to z nejakeho duvodu prestalo printit uplne vsechno, prooooc?
print (12 % 15)

#zaverecne cviceni 1
a = input("What time is it?")
print (a)
b = input("After how many hours do you want your alarm to go off?")
print (b)
c = "Your time will go off at:"
c = (a + b) % 24
print (c)
#Proc je spatne radek 54?

starting_day_string = input("Enter a number of the day your holiday started")
lenght_string = input("Enter a number of days you were enjoying your holiday")

starting_day_int = int(starting_day_string)
lenght_int = int(lenght_string)

holiday_lenght = starting_day_int + lenght_int
day_of_return = holiday_lenght % 7
actual_day_of_return = day_of_return - 1

a = "All"
b = "work"
c = "and"
d = "no"
e = "play"
f = "makes"
g = "Jack"
h = "a"
ch = "dull"
j = "boy"
print(a, b, c, d, e, f, g, h, ch, j)
#Dala jsem to!
radius_str = input("Enter the radius")
radius_int = int(radius_str)
result = 2 * 3.14 * radius_int
print("The area of your little circle is:", result)
#Funguje!
miles = input("Enter the number of miles driven.")
miles_int = int(miles)
gallons = input("Enter the number of gallons used.")
gallons_int = int(gallons)
mpg = miles_int / gallons_int
print("MPG of your car is:", mpg)
#jupiii
