"""
Módulo de inicialização do servidor
"""
from app import app
import os
import locale

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
