# practice-multiple_remote_container
開発コンテナを2つ以上使う実験

## Introduction
* docker-composeで構成される2つ以上のコンテナをRemote-Containersで扱ってみたかった
* FlaskとReactの開発コンテナが起動できる

## Require
* VSCode
  * Remote-Containers
* Docker
* docker-compose

## Usage
1. VSCodeで開く。
```
git clone https://github.com/Sut103/practice-multiple_remote_container.git
code practice-multiple_remote_container
```
2. `F1`を押して `Remote-Containers: Open Folder in Container...` を選択。
1. `backend` を選択して `OK`
1. ビルドが始まるので待つ。結構待つ(frontendコンテナにnpm installしているため)。
1. `shift + ctrl + n` して、同様に`frontend`も開く。
