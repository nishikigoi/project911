# Project 911

Choice-based text adventure (horror / absurd).

Browser-only, no saving (does not use LocalStorage / cookies / IndexedDB / server-side persistence).

<p align="center">
	<img src="public/assets/title.webp" width="32%" alt="Title" />
	<img src="public/assets/scene01.webp" width="32%" alt="Gameplay" />
	<img src="public/assets/clear.webp" width="32%" alt="Clear" />
</p>

## Requirements

- Node.js + npm

This project is a Vite + Vanilla JS SPA.

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

## License

MIT (see `LICENSE`).
