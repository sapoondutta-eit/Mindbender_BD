#!usr/bin/bash


echo "Enter 1 to start serivce"
echo "Enter 2 to stop servie"
read opt 

if [[ $opt == 1 ]]; then
	OUTPUT=$(jps)
	echo "${OUTPUT}"

	if [[ $OUTPUT == *"ResourceManager"* ]]
		then
   		echo "It's already running!"
	else 
  		eval "start-all.sh"
	fi
else
	OUTPUT=$(jps)
	echo "${OUTPUT}"

	if [[ $OUTPUT == *"ResourceManager"* ]]
		then
   		echo "It's running!"
		eval "stop-all.sh"
		
	else 
  		echo "it's already stopped"
	fi
fi

#$java_check = jps
#if [ -z "$java_check" ]; then
#    echo $java_check
#    echo "No processes"
#else
#    echo "Hadoop is already running"

#fi

