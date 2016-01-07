import sys
import argparse

parser = argparse.ArgumentParser(description='parse arguments for labgrid')
parser.add_argument('jobname', metavar='name', type=str, nargs='+',help='name of the executable file')
parser.add_argument('outfile', metavar='out', type=str, nargs='+',help='name of the output file')
parser.add_argument('executable_file', metavar='exec', type=str, nargs='+',help='name of the executable file')
parser.add_argument('filetype', metavar='ft', type=str, nargs='+',help='file extention of the executable file')
parser.add_argument('user_args', metavar='ua', type=list, nargs='+',help='List of tuples representing the user arguments to run jobs with')
parser.add_argument('jobid', metavar='ft', type=int, nargs='+',help='unique job id integer')


parser.parse_args(jobname,outfile,executable_file,filetype,user_args)

jobname = parser.jobname
outfile = parser.oufile
executable_file = parser.executable_file
filetype = parser.filetype
arguments = parser.user_args
jobid=parser.jobid

os.makedirs("/Users/condor/Desktop/%s_%s" %jobname,jobid)
writer = open("%s.sub" %jobname, 'w')
writer.write("should_transfer_files = YES\nwhen_to_transfer_output = ON_EXIT\n")
writer.write("\ntransfer_out_files = $(initialdir)/fact_out.txt\ninitialdir = /Users/condor/Desktop/%s/%s_$(jobnum)" %jobname)
writer.write("executable=/Users/condor/Desktop/%s/%t\n" %jobname,executablefile)
writer.write("output = $(initialdir)/%s.out\n" %jobname)
writer.write("error = $(initialdir)/%s.err\n" %jobname)
writer.write("log = $(initialdir)/%s.log\n" %jobname)
writer.write("\n\n")
for arg in arguments:
	writer.write("arguments=%s\n" %arg)
	writer.write("queue\n")
