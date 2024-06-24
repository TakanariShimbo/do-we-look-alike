README | [English](/README/README_EN.md) | [日本語](/README/README_JP.md)

## 🚀 はじめに

「私たちって似てる？」のリポジトリです。  
以下の QR コードをスキャン、あるいはクリックすると、ウェブサイトにアクセスできます。

[![QR-Code of WebSite](/data/QRCode.png)](https://do-we-look-alike.streamlit.app/)

このアプリでは、[InsightFace](https://github.com/deepinsight/insightface) を利用しています。

## 🐋Docker

- 前提：docker がインストール済み

### サーバーの立ち上げ

```bash
# 実行する前に .env を設定する
docker compose up -d
```

### Build image

```bash
# ユーザー名、タグは適切に設定する
docker build -t takanarishimbo/do-we-look-alike:v1.0.0 .
```

## 🐍Conda

- 前提：conda あるいは miniconda がインストール済み

### 仮想環境の作成

```bash
conda create --name do_we_look_alike python=3.11
```

### 仮想環境の有効化

```bash
conda activate do_we_look_alike
```

### ライブラリのインストール

```bash
# 実行する前に仮想環境を有効化する
pip install -r requirements.txt
```

### サーバーの立ち上げ

```bash
# 実行する前に仮想環境を有効化する
streamlit run server.py
```
