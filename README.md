### portfolio-project

## Python django deployment from GitHub to aws ec2
#### steps for AWS
1. Login AWS
2. Go to EC2
3. Create Instance and select Ubuntu Server 16.04 LTS
4. chose by default t2.micro(free tier)
5. Click review and next
6. click on edit security group and chose Type-> shh and source --> My ip,  again chose add rule Type-> http and source --> AnyWhere and all are default in the same section.
7. Chose review and launch
8. create new pair and download

#### linux or mac
1. cd Downloads/
2. mv zillows.pem ~/Desktop/
3. cd ..
4. cd desktop

5. chmod

6. ssh

7. yes


#### Windows
1. Download Puttygen and Putty
2. open puttygen click on load and chose key pair that donloaded when ec2 created
3. click on generate private key and save 
4. Open putty
5. session section there are two section host(put public DNS from the ec2 instance running and port 22)
6. left side of putty click on SSH and then Auth and chose private key which is generate from step 3
7. Click open
8. Now the terminal open
9. Type login id:ubuntu
10. follow command below


#### Commands
1. sudo apt-get update
2. sudo apt-get install python-pip python-dev nginx git

3. Y

4. sudo apt-get update
5. sudo pip3 install virtualenv
5. git clone https://github.com/sawrupesh04/portfolio-project
6. cd portfolio-project
7. virtualenv venv
8. source venv/bin/activate
9. pip3 install -r requirements.txt
10. pip3 install django bcrypt django-extensions
11. pip3 install gunicorn
12. cd zillow
13. sudo vim settings.py (Inside settings.py modify these lines allowed host public IP address I for INSERT) 

ALLOWED_HOSTS = ['54.161.147.133']

add the line below to the bottom of the file

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

Save your changes and quit. ESC :wq

14. cd .. 
15. python3 manage.py collectstatic
16. gunicorn --bind 0.0.0.0:8000 portfolio.wsgi:application

17. ctrl+c

18. sudo vim /etc/systemd/system/gunicorn.service


[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/portfolio-project
ExecStart=/home/ubuntu/portfolio-project/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/portfolio-project/portfolio.sock portfolio.wsgi:application
[Install]
WantedBy=multi-user.target

ESC :wq

19. sudo systemctl daemon-reload
20. sudo systemctl start gunicorn
21. sudo systemctl enable gunicorn
22. sudo vim /etc/nginx/sites-available/portfolio

server {
  listen 80;
  server_name 54.161.147.133;
  location = /favicon.ico { access_log off; log_not_found off; }
  location /static/ {
      root /home/ubuntu/portfolio-project;
  }
  location / {
      include proxy_params;
      proxy_pass http://unix:/home/ubuntu/portfolio-project/portfolio.sock;
  }
}

ESC :wq

23. sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled
24. sudo nginx -t
25. sudo rm /etc/nginx/sites-enabled/default
26. sudo service nginx restart

27. http://54.161.147.133;


### congratulations
