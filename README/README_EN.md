README | [English](/README/README_EN.md) | [日本語](/README/README_JP.md)

## 🚀About

This is repository of "Do We Look A Like?".  
You can access the website by clicking or scanning the QR code below.

[![QR-Code of WebSite](/data/QRCode.png)](https://do-we-look-alike.streamlit.app/)

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

### Deploy server

```bash
# Please activate venv before executing it.
streamlit run server.py
```
