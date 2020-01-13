#!/usr/bin/env python3.6
import time

#Create file brief with summary of result backup scripts 
open('/home/user/scripts/result/brief', 'w').close()

tests_results_summary = open('/home/user/scripts/result/brief', 'a')
tests_results_summary.write('\n Script start at ')
tests_results_summary.write(time.strftime("%H:%M:%S %d-%m-%Y "))



def output_last_line(path, log_identificator):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        tests_results_summary.write('\n')
        tests_results_summary.write('Result for backup of ')
        tests_results_summary.write(log_identificator)
        tests_results_summary.write(' is ')
        tests_results_summary.write(last_line)
        tests_results_summary.write('\n')


output_last_line('/path_to_logs_of_backup/logs/asa.log', 'ASA')
output_last_line('/path_to_logs_of_backup/logs/ME.log', 'ME')
output_last_line('/path_to_logs_of_backup/logs/sw.log', 'SW1')



tests_results_summary.close
