# Script_For_knowing_the_Congestion_in_Network

// Author - Pranjal Gupta


$$
The file ' newnetscript ' is a linux shell script that is used to measure the network congestion. The Script is Open Source to use and build the further applicability of the commands in linux.
It first creates a set of IP address from the initial value of IP address like 192.168.16.1 and on execution of the command saves the record of the set of IP addresses upto 255 in the Postgres Table.
These are the IP Address that are we validate belong to our set of Network IP.
Then from the Available Network to which the system is connected the script finds all the set of Alive IP addresses. Each of these IP addresses found alive is matched with the IP address that belong to our set.
If the IP Address belong to our set then the Corresponding value of the TTL is stored by running a Ping Command over the IP. Thus for each IP that validates the set of IP addresses and is alive right now the corresponding 
TTL value is stored in Postgres Table.

Now, 

Python comes into the Play....
Python works over just the manual interpretation of the data. The store TTL for each IP Address is collected from the row. Given to a dictionary and the average and the first index of the value of TTL at which it becomes 0
is taken to interpret the error or congestion where it first occured. This result is displayed on the terminal console.

Matplotlib

Graphs look pretty good when their charmness is used to read the data. Matplotlib is used pretty awesomely sketch the pie charts for the TTL values interpretation. Where the TTL collapse with the other or multiple TTL values
collapse definately the network did not gave the TTL coz of the Congestion and for the 0 after some value and before some value there might be the network breakage or high loop for the unresponsive behavior of the node. 
So, the script is not just a one time run process it with re-run again after the 20 seconds pause, re-create the column again, re-update the average and congestion point again and re-update the piechart.

Next is the Javascript into the frame that manipulates the images and place then in a grid one after the other, because we would love to have UI atleast somewhere.

Linux is pretty cool.. and amazing !! Crafted with my love Python them both look pretty lovely. Oops I forgot Postgres.. Hye, Thanks to you too !!
And Yes matpotlib .. you are a blessing !!

$$

## Pre-requisites
   1. Configure Postgres, Python and matplotlib as per your OS. There are Explainations on the Stackoverflow for each of them.
   2. If ( newbie Just like me ) learn linux commands related to cropping and extracting the output of linux command like that of ping command.
   3. Also, Read Postgres and Matplotlib implementation ( for those un-familior ones)
   4. Please either make newnetscript executable or run directly on shell( your choice bash, sh or .. whatever). Same for python script.
