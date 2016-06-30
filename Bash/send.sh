#!/bin/bash
function menu {
clear
echo
echo "1) Пользователи в системе"
echo "2) Отправка сообщения пользователю"
echo "3) Выход"
echo -n "Введите номер функции: "
read -n 1 option
}

function user_in {
clear
users 
}

function  send_mess {
clear
echo 'Введите имя пользователя в системе'
read U 
echo 'Для отправки - Enter, выход - Ctrl+D'
write $U  
}

while [ 1 ]
do
        menu
        case $option in

1)
        user_in ;;
2)
        send_mess ;;
3)
        break ;;
*)
        clear
echo "Нужно выбрать действие";;
esac
echo  "Нажмите любую клавишу для продолжения"
read -n 1 line
done
clear
