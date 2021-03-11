###Solution to exercise 53 in ben stephenson's "the python workbook".

print("Enter a rating:")
rating = float(input())

if rating <= 0:
  print('Unacceptable performance, no raise.')
elif rating == 0.4:
  print(f'Acceptable performance, raise of ${2400 * 0.4}.')
elif rating >= 0.6:
  print(f'Meritorious performance, raise of ${2400 * rating}.')
else:
  print('That\'s not a valid rating.')
