from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>3xe.q</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: Arial, Helvetica, sans-serif;
      background: #000;
      color: #ffffff;
      overflow: hidden;
    }

    .background-video {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: -2;
    }

    .overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.35);
      z-index: -1;
    }

    .exclusive-link {
      text-decoration: none;
      color: inherit;
      text-align: center;
      transition: transform 0.25s ease, filter 0.25s ease;
    }

    .exclusive-link:hover {
      transform: scale(1.06);
      filter: drop-shadow(0 0 22px rgba(255, 0, 150, 0.75));
    }

    .icon {
      width: 190px;
      height: 190px;
      border-radius: 22px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 22px;
      background: rgba(255, 255, 255, 0.12);
      border: 2px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.45);
      backdrop-filter: blur(8px);
      overflow: hidden;
    }

    .logo {
      width: 72%;
      height: 72%;
      object-fit: contain;
      display: block;
    }

    .text {
      font-family: Impact, Haettenschweiler, "Arial Black", sans-serif;
      font-size: 34px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 2px;
      text-shadow: 0 4px 20px rgba(255, 0, 150, 0.85), 0 3px 18px rgba(0, 0, 0, 0.9);
    }


    .age-modal {
      position: fixed;
      inset: 0;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      background: rgba(0, 0, 0, 0.72);
      z-index: 10;
    }

    .age-modal.show {
      display: flex;
    }

    .modal-card {
      width: min(92vw, 420px);
      padding: 28px;
      text-align: center;
      border-radius: 24px;
      background: rgba(18, 10, 28, 0.94);
      border: 1px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 25px 80px rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(12px);
    }

    .modal-title {
      font-family: Impact, Haettenschweiler, "Arial Black", sans-serif;
      font-size: 30px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 12px;
    }

    .modal-text {
      font-size: 16px;
      line-height: 1.45;
      color: rgba(255, 255, 255, 0.88);
      margin-bottom: 22px;
    }

    .modal-actions {
      display: flex;
      gap: 12px;
      justify-content: center;
    }

    .modal-button {
      min-width: 120px;
      border: 0;
      border-radius: 999px;
      padding: 13px 18px;
      cursor: pointer;
      font-size: 15px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #fff;
      transition: transform 0.2s ease, filter 0.2s ease;
    }

    .modal-button:hover {
      transform: translateY(-2px);
      filter: brightness(1.12);
    }

    .yes-button {
      background: linear-gradient(135deg, #ff007a, #7b2cff);
    }

    .no-button {
      background: rgba(255, 255, 255, 0.16);
      border: 1px solid rgba(255, 255, 255, 0.25);
    }

    .age-warning {
      display: none;
      margin-top: 16px;
      color: #ff8fc7;
      font-size: 14px;
      font-weight: 700;
    }

    .age-warning.show {
      display: block;
    }


    @media (max-width: 600px) {
      .exclusive-link {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 0 18px;
      }

      .icon {
        width: 125px;
        height: 125px;
        margin-bottom: 16px;
        border-radius: 16px;
      }

      .logo {
        width: 70%;
        height: 70%;
      }

      .text {
        font-size: 22px;
        letter-spacing: 1.2px;
        line-height: 1.15;
        text-align: center;
      }

      .modal-card {
        padding: 24px 18px;
        border-radius: 20px;
      }

      .modal-title {
        font-size: 24px;
      }

      .modal-text {
        font-size: 14px;
      }

      .modal-actions {
        flex-direction: column;
      }

      .modal-button {
        width: 100%;
      }
    }
  </style>
</head>
<body>
  <!-- Cambia el video reemplazando el archivo static/Fondo.mp4 -->
  <video class="background-video" autoplay muted loop playsinline>
    <source src="{{ url_for('static', filename='Fondo.mp4') }}" type="video/mp4">
  </video>
  <div class="overlay"></div>

  <a class="exclusive-link" id="exclusiveLink" href="#" data-url="https://onlyfans.com/exeof" aria-label="Open exclusive content">
    <div class="icon">
      <!-- Cambia el logo reemplazando el archivo static/logo.png -->
      <img class="logo" src="{{ url_for('static', filename='logo.png') }}" alt="Exclusive content logo">
    </div>
    <div class="text">EXCLUSIVE CONTENT</div>
  </a>

  <div class="age-modal" id="ageModal" role="dialog" aria-modal="true" aria-labelledby="ageTitle">
    <div class="modal-card">
      <div class="modal-title" id="ageTitle">Are you 18 or older?</div>
      <p class="modal-text">You must confirm that you are at least 18 years old to continue.</p>
      <div class="modal-actions">
        <button class="modal-button yes-button" id="yesButton" type="button">Yes</button>
        <button class="modal-button no-button" id="noButton" type="button">No</button>
      </div>
      <div class="age-warning" id="ageWarning">You must be 18 or older to continue.</div>
    </div>
  </div>

  <script>
    const exclusiveLink = document.getElementById('exclusiveLink');
    const ageModal = document.getElementById('ageModal');
    const ageWarning = document.getElementById('ageWarning');
    const yesButton = document.getElementById('yesButton');
    const noButton = document.getElementById('noButton');

    exclusiveLink.addEventListener('click', function(event) {
      event.preventDefault();
      ageWarning.classList.remove('show');
      ageModal.classList.add('show');
    });

    yesButton.addEventListener('click', function() {
      window.location.href = exclusiveLink.dataset.url;
    });

    noButton.addEventListener('click', function() {
      ageWarning.classList.add('show');
    });
  </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
