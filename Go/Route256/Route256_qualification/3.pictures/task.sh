read line
read -a strarr <<< "$line"

echo "Квадрат со стороной" ${#strarr[@]};
for (( i=1; i <= ${#strarr[@]}; i++ ))
do
echo $line;
done