blastp –query target.fa -db /mnt/NFS_UPF/soft/databases/blastdat/pdb_seq -out target_pdb.out

psiblast -query target.fa -db /mnt/NFS_UPF/soft/databases/blastdat/pdb_seq -num_iterations 5 -out target_pdb_5.out

psiblast -query target.fa -num_iterations 5 -out_pssm target_sprot5.pssm -out target_sprot_5.out -db /mnt/NFS_UPF/soft/databases/blastdat/uniprot_sprot.fasta

psiblast -db /mnt/NFS_UPF/soft/databases/blastdat/pdb_seq -in_pssm target_sprot5.pssm -out target_pdb_sprot5.out
