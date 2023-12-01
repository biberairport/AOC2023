result = result2 = 0

string_numbers =["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

### Aufgabe1:
with open("day01.txt", 'r') as filehandle:
    for line in filehandle:
        if(line != "\n"):
            for char in line:
                if char.isdigit():
                    temp = char
                    break           
            for char in reversed(line):
                if char.isdigit():                    
                    temp += char
                    break
        result += int(temp)        
print(result)


### Aufgabe2:
with open("day01.txt", 'r') as filehandle:
    for line in filehandle:
        temp_index = 99
        temp_high = 0
        res_low = res_high = ""        

        for substring in string_numbers:
            try:
                index = line.index(substring)
                last_index = line.rfind(substring)

                if(index <= temp_index):                    
                    temp_index = index
                    res_low = substring
                if(last_index >= temp_high):                    
                    res_high = substring
                    temp_high = last_index                            
            except ValueError: pass
                
        results = []
        for res in [res_low, res_high]:
            try:
                position = string_numbers.index(res)
                if position >= 9:
                    position -= 9
                results.append(str(position + 1))
            except ValueError: pass
        result2 += int(''.join(results))            
print(result2)
