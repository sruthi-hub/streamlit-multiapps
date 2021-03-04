mkdir -p ~/.streamlit/
echo "[general]
email = \"srs204@pitt.edu\"
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
