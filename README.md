> OVERVIEW

This script separately executes (qsub) script files splited by `write_EVM_commands.pl` in EVM.  

> PREPARATION

Prepare a text file describing a common part of job script file for PBS.  

The file is like:  
  

__pbs_job_comment.txt__  
```
#!/bin/bash -f

#PBS -l nodes=1:ppn=1:yuri
#PBS -q yuri
#PBS -N EVM
#PBS -j eo
#PBS -m ae

source ~/.bashrc
conda activate evm

cd /work2/yuka97524/Temma/26evidenceModeler

```

`/work2/yuka97524/Temma/26evidenceModeler` is a directory where files such as `x...` and `partitions_list.out` exist.  

> USAGE

```
evm_create_sh.sh [absolute path to the file in PREPARATION] [absolute path to execute_EVM_commands.pl]
```

Here, you might have to check whether a directory named `execute_EVM_commands` was successfully created in the parent directory, and whether splited job scripts for PBS in it were properly excuted by `qstat`.

> EXAMPLE
```
evm_create_sh.sh /work2/kataoka/gene_prediction_azami/evm/pbs_job_comment.txt /home/kataoka/anaconda3/envs/evm/opt/evidencemodeler-1.1.1/EvmUtils/execute_EVM_commands.pl
```
