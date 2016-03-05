# ebookify
<i>ebookify</i> is a web-based electronic library project written using the django web framework.

# How To

### 1. Install the Required Package(s)
```bash
  sudo pip install -r requirements.txt
```

### 2. Create the Database (first use only)
```bash
  python manage.py makemigrations
  
  python manage.py migrate
```

### 3. Create an Admin Account
```bash
  python manage.py createsuperuser
```

### 4. Run the Library
```bash
  sudo python manage.py runserver 0.0.0.0:80
```
Your library should now be running at [localhost:80](http://localhost).

Your admin panel is available at [localhost:80/admin](http://localhost/admin).

# Author
[Fadi Hanna Al-Kass](http://github.com/alkass)
