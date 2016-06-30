graph = {} 
def sozdanie():
    global graph
    kol = int(input('Введите кол-во вершин - '))
    for i in range(1,kol+1) :
        temp_contiguity = []
        temp_graph = {}
        while True :
            temp = input('Введите вершину смежную для %s вершины(n - stop)\n' % str(i))
            if temp != 'n':
                temp_contiguity += [int(temp)]
            else :
                break
        temp_contiguity.sort()
        temp_graph = { i : temp_contiguity }
        graph.update(temp_graph)

visit = []
def Deep(q):
    global graph,visit
    if q in visit :
        return
    visit += [q]
    for i in graph[q]:
        if i not in visit:
            Deep(i)
            
turn = []
def breadth(q) :
    global graph,visit,turn
    if q not in visit :
        visit += [q]
        for i in graph.get(q) :
            turn += [i]
        while turn :
            breadth(turn.pop(0))
def vivod() :
    global graph
    for key,data in graph.items() :
        print('{0}: {1}'.format(key,data))
        
def menu() :
    global visit,turn
    while True :
        menu = input('\n1 - создать граф\n2 - вывести список смежности\n3 - проход в глубину\n4 - проход в ширину\n0 - выход\n')
        if menu == '1' :
            sozdanie()
        elif menu == '2' :
            vivod()
        elif menu == '3' :
            visit = []
            start = int(input('Введите начальную вершину - '))
            Deep(start)
            print(visit)
        elif menu == '4' :
            visit = []
            turn = []
            start = int(input('Введите начальную вершину - '))
            breadth(start)
            print(visit)     
        elif menu == '0' :
            break
        else :
            print('Неверный выбор!')
menu()
