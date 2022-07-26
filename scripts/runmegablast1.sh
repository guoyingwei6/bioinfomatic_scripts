if [ $# -ne 3 ]; then
 echo "error.. need args"
 echo "command:$0 parts_num infasta targetdb"
 echo "Split the infasta by number of parts (parts_num) and then generating blast shells..."
 exit 1
else
for arg in "$@"
do
 echo $arg
done
 mkdir fasta shells blastout
 echo "Spliting fasta files..."
 seqkit split -p $1 -O fasta $2
for i in `ls fasta/*.part_*.fa`
do
 name=`basename $i`
 echo "echo $name" > shells/$name".sh"
 echo "blastn -task megablast -db $3 -query ../fasta/$name"" -max_hsps 1 -out ../blastout/$name".blastout" -num_threads 4 -outfmt 0 -num_descriptions 1 -num_alignments 1 " >> shells/$name".sh"
done
fi
