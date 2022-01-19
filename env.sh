date >> /home/ntvm/envtest.txt
echo "ENV Script for XYZ App Started" >> /home/ntvm/envtest.txt
cd /home/ntvm/app
. /home/ntvm/app/venv/bin/activate  >> /home/ntvm/envtest.txt
cd /home/ntvm/app/venv/college_webapp/
#nohup python /home/ntvm/app/venv/college_webapp/manage.py runserver 0:8080 &
exec nohup python /home/ntvm/app/venv/college_webapp/manage.py runserver 0:8080
#> /home/ntvm/xyzapp.log
#</dev/null &>/dev/null &
ps -aef | grep "python" >> /home/ntvm/envtest.txt
#sleep 180
echo "ENV Script for XYZ App end" >> /home/ntvm/envtest.txt