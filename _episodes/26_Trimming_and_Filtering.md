---
title: Trimming and bacterial filtration
teaching: 180
exercises: 0
questions:
 - How can we remove adapter sequences?
 - And how can we set up Kraken to filter out bacteria and virus sequence?
---

Let's look at the data. We have a combination of single- and paired-end reads. The paired-end reads are interleaved. First, we will need to de-interleave them. 

```
./scripts/deinterleave.sh < data/raw_data_illumina/SRR6266484.fastq data/SRR6266484.f.fastq data/SRR6266484.r.fastq
./scripts/deinterleave.sh < data/raw_data_illumina/SRR6266483.fastq data/SRR6266483.f.fastq data/SRR6266483.r.fastq
./scripts/deinterleave.sh < data/raw_data_illumina/SRR6255799.fastq data/SRR6255799.f.fastq data/SRR6255799.r.fastq
./scripts/deinterleave.sh < data/raw_data_illumina/SRR6255796.fastq data/SRR6255796.f.fastq data/SRR6255796.r.fastq

./scripts/deinterleave.sh < SRR6255798.fastq data/SRR6255798.f.fastq data/SRR6255798.r.fastq
```

These files were made using MiSeq. We will now trim out the adapters used by Illumina. Please create a file called paired-end-adapter.txt. Into it, paste the following:

```
CTGTCTCTTATACACATCT+AGATGTGTATAAGAGACAG
```


Starting with the first step of the pipeline. We'll remove the adaptors from the paired-end reads first:


```UNIX
java -jar  /work/amwright/Trimmomatic-0.36/trimmomatic-0.36.jar PE data/SRR6266483.f.fastq data/SRR6266483.r.fastq -baseout data/paired-end/SRR6266483_trimmed ILLUMINACLIP:paired-end-adapters.txt:2:30:10 MINLEN:100

java -jar  /work/amwright/Trimmomatic-0.36/trimmomatic-0.36.jar PE data/SRR6266484.f.fastq data/SRR6266484.r.fastq -baseout data/paired-end/SRR6266484_trimmed ILLUMINACLIP:paired-end-adapters.txt:2:30:10 MINLEN:100

java -jar  /work/amwright/Trimmomatic-0.36/trimmomatic-0.36.jar PE data/SRR6255796.f.fastq data/SRR6255796.r.fastq -baseout data/paired-end/SRR6255796_trimmed ILLUMINACLIP:paired-end-adapters.txt:2:30:10 MINLEN:100

java -jar  /work/amwright/Trimmomatic-0.36/trimmomatic-0.36.jar PE data/SRR6255799.f.fastq data/SRR6255799.r.fastq -baseout data/paired-end/SRR6255799_trimmed ILLUMINACLIP:paired-end-adapters.txt:2:30:10 MINLEN:100

```

File SRR6266498 is the largest. It will not be possible to deinterleave and clean during class time.

Then, we will remove adaptors from the single-end reads:

```
java -jar  /work/amwright/Trimmomatic-0.36/trimmomatic-0.36.jar SE data/SRR6266482.fastq data/SRR6266482_trimmed ILLUMINACLIP:paired-end-adapters.txt:2:30:10 MINLEN:100 
```

These steps are not complex, but they are operating on big data. So they take time.

Now, you may say to yourself "this is no longer raw data". You would be right. Let's move all the fastq files down one level. If we count up the size of files in here, there is about 34.5 GB of sequence data, and we have not processed one of our files.

##Processing the nanopore data

You might recall that when we practiced with nanopore data, we used a tool called poretools. But this time, we're taking someone else's data in SRA format. In the paper, the authors say they filtered the reads so that no read was shorter than 500 BP. How can we perform the same filtration, which we would have simply done in poretools? 

There are two ways we can do this. First, in your nanopore data directory, make a directory called "unfiltered", and put the *fastq files in it. We can re-export the SRA data, with a filter, like so:
```
/work/amwright/sratoolkit.2.9.0-ubuntu64/bin/fastq-dump -M 500 raw_data_nanopore/SRR6255801.sra
```
Make a directory called "filtered", and place the output of this command in it. Use ls -lth to get the file size.

```
 awk -v min=$minlen '{if(NR%4==2) if(length($0)<500) print NR"\n"NR-1"\n"NR+1"\n"NR+2}' raw_data_nanopore/unfiltered/SRR6255801.fastq > temp.lines1
 
sort -n temp.lines1 | uniq > temp.lines 

awk 'NR==FNR{l[$0];next;} !(FNR in l)' temp.lines raw_data_nanopore/unfiltered/SRR6255801.fastq > SRR6255801.fastq.500
 ```

Does the way in which you perform the filtration make a difference? Try looking at the first couple lines of temp.lines - does it make sense that this would or would not make a difference to the ultimate file size? 

So, how many reads do we have, total? We can use very simple unix commands to find this info.

The next step is to use Kraken to filter out contaminants. Kraken has one dependency, jellyfish. In your work directory:

```
wget http://www.cbcb.umd.edu/software/jellyfish/jellyfish-1.1.11.tar.gz

tar xvf jellyfish-1.1.11.tar.gz

cd jellyfish-1.1.11

./configure
make
```

We now have a  jellyfish executeable. Kraken will need to be told where it is, so we'll add it to our path:

```
nano ~/.bash_profile
source ~/.bash_profile
```

Now, we will be able to build our Kraken database, which will house basically all known bacteria and viruses. This will run over night.




