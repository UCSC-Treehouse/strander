# Inferring Library Type from RNA-Seq Data
This docker container uses Salmon to infer the library type from RNA-seq data. 
The output includes the [Salmon library code](https://salmon.readthedocs.io/en/latest/library_type.html) 
and an ASCII figure describing the library. This method does not create an alignment file. 

### Paired-End Sequencing
```
docker run -it -v $PWD:/data jpfeil/strander:0.1.0 -1 sample-R1.fastq -2 sample-R2.fastq
```

### Single-Read Sequencing
```
docker run -it -v $PWD:/data jpfeil/strander:0.1.0 -1 sample-R1.fastq
```

### Output
The output contains an ASCII figure and the Salmon libtype code (described here https://salmon.readthedocs.io/en/latest/salmon.html#what-s-this-libtype).

```
Library Type: ISF
5'--====1====>-----------------3',
3'-----------------<====2====--5
```
