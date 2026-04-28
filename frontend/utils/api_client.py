def get_health():
    try:
        response = httpx.get(f"{BASE_URL}/health")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}