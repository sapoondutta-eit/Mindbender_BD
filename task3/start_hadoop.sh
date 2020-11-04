#!usr/bin/bash

OUTPUT=$(jps)
echo "${OUTPUT}"

if [[ $OUTPUT == *"ResourceManager"* ]]
then
   echo "It's there!"
else 
  eval "start-all.sh"
fi

#$java_check = jps
#if [ -z "$java_check" ]; then
#    echo $java_check
#    echo "No processes"
#else
#    echo "Hadoop is already running"

#fi

