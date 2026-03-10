from quart import Quart, jsonify

app = Quart(__name__)

@app.route("/")
async def home():
    return {"message": "Podman API running"}

@app.route("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)