# Project 911 (temp)

Choice-based text adventure (horror / absurd).

Browser-only, no saving (does not use LocalStorage / cookies / IndexedDB / server-side persistence).

## Requirements (Windows + WSL2)

- Windows: VS Code
- WSL2 (Ubuntu, etc.)
- Node.js / npm (this repo uses Vite + Vanilla JS)

### Installing Node (recommended: nvm)

In WSL:

```bash
# nvm
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# load nvm (opening a new shell is the safest option)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

# Node (LTS)
nvm install --lts
nvm use --lts
```

## Development

```bash
npm install
npm run dev
```

- `public/data/gameData.json` contains all scene / BAD END / clear data
- Put images in `public/assets/`

## Build

```bash
npm run build
npm run preview
```

Build output is `dist/`.

## Game Rules

- Starts from Scene 1
- Each scene has 2 choices (A/B)
- Exactly one route is correct
- A wrong choice immediately leads to a BAD END
- 10 consecutive correct choices leads to GAME CLEAR
- No saving: reloading restarts from Scene 1

## Deploy to Cloudflare Pages

You can deploy via GitHub integration on Cloudflare Pages.

- Framework preset: `Vite`
- Build command: `npm run build`
- Build output directory: `dist`
