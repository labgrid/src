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
args = vars(parser.parse_args())

jobname = args.jobname
outfile = args.oufile
executable_file = args.executable_file
filetype = args.filetype
arguments = args.user_args
jobid=args.jobid

'''TODO: decide on overall execute directory'''
initialpath=/Users/condor/Desktop/%s_%s" %(jobname,jobid)
os.makedirs(initialpath)
writer = open("%s.sub" %jobname, 'w')

writer.write("should_transfer_files = YES\nwhen_to_transfer_output = ON_EXIT\n")
writer.write("\ntransfer_out_files = $(initialdir)/%s.txt\ninitialdir = %s" %(outfile,jobname,initialpath))
writer.write("executable=%s\n" %(initialpath,executablefile))
writer.write("output = $(initialdir)/%s.out\n" %jobname)
writer.write("error = $(initialdir)/%s.err\n" %jobname)
writer.write("log = $(initialdir)/%s.log\n" %jobname)
writer.write("\n\n")
for arg in arguments:
	writer.write("arguments=%s\n" %arg)
	writer.write("queue\n")
