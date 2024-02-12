
a=$(zipinfo -1 hidden*)

echo $a
for i in $a; do
	echo $i
	less $i
