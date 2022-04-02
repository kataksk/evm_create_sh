job_file_temp=$1
execute_EVM_commands_path=$2
mkdir ../execute_EVM_commands
python evm_create_sh.py $2
for pathfile in `ls ../execute_EVM_commands/*`; do
    cat $1 $pathfile > ../execute_EVM_commands/$pathfile'.sh'
done
find ../execute_EVM_commands -type f | grep -v -E '*.sh' | xargs rm -rf
sh_file=(`find ../execute_EVM_commands -type f`)
for i in ${sh_file[@]}; do
qsub $i
done
