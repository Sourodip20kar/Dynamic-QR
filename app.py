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

# app.py (Update this function)

@app.route("/newyear")
def christmas_theme():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Merry Christmas!</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background-color: black;
                height: 100vh; /* Full viewport height */
                width: 100vw;  /* Full viewport width */
                overflow: hidden; /* Prevent scrolling */
                display: flex;
                justify-content: center;
                align-items: center;
            }

            /* --- THE VIDEO PLAYER --- */
            #bg-video {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                
                /* This is the Magic Line: */
                /* 'cover' makes it fill the screen without stretching/distorting */
                object-fit: cover; 
                
                /* Keeps the video centered so the main content isn't cut off */
                object-position: center; 
                
                z-index: -1; /* Puts video behind the button */
            }

            /* --- UNMUTE BUTTON (Floating & Stylish) --- */
            .btn-container {
                position: absolute;
                bottom: 80px; /* Positioned for thumb reach on mobile */
                z-index: 10;
                text-align: center;
                width: 100%;
                animation: float 3s ease-in-out infinite;
            }

            .btn {
                background: rgba(255, 255, 255, 0.25); /* Frosted Glass Effect */
                border: 1px solid rgba(255, 255, 255, 0.6);
                color: white;
                padding: 14px 32px;
                font-size: 1.1rem;
                font-weight: 600;
                border-radius: 50px;
                cursor: pointer;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                backdrop-filter: blur(12px); /* Blurs background behind button */
                -webkit-backdrop-filter: blur(12px); /* Safari support */
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
            }

            .btn:active {
                transform: scale(0.95);
                background: rgba(255, 255, 255, 0.4);
            }
            
            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
                100% { transform: translateY(0px); }
            }
        </style>
    </head>
    <body>

        <video autoplay loop muted playsinline id="bg-video">
            <source src="/static/new_year.mp4" type="video/mp4">
            Your browser does not support HTML5 video.
        </video>

        <div class="btn-container" id="soundBtn">
            <button class="btn" onclick="unmuteVideo()">🔊 Tap for Sound</button>
        </div>

        <script>
            function unmuteVideo() {
                var vid = document.getElementById("bg-video");
                var btnContainer = document.getElementById("soundBtn");
                
                // Unmute and ensure play
                vid.muted = false;
                vid.play();
                
                // Smoothly fade out the button
                btnContainer.style.transition = "opacity 0.5s";
                btnContainer.style.opacity = "0";
                
                // Remove button from layout after fade
                setTimeout(() => { btnContainer.style.display = 'none'; }, 500);
            }
        </script>

    </body>
    </html>
    """
if __name__=="__main__":
    app.run(debug=True, port=5000)