"""
defaults.py

(section_name, option, value, default, typeof, is_required)
"""

DEFAULT_CONFIG = [
    ("mywsgi:server", "host", None, "127.0.0.1", str, True),
    ("mywsgi:server", "port", None, 8080, int, True),
    ("mywsgi:logging", "level", None, "info", str, True),
]

"""
[mywsgi:server]
host: 127.0.0.1
port: 8080

[mywsgi:logging]
level: info
"""
