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
java -jar  /work/amwright/Trimmomatic-0.36/trimmomatic-0.36.jar SE data/SRR6266482.fastq SRR6266482_trimmed.fastq ILLUMINACLIP:paired-end-adapters.txt:2:30:10 MINLEN:100
```

These steps are not complex, but they are operating on big data. So they take time.

Now, you may say to yourself "this is no longer raw data". You would be right. Let's move all the fastq files down one level. If we count up the size of files in here, there is about 34.5 GB of sequence data, and we have not processed one of our files.

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

So, overnight:

Run 

1. long_clean. Make sure to edit the "me-specific" parts to "you-specific".
2. kraken-build. Make sure to edit the "me-specific" parts to "you-specific".
3. kraken-filter. Make sure to edit the "me-specific" parts to "you-specific".
