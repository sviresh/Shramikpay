import os
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from supabase import create_client

# ------------------------------
# Supabase config
# ------------------------------
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://jjzxnguvnlfvxljyqiye.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqenhuZ3V2bmxmdnhsanlxaXllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY2Mjk0NDksImV4cCI6MjA3MjIwNTQ0OX0.f7hCWxUdwTIUotskNjAtKIo-Tae7LCYZpiGowZvpAL0")  # Must be service_role key

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ------------------------------
# Demo client + admin
# ------------------------------
def create_demo_client_and_admin():
    now = datetime.now()
    demo_days = 15
    license_key = "DEMO-12345"
    license_expiry = (now + timedelta(days=demo_days)).date().isoformat()  # Convert to string

    # Demo client
    demo_client = supabase.table("clients").select("*").eq("id", 1).execute()
    if demo_client.data:
        expiry = demo_client.data[0].get("license_expiry")
        if expiry and expiry < now.date().isoformat():
            supabase.table("clients").update({
                "license_expiry": license_expiry,
                "is_active": True
            }).eq("id", 1).execute()
            print(f"✅ Demo license refreshed until {license_expiry}")
        else:
            print(f"✅ Demo license valid until {expiry}")
    else:
        supabase.table("clients").insert({
            "id": 1,
            "name": "Demo Client",
            "email": "demo@example.com",
            "phone": "9999999999",
            "address": "HQ",
            "is_active": True,
            "license_key": license_key,
            "license_expiry": license_expiry,
            "max_users": 5
        }).execute()
        print(f"✅ Demo client created with license until {license_expiry}")

    # Admin user
    admin_user = supabase.table("users").select("*").eq("username", "admin").eq("client_id", 1).execute()
    if not admin_user.data:
        hashed_pw = generate_password_hash("admin")
        supabase.table("users").insert({
            "username": "admin",
            "email": "admin@example.com",
            "role": "admin",
            "password": hashed_pw,
            "client_id": 1,
            "is_active": True
        }).execute()
        print("✅ Demo admin user created (username: admin, password: admin)")
    else:
        print("✅ Demo admin user already exists")


if __name__ == "__main__":
    create_demo_client_and_admin()
    print("🚀 Supabase client initialization complete!")