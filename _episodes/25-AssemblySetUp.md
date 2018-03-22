---
title: Assembly Set Up
teaching: 20
exercises: 25
questions:
 - No real questions, just a lot o' stuff we need to get ready to assembleeeeeeee!
---

Today, we're getting ready to do genome assembly. There's a bit of legwork for us to do. We will need to download some genomic data (about 10 minutes), and download and prepare some software (the rest of the time).

## Downloading Data

We'll be downloading Minion Sequences from the clownfish from an NCBI database. Most of you are familiar with BLAST, which is operated by NCBI. SRA, the Sequence Read Database, is also an NCBI database, intended for deposition of sequencing reads.

Our data come from the SRA genome website for [_Amphiprion ocellaris_](https://trace.ncbi.nlm.nih.gov/Traces/study/?acc=SRP123679), the clownfish. The genome was published in [this paper](https://academic.oup.com/gigascience/article/7/3/1/4803946)

We will use the command wget to download the three datasets the authors deposited. 

Change directories into your work directory. Make a directory in which you will store and work with the data. Change directories into it, and create the normal data, output and scripts directories.

Within the data directory, create a raw_nanopore directory and a raw_illumina directory. In the raw nanopore directory:

```
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR625/SRR6255801/SRR6255801.sra
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR625/SRR6255800/SRR6255800.sra
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR625/SRR6255797/SRR6255797.sra
```

In the raw Illumina directory: 
```
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR626/SRR6266484/SRR6266484.sra
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR626/SRR6266483/SRR6266483.sra
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR626/SRR6266482/SRR6266482.sra
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR626/SRR6262202/SRR6262202.sra
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR625/SRR6255799/SRR6255799.sra
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR625/SRR6255798/SRR6255798.sra
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR625/SRR6255796/SRR6255796.sra
```

Move these files into the data directory. Each of these files is a different run on a Nanopore or the Illumina. 

## Installing Software

Leave your directory, and place yourself in the work directory. We will now load NCBI's library for interpreting SRA files:

```unix
https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
```

What kind of file is this? How will we unpack it? 

Unpack it, and you can delete the *.gz file.

Next, we will install trimmomatic for adaptor trimming:

```
wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip

unzip Trimmomatic-0.36.zip

cd Trimmomatic-0.36

java -jar trimmomatic-0.36.jar
```
 Change directories back into your work directory.
 
 Next, we will install Kraken, a software for filtering microbial and viral contaminants:
 
```
git clone https://github.com/DerrickWood/kraken.git
cd kraken
./install_kraken.sh .
```

Change directories back into your work directory.

Now we will install an assembler called [MaSURCA](http://www.genome.umd.edu/masurca.html):

```
module load gcc
wget https://github.com/alekseyzimin/masurca/archive/3.2.4.1.tar.gz
cd masurca-3.2.4.1/
tar xvf MaSuRCA-3.2.4.tar.gz 
cd MaSuRCA-3.2.4
BOOST_ROOT=install ./install.sh
./bin masurca
```
The last command should give you an error.

We will also install an assembly refinement software called Pilon:

```
wget https://github.com/broadinstitute/pilon/releases/download/v1.22/pilon-1.22.jar
java -jar pilon-1.22.jar 
```

And a library that lets us calculate genome-level summary stats:

```
git clone https://gitlab.com/ezlab/busco.git
source activate py36
python setup.py install --user
python scripts/run_BUSCO.py -h
```

Aaaaand, that's it.


## Unpacking the data

This step takes a little bit long. SRA files are compressed archives - we will need to unpack them into FASTQ files. This is easy, but it is time consuming. That's why it's last - if you have to complete it over the weekend, the effort is trivial, but the time involved is not. 

We will call a piece of software out of the SRA toolkit calls fastq-dump. As the name suggests, this piece of software unpacks the SRA file and writes it to FASTQ. You will call this on each of the three SRA files. My commands looks like this:

```
/work/amwright/sratoolkit.2.9.0-ubuntu64/bin/fastq-dump data/raw_data/SRR6255797.sra 


```

Make appropriate adjustments for your data and run them. Start an interactive session before you do - this is a high memory operation. 

