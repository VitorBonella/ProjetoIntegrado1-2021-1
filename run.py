from app import app
import os
import locale

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
