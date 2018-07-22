import re

datestr = '2-11-2002\n23/9/2002\n3/8/02\n9/3/2002\n2 May 2002\n23 September 2002\nJan 2, 2002\nOctober 23, 2002\n'

"""
Potential Digit(s) in the beginning (up to 2)
Return more than just the abbreviation of months
[a-z]* because May doesn't necesarrily have anything after
2 - 4 digits for the year
"""

print(re.findall(r'\d{,2}[/-]\d{,2}[/-]\d{2,4}', datestr))
print(re.findall(r'(?:\d{,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{,2}, )?\d{2,4}', datestr))

# working on combining