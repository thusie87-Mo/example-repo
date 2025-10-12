Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Ask for user input
swimming = int(input("Enter swimming time (minutes):"))
Enter swimming time (minutes):30
cycling = int(input("Enter cycling time (minutes):"))
Enter cycling time (minutes):40
running = int(input("Enter running time (minutes):"))
Enter running time (minutes):25

# Calculate total time
total_time = swimming + cycling + running
>>> 
>>> # Print total time
>>> print(f"\nTotal time to complete the triathlon:{total_time)minutes")
SyntaxError: f-string: unmatched ')'
>>> print(f"\Total time to complete the triathlon:{total_time}minutes")
\Total time to complete the triathlon:95minutes
>>> 
>>> #Determine award
>>> if total_time <= 100
SyntaxError: expected ':'
>>> if total_time <= 100:
...     print("Award: Provicial Colours")
...     elif total_time <= 105:
...         
SyntaxError: invalid syntax
>>> elif total_time <= 105:
...     
SyntaxError: invalid syntax
>>> 
...  
>>> elif total_time <= 105:
...     
SyntaxError: invalid syntax
>>> elif total_time <=105:
...     
SyntaxError: invalid syntax
>>> # Determine award
>>> if total_time <= 100:
...     print("Award: Provincial Colours
...           
SyntaxError: unterminated string literal (detected at line 2)
>>> if total_time <= 100:
...           print("Award: Provincial Colours")
... elif total_time <= 105:
...     print("Award: Provincial Half Colours")
... elif total_time <= 110:
...     print("Award: Provincial Scroll")
... else:
...     print("Award: No award")
