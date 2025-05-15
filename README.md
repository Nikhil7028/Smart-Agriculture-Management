It seems like I can’t do more advanced data analysis right now. Please try again later.

However, you can copy and paste the formatted content below directly into your `README.md` file:

---

```markdown
# 🌾 Smart Agriculture Portal

A Django-based web application for crop recommendation, worker management, and government scheme integration to support farmers and agricultural officers.

---

## 🏠 Home Page

The homepage allows users to:

- Access crop recommendation  
- View available workers  
- Navigate to different modules (dashboard, profile, login)  
- Access weather information  

![Home Screenshot](Screenshot%202025-05-08%20154252.png)

---

## 📌 Features

- 🌱 **Crop Recommendation** using ML model (Decision Tree Classifier)  
- 👨‍🌾 **Farmer and Worker Registration & Login**  
- 👷 **Availability Status Toggle** for workers  
- 📍 **Location-Based Filtering** (District → Sub-District → Village)  
- 🌐 **Weather Forecast** for selected city  
- 📑 **Government Scheme Management** (Add, View)  
- 🧪 **Unit Testing** and CSRF protection  

---

## 🛠 Technologies Used

| Technology       | Purpose                     |
|------------------|-----------------------------|
| Django           | Backend Framework           |
| SQLite           | Lightweight Database        |
| HTML/CSS/Bootstrap | Frontend Design          |
| Scikit-learn     | Machine Learning model      |
| Joblib           | Model Serialization         |
| JavaScript       | Form validations & dropdowns|
| Font Awesome     | Icons                       |
| W3Schools, Stack Overflow | Learning Resources |

---

## 📁 Project Structure

```
agriculture_portal/
├── ml_model/
│   └── crop_recommendation_model.pkl
├── templates/
│   ├── home.html
│   ├── dashboard.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── app/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
└── manage.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Nikhil7028/Smart-Agriculture-Management.git
cd Smart-Agriculture-Management
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Load ML Model & Run the Server
```bash
python manage.py runserver
```

### 4. Visit Application
Go to: `http://localhost:8000`

---

## ✅ Usage Notes

- Workers can **toggle their availability** from the dashboard using a toggle switch.  
- Officers can **add new government schemes** via their dashboard.  
- Farmers can **view available workers** and **get crop recommendations**.  
- **Weather info** can be retrieved from the "Weather" tab by entering a valid city name.  

> 💡 *Note*: For the weather feature, ensure you create a `weather.html` template and securely call the API from the backend to avoid exposing your API key.
```

Let me know if you'd like me to email or export this as a downloadable `.md` file later.