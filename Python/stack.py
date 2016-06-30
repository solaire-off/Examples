class Stack: 
    def __init__(self):
        self.elements = [] 

    def push(self, item): 
        self.elements.append(item) 

    def pop(self): 
        self.elements.pop()

    def peek(self):
        print('Вершина стека  - %s'%str(self.elements[len(self.elements)-1])) 

s = Stack() 

def menu():
    while True:
        menu = int(input('1 - Добавление 2 - Удаление 3 - Просмотр 0 - Выход\n'))
        if menu==1 :
            temp = int(input('Новый элемент = '))
            s.push(temp)
        elif menu==2 :
            s.pop()
        elif menu==3 :
            s.peek()
        elif menu==0 :
            break

menu()
