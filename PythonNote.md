# Python Tips

* [Video Link](https://www.youtube.com/watch?v=C-gEQdGVXbk&list=FLqcikxBbByUlHNJrWP0ryGA&index=2&t=151s)

---



### 1

### 2

### Enumerate function

```python
names = ['Anna', 'Alex', 'Tiffany', 'Leo']

for index, name in enumerate(names, start = 1):
  print(index, name)
  
# OUTPUT #
1 Anna
2 Alex
3 Tiffany
4 Leo
```

### Zip function

```python
names = ['Anna', 'Alex', 'Tiffany', 'Leo']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

#for index, name in enumerate(names, start):
#  her = heroes[index]
#  print(f'{name} is actually {hero}')
  
for name, hero in zip(names, heroes):
  print(f'{name} is actually {hero}')
  
for value in zip(names, heroes):
  print(value)
  
# OUTPUT #
Anna is actually Spiderman
Alex is actually Superman
Tiffany is actually Deadpool
Leo is acutally Batman
('Anna', 'Spiderman')
('Alex', 'Superman')
('Tiffany', 'Deadpool')
('Leo', 'Batman')
```



