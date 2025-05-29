from pyngrok import ngrok

def start_ngrok(port=8080):
    print("Starting Ngrok tunnel...")
    public_url = ngrok.connect(port, "http")
    print(f"Your public URL: {public_url}")
    return public_url
