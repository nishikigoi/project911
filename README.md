# Project 911 (仮)

テキストアドベンチャー（選択肢型） + ホラー／不条理。
**ブラウザ完結保存なし**（LocalStorage / Cookie / IndexedDB / サーバ保存は使いません）。

## 必要環境（Windows + WSL2）

- Windows: VS Code
- WSL2 (Ubuntuなど)
- Node.js / npm（このリポジトリは Vite + Vanilla JS）

### Node導入（nvm推奨）

WSL内で：

```bash
# nvm
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# 反映（新しいシェルを開くのが確実）
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

# Node (LTS)
nvm install --lts
nvm use --lts
```

## 開発

```bash
npm install
npm run dev
```

- `public/data/gameData.json` がシーン／BAD END／クリアのデータです
- 画像は `public/assets/` に置きます（現状はSVGプレースホルダ）

## ビルド

```bash
npm run build
npm run preview
```

出力は `dist/` です。

## ゲーム進行（仕様）

- Scene1から開始
- 各Sceneは2択（A/B）。正解ルートは1つのみ
- 誤選択は即BAD END
- 10連続正解で GAME CLEAR
- **保存なし**：リロードすると最初から（Scene1）

## Cloudflare Pages デプロイ

Cloudflare PagesでGitHub連携してデプロイできます。

- Framework preset: `Vite`
- Build command: `npm run build`
- Build output directory: `dist`

初回デプロイ後、`public/assets/` のプレースホルダSVGを WebP 等に差し替えていく想定です。
