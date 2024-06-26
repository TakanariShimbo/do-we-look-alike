README | [English](/README/README_EN.md) | [日本語](/README/README_JP.md)

## 🚀About

This is repository of "Do We Look A Like?".  
You can access the website by clicking or scanning the QR code below.

[![QR-Code of WebSite](/data/QRCode.png)](https://do-we-look-alike.streamlit.app/)

This application is powered by [InsightFace](https://github.com/deepinsight/insightface).

## 🐋Docker

- docker is required

### Build image

```bash
# Please change the username and tag correctly.
docker build -t takanarishimbo/do-we-look-alike:v1.0.0 .
```

### Generate Self-Signed Certificate

```sh
cd nginx

# generate private-key
openssl genpkey -out private-key.key -algorithm RSA -pkeyopt rsa_keygen_bits:2048

# generate certificate-request
# please set the certificate.cnf file before executing it.
openssl req -new -key private-key.key -out certificate-request.csr -config certificate.cnf

# generate certificate
openssl x509 -req -in certificate-request.csr -signkey private-key.key -out certificate.crt -days 3650 -extfile certificate.cnf -extensions v3_ca
```

### Build server

```bash
# Please set the .env file before executing it.
docker compose up -d
```

## 🐍Conda

- conda or miniconda is required

### Create venv

```bash
conda create --name do_we_look_alike python=3.11
```

### Activate venv

```bash
conda activate do_we_look_alike
```

### Install libs

```bash
# Please activate venv before executing it.
pip install -r requirements.txt
```

### Build server

```bash
# Please activate venv before executing it.
streamlit run server.py
```
