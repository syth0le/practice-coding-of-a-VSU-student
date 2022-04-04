read first second
DATEINSEC1=$(date -d "$first" +%s)
DATEINSEC2=$(date -d "$second" +%s)
if [ $DATEINSEC1 -gt $DATEINSEC2 ]
then
	difference=$((DATEINSEC1-DATEINSEC2))
	let sec_in_day=24\*60\*60
	diff_in_dates=$((difference/sec_in_day))
	echo $diff_in_dates
else
	difference=$((DATEINSEC2-DATEINSEC1))
    let sec_in_day=24\*60\*60
    diff_in_dates=$((difference/sec_in_day))
    echo $diff_in_dates
fi