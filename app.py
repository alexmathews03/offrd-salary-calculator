from flask import Flask, render_template, request, jsonify
from salary_calculator import calculate_monthly_salary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json() or {}
        ctc = float(data.get("annual_ctc", 600000))
        result = calculate_monthly_salary(ctc)
        return jsonify({"success": True, "data": result})
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": "Invalid request"}), 500

if __name__ == "__main__":
    print("Starting Offrd Salary Calculator Web App at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
