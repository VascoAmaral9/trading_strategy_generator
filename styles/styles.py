CSS = """
/* Full-width layout */
.gradio-container {
  max-width: 100% !important;
  padding: 40px 60px !important;
}

/* Header styling */
.gradio-container h1 {
  background: linear-gradient(135deg, #753991 0%, #209dd7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-size: 2.5em !important;
  font-weight: 800 !important;
  margin-bottom: 20px !important;
  text-align: center;
}

.gradio-container .markdown p {
  color: rgba(233, 238, 245, 0.8);
  font-size: 1.1em;
  line-height: 1.6;
  text-align: center;
  max-width: 900px;
  margin: 0 auto 30px auto;
}

/* Control section */
.controls {
  background: rgba(22, 26, 34, 0.6);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 20px;
}

/* Main generate button */
.convert-btn button {
  background: linear-gradient(135deg, #753991 0%, #8e45b0 100%) !important;
  border: 1px solid rgba(255,255,255,.12) !important;
  color: white !important;
  font-weight: 700 !important;
  font-size: 1.05em !important;
  padding: 12px 32px !important;
  border-radius: 12px !important;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.convert-btn button:hover {
  box-shadow: 0 0 0 3px #753991 inset !important;
}

/* Action buttons */
.run-btn button {
  background: #202631 !important;
  color: #e9eef5 !important;
  border: 1px solid rgba(255,255,255,.12) !important;
  font-weight: 600 !important;
  padding: 10px 24px !important;
  border-radius: 10px !important;
}

.run-btn.py button:hover {
  box-shadow: 0 0 0 2px #209dd7 inset !important;
}

.run-btn.cpp button:hover {
  box-shadow: 0 0 0 2px #ecad0a inset !important;
}

/* Output area styling */
.py-out textarea {
  background: linear-gradient(135deg, rgba(32,157,215,.18) 0%, rgba(32,157,215,.08) 100%) !important;
  border: 1px solid rgba(32,157,215,.4) !important;
  border-radius: 14px !important;
  color: rgba(32,157,215,1) !important;
  font-weight: 600 !important;
  padding: 16px !important;
}
"""
