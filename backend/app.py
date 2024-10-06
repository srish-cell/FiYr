from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Replace with the actual Gemini API endpoint
GEMINI_API_URL = "https://api.gemini.com/v1/analyze"

# Replace with your Gemini API key
GEMINI_API_KEY = "AIzaSyDC4S2ykQO2yP62_nNe-bHiaB4gp-xA0A0"


def analyze_with_gemini(nmap_output):
    """Sends Nmap output to Gemini API for analysis."""
    headers = {
        "Authorization": f"Bearer AIzaSyDC4S2ykQO2yP62_nNe-bHiaB4gp-xA0A0",
        "Content-Type": "application/json",
    }

    payload = {"nmap_output": nmap_output}

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for non-200 status codes

        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to get analysis from Gemini: {e}"}


@app.route('/scan', methods=['POST'])
def scan():
    target = request.json.get('target')
    if not target:
        return jsonify({"error": "Target is required"}), 400

    # Use external Nmap tool (not recommended within container)
    # Consider installing Nmap separately or exploring Nmap libraries
    # This example demonstrates the flow, but replace with your preferred method

    # Replace with your Nmap scanning command (e.g., subprocess or external tool)
    command = f"nmap -A -T4 {target}"  # Example command, adjust based on your environment
    nmap_output = "Simulated Nmap output (replace with actual output)"  # Placeholder

    try:
        # Simulate successful Nmap scan (replace with actual execution)
        # result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # nmap_output = result.stdout.decode()
        pass
    except Exception as e:  # Handle potential Nmap execution errors
        return jsonify({"error": f"Nmap scan failed: {e}"}), 500

    gemini_report = analyze_with_gemini(nmap_output)

    return jsonify({"output": gemini_report})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
