#!/bin/bash

while true; do
#Menu options
echo "Menu:"
echo "1. Hello World"
echo "2. Ping self"
echo "3. IP info"
echo "4. Exit"
echo "Please choose an option (1-4):"
read choice

#Evaluate user's input and executing according to it
if [ "$choice" == "1" ]; then
    echo "Hello World!"

    elif [ "$choice" == "2" ]; then
        echo -n "What is your IP address? "
        read ip
        ping -c 3 $ip

    elif [ "$choice" == "3" ]; then
        ip addr show

    elif [ "$choice" == "4" ]; then
        echo "Exiting program"
        exit 0
fi
done
