from django.core.mail import send_mail

def send_magic_link(email, token):
    link = f"http://localhost:8000/auth/verify-magic-link/?token={token}"
    send_mail(
        'Your Login Link',
        f'Click to login: {link}',
        'noreply@securepass.dev',
        [email],
        fail_silently=False,
    )