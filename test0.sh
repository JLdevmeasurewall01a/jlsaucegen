#!/bin/bash
echo 'well here we go'

for i in {1..15}
do echo "F" | python3 saucegen.py
   
   sleep 3
done

echo 'done!'
