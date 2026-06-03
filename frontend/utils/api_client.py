import httpx

BASE_URL = "http://127.0.0.1:8000"

def register(username, password):
    try:
        response = httpx.post(f"{BASE_URL}/auth/register", params={"username": username, "password": password})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def login(username, password):
    try:
        response = httpx.post(f"{BASE_URL}/auth/login", data={"username": username, "password": password})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_expenses(token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = httpx.get(f"{BASE_URL}/expenses", headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def add_expense(token, amount, category, note=""):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = httpx.post(f"{BASE_URL}/expenses", headers=headers, params={"amount": amount, "category": category, "note": note})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_income(token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = httpx.get(f"{BASE_URL}/income", headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def add_income(token, amount, source):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = httpx.post(f"{BASE_URL}/income", headers=headers, params={"amount": amount, "source": source})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_summary(token, month):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = httpx.get(f"{BASE_URL}/summary", headers=headers, params={"month": month})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_categories(token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = httpx.get(f"{BASE_URL}/categories", headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}