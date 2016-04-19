class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left  = left
        self.right = right

def newnode(tree,newdata):
    if tree.data == None :  
        tree.data = newdata
    elif tree.data<newdata and tree.right == None :
        tree.right = Tree(newdata)
    elif tree.data>newdata and tree.left == None :
        tree.left = Tree(newdata)
    elif tree.data>newdata and tree.left != None :
        newnode(tree.left, newdata)
    elif tree.data<newdata and tree.right != None :
            newnode(tree.right, newdata)

def summa(tree):
    if tree == None:
        return 0
    return summa(tree.left) + summa(tree.right) + tree.data 

def print_on_lvl(tree, lvl=0):
    if tree == None:
        return 
    print_on_lvl(tree.right, lvl+1)
    print ('   ' * lvl + str(tree.data))
    print_on_lvl(tree.left, lvl+1)
               
def sozdanie(tree) :
    spisok = []
    while True :
        temp = input('Введите элемент для построения дерева(n - выход)')
        if temp != 'n' :
            spisok += [temp]
        else :
            break
    while spisok :
        temp = int(spisok[0])
        spisok.pop(0)
        newnode(tree,temp)

    
tree = Tree() 
def menu(tree):
    while True :
        main = input('''1 - создать дерево \n2 - добавить элемент\n3 - посчитать сумму\n4 - вывести дерево по уровням \n0 - выход\n''')
        if main == '1' :
            sozdanie(tree)
        elif main == '2' :
            temp = int(input('Введите элемент, которых хотите добавить (int)'))
            newnode(tree,temp)
        elif main == '3' :
            print('Cумма = ', summa(tree))
        elif main == '4' :
            print_on_lvl(tree)
        elif main == '0' :
            break
        else :
            print('Неправильная команда, повторите попытку!')



menu(tree)


        
