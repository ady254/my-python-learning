
import time

def fetch_user(user_id):
    time.sleep(0.5)  # pretend this is a slow database / API call
    print(f"HIT THE DATABASE for {user_id}")
    return {"id": user_id, "name": f"user_{user_id}"}


