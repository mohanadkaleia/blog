from app import app

if __name__ == "__main__":
    # Not 5000: macOS Control Center (AirPlay Receiver) squats on it and answers
    # every request with a 403, which browsers then cache.
    app.run(debug=True, port=5001)
