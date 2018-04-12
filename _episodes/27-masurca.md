---
title: Setting Up Masurca
teaching: 180
exercises: 0
questions:
 - Setting up data and config files for use with Masurca
---

## Masurca

First, begin an interactive session. Then, move into your owrk directory.

```
wget https://github.com/alekseyzimin/masurca/files/1668918/MaSuRCA-3.2.4.tar.gz
cd MaSuRCA-3.2.4/
BOOST_ROOT=install ./install.sh
```

Get into your clownfish directory. Masurca takes an input configuration file. We will generate and edit a sample: 

```
/work/UserName/MaSuRCA-3.2.4/bin/masurca -g short_reads.config
```
Masurca uses a config file that keeps all your input arguments in one place. 

Today, we're just going to do the short reads. The paper performed both short read and hybrid assembly; we will do the hybrid Tuesday.

We will first edit the config script. Rename the config to short_reads.config, to indicate that this script will only be used for short reads. 

Next, edit line 13 in the script with the path to your Illumina paired-end reads. 

You will notice that after the PE, there are two numerical values. These are the average and the std dev of the read length; they are used to figure out how long the kmers should be. 

This script:
```
awk 'BEGIN { t=0.0;sq=0.0; n=0;} ;NR%4==2 {n++;L=length($0);t+=L;sq+=L*L;}END{m=t/n;printf("total %d avg=%f stddev=%f\n",n,m,sq/n-m*m);}'  data/paired-end/*P
``` 
can be used to calculate this info; in the interest of time, I will tell you that the values should be 155 and 18 for the paired end. Edit these values in the config script.

Now, at line 14, we will add a line for the single-end data. We could also run the average read legnth script:

```
awk 'BEGIN { t=0.0;sq=0.0; n=0;} ;NR%4==2 {n++;L=length($0);t+=L;sq+=L*L;}END{m=t/n;printf("total %d avg=%f stddev=%f\n",n,m,sq/n-m*m);}'  data/single-end/*.fastq
```
But for the sake of time, I have provided the values below.

```
PE= se 150 7 data/single-end/SRR6266482_trimmed.fastq
```

Lastly, comment out the PacBio line.

Now, we will run Masurca to get the config for this specific run:

```
/work/amwright/MaSuRCA-3.2.4/bin/masurca scripts/short_reads.config

```

In your directory, you will now have a file called assemble.sh. Rename it to short_read_assemble.sh.

Change directories into the course repository. Do a git pull. Copy the file assembly_script.sh from the course repo (in the scripts directory) into your scripts of the clownfish directory. 

Now, copy your short_reads.config to a script called long_reads.config. 

We need to combine our nanopore output into one single file:

```
for file in *.fastq
do
cat >> mega_fastq
done
```

Uncomment the PacBio line, and add your path to the combined fastq. 

Now, we will call masurca to make the assembly script:

```
/work/amwright/MaSuRCA-3.2.4/bin/masurca scripts/long_reads.config

```

This will, again, create a script called assemble.sh. Change it to long_read_assemble.sh.

## Homework:

Work in pairs. One of you use the assembly_script.sh to run the short read assembly, one the hybrid assembly. By Tuesday, commit the long read MaSuRCA input file, the short read Masurca file, and a qsub script that will run either (or both) to your copy of the course repo.

