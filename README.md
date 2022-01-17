# college_webapp
 College Web App

1.	App Overview 
This Web App is designed to provide some static information about college to outside world and a student portal to handle their day-to-day queries.
2.	Features 
The Web App has the following features:
	BOT: Web app has a bot which is designed to help visitors on the website by answering FAQs.
	The Web App has a student portal on which the registered students will be able to query information like results, fee dues, class schedules, attendance records etc.  from college information systems.
3.	How to test (see demo)
1)	Start the Web Server:
Click the below URL
NOTE: if click does not work copy-paste the below URL

https://xyzc.azurewebsites.net/api/HttpTrigger1?code=6dTMdAlCgQApt9cDBxmpUjSOQRtkwcma8b8JnkHuD1b34GM9OaULHg==
The server startup may take time so please wait for 5 minutes after you click the above URL,
sometimes it may return “time out error“ but you may ignore it and after 5 minutes click (or copy-paste in browser) on the below link to access the web app
http://xyzapp.centralindia.cloudapp.azure.com:8080/home
This will show XYZ college home page.

2)	TO access Student portal 

In order to access the Student Portal you may use following Test user credentials :

USER  NAME	PASSWORD
Raj	1_r
Betty	2_b

3)	After successful authentication you will be directed to the Student Portal.
In case you face an issue in accessing the App please write to: tanejanandika@gmail.com for support.
4.	Technology Platform
The following technologies are used in the project:
1)	Python version:3.8
2)	Django
3)	Azure 
I.	Linux VM (to host Web App workload)
II.	Azure Database for MySQL flexible server
III.	Web app BOT (including QnA maker)
IV.	Function App (to automate start/stop of VM and Database)
V.	Persistent Storage for VM 
VI.	Microsoft.Compute/images
VII.	PowerShell
4)	Repository: GitHub 
