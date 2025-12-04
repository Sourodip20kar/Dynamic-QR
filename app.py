from flask import Flask, redirect, request, jsonify
from config import ADMIN_SECRET
from config import r, QR_ID

app=Flask(__name__)

@app.route("/qr")
def qr_redirect():
    qr_id = request.args.get("id")
    if not qr_id:
        return "Missing qr id", 400
    
    link= r.get(qr_id)
    if not link:
        return "No active link set for this qr", 404
    
    return redirect(link)

@app.route("/update", methods=["POST","GET"])
def update_link():
    user_secret= request.args.get("secret")
    if user_secret!=ADMIN_SECRET:
        return jsonify({"error": "Unauthorized. Wrong secret key."}), 401
    
    qr_id = request.args.get("id")
    new_link = request.args.get("url")

    if not qr_id or not new_link:
        return jsonify({"error":"Missing id or url"}), 400
    
    r.set(qr_id,new_link)
    return jsonify({"success":True, "message":f"updated {qr_id} -> {new_link}"})

@app.route("/status")
def status():
    qr_id= request.args.get("id", QR_ID)
    current = r.get(qr_id)
    return jsonify({"id":qr_id, "current_link":current})


if __name__=="__main__":
    app.run(debug=True, port=5000)