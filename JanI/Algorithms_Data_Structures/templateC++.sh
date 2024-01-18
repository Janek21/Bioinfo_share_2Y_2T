if [ -d "$1" ]; then
	cd $1
else
	echo "new directory created"
	mkdir $1
	cd $1
fi

curl -o $3.zip https://jutge.org/problems/$3/zip
unzip $3.zip
mv $3 $2
rm $3.zip
cd $2

problem_id="${3%???}"

rename 's/sample/'$problem_id'/' *
rename 's/problem/'$3'/' *

english="${problem_id}_en"
curl -o $english.pdf https://jutge.org/problems/$english/pdf

#treure _en o _ca
set -o noclobber

echo "#!/usr/bin/python3" > $2.py
echo "import sys" >> $2.py

