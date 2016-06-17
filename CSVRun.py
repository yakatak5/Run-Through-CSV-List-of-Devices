import paramiko
import csv

with open('IPlist.csv') as csvfile: #Example file
	reader = csv.DictReader(csvfile)
	a = [line for line in reader]

		#open file and create a list of devices and info as a dictionary


for dicts in a:
	print "  " + dicts['address']
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())
	ssh.connect(dicts['address'] , username= dicts['username'] , password= dicts['password'])
	stdin, stdout, stderr = ssh.exec_command("sh version")
	out = [line for line in stdout.readlines()]
	for number in range(22,23):
		print out[number] 
		#Adjust range to print out only exactly what is needed
		
#logs in and checks version for every address in csv file