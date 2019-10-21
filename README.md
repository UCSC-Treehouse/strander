# Inferring Library Type for RNA-Seq Data

### Paired-End Sequencing
```
docker run -it -v $PWD:/data jpfeil/strander:0.1.0 -1 sample-R1.fastq -2 sample-R2.fastq
```

### Single-Read Sequencing
```
docker run -it -v $PWD:/data jpfeil/strander:0.1.0 -1 sample-R1.fastq
```
