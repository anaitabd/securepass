# 🔐 SecurePass – Passwordless Authentication API (Django + Djoser)

SecurePass is a production-ready authentication API that supports:
- ✅ Passwordless login via magic link (email)
- ✅ Classic JWT login with Djoser
- ✅ Easy integration into any web/mobile app

Built with **Django**, **DRF**, **Djoser**, and **JWT**.

---

## 🚀 Features

- 🔐 Login via magic link (no password)
- 📩 Token sent to user’s email
- 🧾 Access + Refresh JWT tokens
- ⏱️ Expiring one-time-use tokens
- 📚 Djoser integration for optional classic login/reset flows

---

## 🛠️ Tech Stack

- Django 4+
- Django REST Framework
- Djoser
- SimpleJWT
- SMTP (or SendGrid, Mailgun, etc.)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/securepass.git
cd securepass
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver



⸻

⚙️ .env Configuration

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password



⸻

📩 Email Setup

You can use Gmail SMTP or SendGrid. Make sure to allow app passwords or disable 2FA if using Gmail.

⸻

📖 API Use Cases

1. 📬 Request Magic Link

POST /auth/request-magic-link/

{
  "email": "user@example.com"
}

✅ Response:

{
  "detail": "Magic link sent"
}

	•	Sends a one-time-use token to user’s email
	•	Token expires after 10 minutes

⸻

2. 🔓 Verify Magic Link

GET /auth/verify-magic-link/?token=123e4567-e89b-12d3-a456-426614174000

✅ Response:

{
  "refresh": "long.jwt.refresh.token",
  "access": "short.jwt.access.token"
}

❌ Invalid or used token:

{
  "error": "Token expired or already used"
}



⸻

3. 🔁 Refresh JWT Token

POST /auth/jwt/refresh/

{
  "refresh": "your_refresh_token"
}

✅ Response:

{
  "access": "new_access_token"
}



⸻

4. 👤 Get Current User

GET /auth/users/me/
	•	Requires Authorization: Bearer <access_token>

⸻

5. ✅ Classic Djoser Endpoints (Optional)

Endpoint	Method	Description
/auth/users/	POST	Register a user
/auth/jwt/create/	POST	Login via password
/auth/jwt/refresh/	POST	Refresh token
/auth/users/reset_password/	POST	Send password reset email
/auth/users/reset_password_confirm/	POST	Reset password



⸻

🧪 Testing

Use Postman or Swagger UI:

python manage.py runserver
# Navigate to http://localhost:8000/docs/ if using drf-yasg (optional)



⸻

📦 Deployment

To deploy with Docker:

docker build -t securepass .
docker run -p 8000:8000 securepass



⸻

✅ TODO / Improvements
	•	Add rate limiting to prevent abuse
	•	Add support for phone-based magic links (SMS)
	•	Create a simple frontend for testing
	•	Admin dashboard for managing users

⸻

👨‍💻 Author

Made by @anaitabd – feel free to reach out!

⸻