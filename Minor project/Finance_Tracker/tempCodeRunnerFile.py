@app.route("/add", methods=["POST"])
# def add():
#     data = request.json
#     conn = sqlite3.connect("finance.db")
#     cursor = conn.cursor()

#     cursor.execute(
#         "INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
#         (data["type"], data["category"], data["amount"], data["date"])
#     )

#     conn.commit()
#     conn.close()
#     return jsonify({"message": "Added successfully"})