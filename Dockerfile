# Fusion detection DockerFile using STAR-Fusion and FusionInspector software
# https://github.com/STAR-Fusion/STAR-Fusion/wiki
# https://github.com/FusionInspector/FusionInspector

FROM ubuntu:18.04

MAINTAINER Jacob Pfeil, jpfeil@ucsc.edu

# Update and install required software
RUN apt-get update --fix-missing

RUN apt-get install -y wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda 

ENV PATH=/root/miniconda/bin:$PATH

RUN conda update -y conda && conda install -y pandas biopython && conda install -y -c bioconda salmon

WORKDIR /opt

# Add wrapper scripts
COPY strander /opt/strander

# Data processing occurs at /data
WORKDIR /data

ENTRYPOINT ["python", "/opt/strander/run.py"]
CMD ["-h"]
