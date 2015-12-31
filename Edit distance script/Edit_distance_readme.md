# Edit distance script.

These scripts may contain two parts to calculate edit distance. At first, from.fast.get_29bp.for.revcomp.py should be run to get 29-length DNA base pairs from given chromosome number and position in your reference genome (e.g. hg19). Next, edit.step.bulge.weight.py will calculate between obtained 29-length DNA base pair and RGEN on-target sequence. Second script also gives the edit distance steps which can be identify 'addition', 'deletion' and 'subtitution'. Finally, the number of 'deletion' step will be added to edit distance score to assign 'bulge' weight.

Instruction

step1. from.fast.get_29bp.for.revcomp.py

* Input : Chromosome number and position, fasta file of reference genome

1. Chromosome number and sequence position of your interest.

        Example> Cloning.txt
        chr1	17346702
        chr1	177593980
        chr3	3662556
        chr3	19957634
        chr4	148531374
        chr5	14347051
        chr5	131423385
        chr6	23709579

2. fasta file of each chromosome of reference genome (e.g. hg19)

        Example> chr1.fa, chr2.fa, chr3.fa ...

* Output: 29-length DNA base pairs and its reverse-complement of given chromosome number and position.

        Example>
        Cloning_29.txt
        chr1	17346702	TTTCCGGTCCCCACAGGGTCAGTAAGGGT	TTCTAAGTCTAAACACCCTTACTGACCCT
        chr1	177593980	GAATTTCTACCCCACATGGCAGTAATGGG	AGGGGATTCACCAACCCATTACTGCCATG
        chr3	3662556	TTGTTAAAGCCCCACAGGGTAGTAGAGGA	GATCTTTGGGCGATTCCTCTACTACCCTG
        chr3	19957634	GAACCACAAATTAGAACCCCTAATGCCCT	CATGGCTACCCCACAGGGCATTAGGGGTT
        chr4	148531374	CATATGTTACCTCACAGAGCAGAAAGGGA	CCATGTCTACAAAATCCCTTTCTGCTCTG
        chr5	14347051	GTCCTCATACCCCACAGGTCAGTAAGGAA	AGACTGGACGTGACTTCCTTACTGACCTG
        chr5	131423385	TCCTGGTTTTTTCCTCCCCTTCCTGGCCT	TTTCTCTGCCCCACAGGCCAGGAAGGGGA
        chr6	23709579	CCAAGGTACAGGGACTCCATTGCTGCCCT	TTCAGAAGCCCTACAGGGCAGCAATGGAG


step2. edit.step.bultge.weight.py 

* Input: the result of step1, on-target sequence

1. the result of step1

        Example> Cloning_29.txt
        chr1	17346702	TTTCCGGTCCCCACAGGGTCAGTAAGGGT	TTCTAAGTCTAAACACCCTTACTGACCCT
        chr1	177593980	GAATTTCTACCCCACATGGCAGTAATGGG	AGGGGATTCACCAACCCATTACTGCCATG
        chr3	3662556	TTGTTAAAGCCCCACAGGGTAGTAGAGGA	GATCTTTGGGCGATTCCTCTACTACCCTG
        chr3	19957634	GAACCACAAATTAGAACCCCTAATGCCCT	CATGGCTACCCCACAGGGCATTAGGGGTT
        chr4	148531374	CATATGTTACCTCACAGAGCAGAAAGGGA	CCATGTCTACAAAATCCCTTTCTGCTCTG
        chr5	14347051	GTCCTCATACCCCACAGGTCAGTAAGGAA	AGACTGGACGTGACTTCCTTACTGACCTG
        chr5	131423385	TCCTGGTTTTTTCCTCCCCTTCCTGGCCT	TTTCTCTGCCCCACAGGCCAGGAAGGGGA
        chr6	23709579	CCAAGGTACAGGGACTCCATTGCTGCCCT	TTCAGAAGCCCTACAGGGCAGCAATGGAG

2. On-target sequence

        Example>
        HBB = 'CTTGCCCCACAGGGCAGTAACGG'

* Output: result file containing edit distance information, this tab-delimited file can be opened in Microsoft Excel.

        Example>
        Cloning_29_result_bulge3.txt
        Chr	Location	Forward29	Reverse29	Edit dist for	Edit dist rev	Step for	Step rev	Deletion# for	Deletion# rev	Bulge dist for	Bulge dist rev		
        chr1	17346702	        TTTCCGGTCCCCACAGGGTCAGTAAGGGT	TTCTAAGTCTAAACACCCTTACTGACCCT	8	18	"        [('replace', 0, 0), ('insert', 3, 3), ('insert', 3, 4), ('insert', 4, 6), ('insert', 4, 7), ('insert', 14, 18), ('replace', 20, 25), ('insert', 23, 28)]"	"[('insert', 0, 0), ('insert', 0, 1), ('insert', 2, 4), ('replace', 2, 5), ('insert', 4, 7), ('replace', 5, 9), ('replace', 6, 10), ('replace', 7, 11), ('insert', 11, 15), ('replace', 11, 16), ('replace', 12, 17), ('replace', 13, 18), ('replace', 14, 19), ('replace', 16, 21), ('insert', 18, 23), ('replace', 19, 25), ('replace', 21, 27), ('replace', 22, 28)]"	0	0	8	18	8	0

