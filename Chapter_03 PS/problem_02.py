

name = input("Enter your name: ")
date = "14 july 2026"

# Method 1 - f-string
latter = f'''
 Dear {name}, 
 You are Selected! 
 {date}
 '''

print(latter)


# Method 2 - replace()
latter1 = '''
Dear <|Name|>,
You are Selected!
<|Date|>
'''
latter1 = latter1.replace("<|Name|>", name)
latter1 = latter1.replace("<|Date|>", date)

print(latter1)