import http.server
import json
import urllib.request
import urllib.error

# This acts as a bridge from the expected 8000 port to the Ollama 11434 port
class OllamaProxyHandler(http.server.BaseHTTPRequestHandler):
    OLLAMA_URL = 'http://127.0.0.1:11434/api/generate'
    MODEL_NAME = 'llama3' # Changing to an available local model

    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            user_msg = data.get('message', '')

            # Build request to Ollama
            ollama_payload = {
                'model': self.MODEL_NAME,
                'prompt': "You are MindMate AI, an empathetic, calming mental health companion for college students. Be supportive, concise, and non-judgmental. Do not give medical advice. The user says: " + user_msg,
                'stream': False
            }
            
            print(f"Sending prompt to Ollama model '{self.MODEL_NAME}'")
            req = urllib.request.Request(
                self.OLLAMA_URL, 
                data=json.dumps(ollama_payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            
            try:
                with urllib.request.urlopen(req) as response:
                    ollama_resp = json.loads(response.read().decode('utf-8'))
                    reply = ollama_resp.get('response', 'I am here for you.')
            except urllib.error.HTTPError as e:
                err_text = e.read().decode('utf-8')
                reply = f"Ollama HTTP {e.code} Error: {err_text}"
                print("Ollama returned an error:", err_text)
            except urllib.error.URLError as e:
                reply = f"I am having trouble connecting to your local Ollama server at port 11434. Make sure Ollama is running and has the '{self.MODEL_NAME}' model pulled. Error: {str(e)}"
                print("Connection error to Ollama:", e)
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            
            self.wfile.write(json.dumps({'reply': reply}).encode('utf-8'))
            print("Reply sent back to Flutter app.")
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'reply': f'Server Error: {str(e)}'}).encode('utf-8'))
            print(f"Error handling request: {str(e)}")

server = http.server.HTTPServer(('127.0.0.1', 8000), OllamaProxyHandler)
print('Starting Ollama proxy server on http://127.0.0.1:8000')
print('This will forward `/chat` requests from Flutter to http://127.0.0.1:11434 (Ollama)')
server.serve_forever()
