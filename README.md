# SQLi PoC Tools — Blind & Time-based (Educativo)

**Advertencia legal:** Estas herramientas están pensadas **solo** para fines educativos y pruebas en entornos controlados (p. ej. labs locales como SQLi Labs, DVWA, máquinas virtuales de laboratorio). **No** las uses contra sistemas de terceros sin permiso explícito. El autor no se responsabiliza por el uso indebido.

---

## Descripción

Conjunto de scripts en Python para demostrar dos técnicas de inyección SQL:

- **Blind (boolean-based)**: extracción carácter a carácter comprobando la respuesta del servidor.  
- **Time-based**: extracción mediante medición del retraso (sleep) en las respuestas.

Estos scripts están pensados para ejecutarse contra entornos de práctica (por ejemplo `http://localhost/sqli-labs-php7/`).

---

## Requisitos

- Python 3.8+
- Paquetes Python:
  - `requests`
  - `pwntools` (opcional; se usa para `log.progress` en la salida)

Puedes instalar dependencias (recomendado en un entorno virtual):
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate.bat     # Windows
pip install -r requirements.txt
