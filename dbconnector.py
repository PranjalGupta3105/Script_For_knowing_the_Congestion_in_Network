#!/usr/bin/python
import psycopg2
import sys
import numpy as np
import matplotlib.pyplot as plt
import webbrowser

conn = None

try:
	conn=psycopg2.connect(host="localhost",user="postgres",database="firstdb");

	cur=conn.cursor()
	cur.execute("select * from data ORDER BY ip_addresses;")
	
	ttl_value=[]
	

	while True:
		
		row = cur.fetchone()
		
		if row == None:
			break
		
 
                	print "\n"
			
		else:
			ip=row[0]

                	average=(row[1]+row[2]+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+row[11])/11

                	print ("The Average for ",ip," is ",average)



                	if (row[1] == 0):
                                	print "There is a problem at first second"
                	elif (row[2] == 0):
                                	print "There is a problem at second second"
                	elif (row[3] == 0):
                                	print "There is a problem at third second"
                	elif (row[4] == 0):
                                	print "There is a problem at fourth second"
                	elif (row[5] == 0):
                                	print "There is a problem at fifth second"
                	elif (row[6] == 0):
                                	print "There is a problem at sixth second"
                	elif (row[7] == 0):
                                	print "There is a problem at seventh second"
	               	elif (row[8] == 0):
                                	print "There is a problem at eighth second"
	               	elif (row[9] == 0):
                                	print "There is a problem at nineth second"
                	elif (row[10] == 0):
                                	print "There is a problem at tenth second"
			elif (row[11] == 0):
                                        print "There is a problem at eleventh second"


		  	#print ("The ",ip," system was Up all the Time")

			#ttl_value=[]
			#for i in range(1,5):
                    	#		     ttl_value.append(row[i])
                        

	                #x=[1,21,42,62]
        	        #for i in range(0,9):
					#col="C"+str(i)
			#execfile('plotgraph.py')
					#i++
					#break
			#print (x)
                	#print(ip,ttl_value)
                	#labelname='Bar Plot for Corresponding value of ttl for the IP'+ip
			#print(labelname)
			#for i in range(1,12):
			#plt.bar(x,ttl_value)
			#labelname=''
			#print(labelname)
			#plt.xlabel('seconds')
                	#plt.ylabel('TTL Hit')
                	#plt.title(ip, size=14)
                	#plt.legend()
                	#filename='Desktop/pielogs/'+ip+'.png'
                	#plt.savefig(filename, format='png')
			#del x[:]
			#del ttl_value[:]
			#print(ttl_value)

			print "\n"
			
			

			#---------------------Entries for plotting the piechart ---------
			data = [row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]]
                     	plt.figure(num=1, figsize=(6, 6))
                     	plt.axes(aspect=1)
                     	label='chart for '+ip
                     	plt.title(label, size=14)
                     	plt.pie(data, labels=('ttl 1', 'ttl 2', 'ttl 3','ttl 4','ttl 5','ttl 6','ttl 7','ttl 8','ttl 9','ttl 10','ttl 11'))
                     	filename='Desktop/pielogs/'+ip+'.png'
                     	plt.savefig(filename, format='png')
	        #----------------------------------------------------------------------------------------------------
	        	
			#f=open('/root/Desktop/summaryreport.html','w')
			#content="""<html><head><title>My Summary Report</title></head><body><img src="192.168.16.1.png"/></body></html>"""
			#f.write(content)
			#f.close()
			#execfile('/root/Desktop/abcde.py')
			#webbrowser.open_new_tab('/root/Desktop/summaryreport.html')
		
	webbrowser.open_new('/root/Desktop/summaryreport.html')	
	
except psycopg2.DatabaseError, e:
	print 'Error %s' % e
	sys.exit(1)


finally:
	if conn:
		conn.close()
