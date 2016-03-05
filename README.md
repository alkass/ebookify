# ebookify
<i>ebookify</i> is a web-based electronic library project written on top of the [django web framework](#).

# Installing the Required Package(s)
```bash
  sudo pip install -r requirements.txt
```

# Creating the Database (first use only)
```bash
  python manage.py makemigrations
  
  python manage.py migrate
```

# Creating an Admin Account
```bash
  python manage.py createsuperuser
```

# Running the Library
```bash
  sudo python manage.py runserver 0.0.0.0:80
```
Your library should now be running at [localhost:80](http://localhost).

Your admin panel is available at [localhost:80/admin](http://localhost/admin).

# Author
[Fadi Hanna Al-Kass](http://github.com/alkass)
