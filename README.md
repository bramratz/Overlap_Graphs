# Overlap_Graphs
Python script that finds sequences in a fasta file such that sequences s and t overlap by k-number of bases between k-suffix of s and k-prefix of t.

## Usage:
python SequenceEdgeOverlap.py DNA_Sequences.fasta k

## Sample Input and output
### Example input:
>ID_0498  
AAATAAA  
>ID_2391  
AAATTTT  
>ID_2323  
TTTTCCC  
>ID_0442  
AAATCCC  
>ID_5013  
GGGTGGG  

### Example output:
>Rosalind_0498 Rosalind_2391  
>Rosalind_0498 Rosalind_0442  
>Rosalind_2391 Rosalind_2323  
