import sys
import glob

# job_file_temp = sys.argv[1]
execute_EVM_commands_path = sys.argv[1]
devision_num = 10
# job_file_temp = '/work2/kataoka/gene_prediction_azami/evm/pbs_job_comment.txt'
# execute_EVM_commands_path = '/home/kataoka/anaconda3/envs/evm/opt/evidencemodeler-1.1.1/EvmUtils/execute_EVM_commands.pl'

x_file = glob.glob('../x*')
# x_file = glob.glob('/work2/yuka97524/Temma/26evidenceModeler/x*')
# print(x_file)
count = 0
# with open(job_file_temp, 'r') as j:
for i in range(0, len(x_file), devision_num):
    devided_x_file = x_file[i : i + devision_num]
    write_file_path = '../execute_EVM_commands/EVM_run_list_' + str(count)
    # print(devided_x_file)
    for x in devided_x_file:
        with open(write_file_path, 'a') as f:
            # for line_j in j:
            #     f.write(line_j)
            line = execute_EVM_commands_path + ' ' + x + '\n'
            f.write(line)
    count += 1