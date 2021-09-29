# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def changeX(num):
    x[1][0] = num
    students[0]['last_name'] = 'Bryant'
    sports_directory['soccer'][0] = 'Andres'
    z[0]['y'] = 30
changeX(15)
# print(x)
# print(students)
# print(sports_directory['soccer'])
# print(z)

# 2. Iterate Trough a List of Dictionaries
