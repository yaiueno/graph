mydic={'Yamada':175, 'Nakamura':163, 'Takahashi':163, 'Sato':181}
print(mydic)
print(mydic['Takahashi'])
mydic['Takahashi'] = 999
print(mydic)
mydic['BOOK'] = 333
print(mydic)
del mydic['Nakamura']
print(mydic)