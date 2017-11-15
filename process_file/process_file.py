"""
Reads an fixed length input file and parses the first name, last name and
amount. If the state is 'MI', prints the information and adds the amount to a
running total. Displays the total at the end.
"""

import sys
from decimal import Decimal

total = Decimal(0.00)
for line in sys.stdin:
    if line.strip():
        first_name = line[10:25].strip()
        last_name = line[25:40].strip()
        state = line[40:42]
        amount = Decimal(line[45:].strip())
        if state == 'MI':
            print('{} {} {}'.format(first_name, last_name, amount))
            total += amount

print()
print(total)
