mkdir -p ~/.streamlit/
echo "[theme]
base='dark'
font = 'sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml