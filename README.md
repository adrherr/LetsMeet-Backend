# LetsMeet-Backend
Backend for LetsMeet

# To Run
Debian Package Installation
```bash
sudo apt install git
sudo apt install python3
sudo apt install python3-pip
sudo apt install mariadb-server
sudo apt install libmariadb3 libmariadb-dev
```

1. Clone repo
```git
git clone https://github.com/adrherr/LetsMeet-Backend.git
```
or (for ssh)
```git
git clone git@github.com:adrherr/LetsMeet-Backend.git
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. You need to have a MariaDB password setup

* Skip to step 3: [MariaDB Setup](https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-20-04)

4. Connect to MariaDB and run script

MariaDB [(none)]> ```source init.sql```

5. Fill out config in private.json
* Note: If you don't want to accidently push changes from this file
```git
git update-index --assume-unchanged private.json
```

6. Start website
```py
python3 app.py
```

# Usage
To get info about one event specifiy the eventid
```
/get?event=1
```

To get info about all events
```
/get?event=all
```

To get info about one user specify the userid
```
/get?user=4 
```

To get info about all users
```
/get?user=all
```