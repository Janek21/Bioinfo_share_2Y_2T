
#example input: Q8TWL6, A3CS71, A8AUJ7, C6A5E8, A7IAU8, O29101, Q0W363,
read -r query

for word in $query; do
	word=${word::-1}
	echo ${word}
	curl -O https://rest.uniprot.org/uniprotkb/${word%+}.fasta
done
