#!/bin/bash


# this script will run when a user logs in, the user won'tbe able to use the system, only choose from the following options, each choice will be written to a log file 

# generate log file 
log_file=/var/log/choice.log

log_choice() {
    echo "$(date '+%Y-%m-%d %H:%M:%S'): $1" >> "$log_file"
}

while true; do
echo
echo		
echo "choose one of the following options:"

echo "1. display all usernames"
echo "2. display details in specific user"
echo "3. list a specific directory"
echo "4. edit your profile file"
echo "5. display 4 biggest process"
echo "6. display FS details"
echo "7. manage storage"
echo "8. exit the script"

username=$(whoami)
usernames=$(cut -d: -f1 /etc/passwd)

read "a";

case $a in
    1) echo "$usernames"
       log_choice "option 1" ;;
    2) read -p "enter username  " "us"
	    echo "username: $us, groups: $(groups $us), home directory: /home/$us"
            log_choice "option 2" ;;
    3) read -p "enter the directory path you want to list  " "dir"
	    if [ -d "$dir" ]; 
	    then
	    ls $dir
	    else
	    echo "directory does not exist"			
	    fi 
            log_choice "option 3" ;;
    4) sudo nano .bash_profile 
       log_choice "option 4" ;;
    5) ps aux --sort=-%cpu | head -n 5
       echo
       echo
       read -p "would you like to kill one of the following processes? (yes/no)  " "ans";
       if [ "$ans" == "yes" ]; then
           read -p "insert PID of the process you want to kill  " "pid"
	   kill $pid
       fi 
       log_choice "option 5" ;; 
    6) read -p "choose a unit: k(KB), m(MB), h(GB)  " "u";
       df -$u 
       echo
       echo
       echo "Fs with less then 15% free space:"
       echo
       echo
       df -h | awk '$5+0 > 85 {print}' 
       log_choice "option 6" ;;
    7) sudo vgs
       echo
       echo  
       read -p "type VG name to display LV's  " "vg"
       echo
       echo
       sudo vgdisplay $vg 
       log_choice "option 7" ;;   
    8) echo "exiting the script"
       log_choice "option 8"
       pkill -9 -u $username
       exit 0;;
esac
done
