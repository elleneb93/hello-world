name = "Ellen"
age = 24
heighta = 5
heightb = 4
eyes = 'brown'
teeth = 'white'
hair = 'brown'

print(f"let's talk about {name}.") #f" tells python to expect a format is needed
print(f"she's {heighta} foot {heightb} inches tall")
print(f"she's got {eyes} eyes and {hair} hair")

total_height = (heighta * 12) + heightb
total = age + total_height
print(f"if I add my age and height together i get {total}")

height_metric = total_height * 2.54
print(f" {heighta} foot {heightb} is equivalent to {height_metric} cm")
