# portfolio-project

Python django deployment from GitHub to aws ec2

cd Downloads/
mv zillows.pem ~/Desktop/
cd ..
cd desktop

chmod

ssh

yes

sudo apt-get update
sudo apt-get install python-pip python-dev nginx git

Y

sudo apt-get update
sudo pip3 install virtualenv
git clone https://github.com/mruanova/zillow.git
cd zillow
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install django bcrypt django-extensions
pip3 install gunicorn
cd zillow
sudo vim settings.py


# Inside settings.py modify these lines allowed host public IP address I for INSERT

i
cd 

ALLOWED_HOSTS = ['13.59.206.93']

# add the line below to the bottom of the file

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

Save your changes and quit. ESC :wq

cd .. 
python3 manage.py collectstatic
gunicorn --bind 0.0.0.0:8000 portfolio.wsgi:application

ctrl+c

sudo vim /etc/systemd/system/gunicorn.service

i

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

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo vim /etc/nginx/sites-available/portfolio

i

server {
  listen 80;
  server_name 54.161.147.136;
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

sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart

http://54.161.147.136;
