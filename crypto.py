import hashlib
from datetime import datetime
import socket

def compute_file_hash(file_bytes: bytes) -> str:
    return hashlib.sha256(file_bytes).hexdigest()

def gather_metadata() -> dict:
    return {
        "timestamp_ist": datetime.now().strftime("%Y-%m-%d %H:%M:%S IST"),
        "node_identifier": hashlib.md5(socket.gethostname().encode()).hexdigest()[:12].upper()
    }
