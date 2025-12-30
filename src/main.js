import "./style.css";

const DATA_URL = "/data/gameData.json";

/** @typedef {{label:string, text:string, next:string}} Choice */
/** @typedef {{id:string, title:string, illustration:string, storyText:string, choices:Choice[]}} Scene */
/** @typedef {{id:string, title:string, illustration:string, deathText:string}} BadEnd */
/** @typedef {{id:string, title:string, illustration:string, clearText:string}} Clear */

/** @type {{meta:{gameTitle:string,totalScenes:number}, scenes:Scene[], badEnds:BadEnd[], clear:Clear} | null} */
let gameData = null;

/** @type {string} */
let currentId = "scene1";

const app = document.querySelector("#app");

function el(tag, props = {}, children = []) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(props)) {
    if (key === "class") node.className = value;
    else if (key === "text") node.textContent = value;
    else if (key.startsWith("on") && typeof value === "function") node.addEventListener(key.slice(2).toLowerCase(), value);
    else node.setAttribute(key, String(value));
  }
  for (const child of children) node.append(child);
  return node;
}

function sceneIndexFromId(id) {
  const match = id.match(/^scene(\d+)$/);
  if (!match) return null;
  const n = Number(match[1]);
  return Number.isFinite(n) ? n : null;
}

function badSceneIndexFromId(id) {
  const match = id.match(/^bad_scene(\d{2})_b$/);
  if (!match) return null;
  const n = Number(match[1]);
  return Number.isFinite(n) ? n : null;
}

function restart() {
  currentId = "scene1";
  render();
}

function findScene(id) {
  return gameData?.scenes.find((s) => s.id === id) ?? null;
}

function findBadEnd(id) {
  return gameData?.badEnds.find((b) => b.id === id) ?? null;
}

function renderHeader(progressText) {
  return el("header", { class: "header" }, [
    el("div", { class: "title", text: gameData?.meta.gameTitle ?? "911" }),
    el("div", { class: "progress", text: progressText })
  ]);
}

function renderIllustration(src, alt) {
  return el("div", { class: "illusWrap" }, [
    el("img", {
      class: "illus",
      src,
      alt,
      loading: "lazy",
      decoding: "async"
    })
  ]);
}

function renderTextBlock(text) {
  return el("div", { class: "story", text });
}

function renderButtons(buttons) {
  return el("div", { class: "buttons" }, buttons);
}

function render() {
  if (!app) return;

  if (!gameData) {
    app.replaceChildren(
      el("main", { class: "container" }, [
        renderHeader("Loading"),
        el("div", { class: "card" }, [
          el("p", { class: "hint", text: "Loading game data" })
        ])
      ])
    );
    return;
  }

  const total = gameData.meta.totalScenes ?? 10;

  if (currentId === gameData.clear.id) {
    const clear = gameData.clear;
    app.replaceChildren(
      el("main", { class: "container" }, [
        renderHeader(`GAME CLEAR (10 / ${total})`),
        el("div", { class: "card" }, [
          renderIllustration(clear.illustration, clear.title),
          renderTextBlock(clear.clearText),
          renderButtons([
            el("button", { class: "btn secondary", type: "button", onClick: restart, text: "Restart" })
          ])
        ])
      ])
    );
    return;
  }

  const scene = findScene(currentId);
  if (scene) {
    const idx = sceneIndexFromId(scene.id) ?? 0;
    const progress = `Scene ${idx} / ${total}`;

    const choiceButtons = scene.choices.map((c) =>
      el(
        "button",
        {
          class: "btn",
          type: "button",
          onClick: () => {
            currentId = c.next;
            render();
          }
        },
        [
          el("span", { class: "choiceLabel", text: c.label }),
          el("span", { class: "choiceText", text: c.text })
        ]
      )
    );

    app.replaceChildren(
      el("main", { class: "container" }, [
        renderHeader(progress),
        el("div", { class: "card" }, [
          renderIllustration(scene.illustration, scene.title),
          renderTextBlock(scene.storyText),
          renderButtons([
            ...choiceButtons,
            el("button", { class: "btn secondary", type: "button", onClick: restart, text: "Restart" })
          ])
        ])
      ])
    );
    return;
  }

  const bad = findBadEnd(currentId);
  if (bad) {
    const idx = badSceneIndexFromId(bad.id) ?? 0;
    app.replaceChildren(
      el("main", { class: "container" }, [
        renderHeader(`GAME OVER (Scene ${idx} / ${total})`),
        el("div", { class: "card" }, [
          renderIllustration(bad.illustration, bad.title),
          renderTextBlock(bad.deathText),
          renderButtons([
            el("button", { class: "btn", type: "button", onClick: restart, text: "Start Over" })
          ])
        ])
      ])
    );
    return;
  }

  currentId = "scene1";
  render();
}

async function boot() {
  try {
    render();
    const res = await fetch(DATA_URL, { cache: "no-store" });
    if (!res.ok) throw new Error(`Failed to load data: ${res.status}`);
    gameData = await res.json();
    currentId = "scene1";
    render();
  } catch (e) {
    console.error(e);
    if (!app) return;
    app.replaceChildren(
      el("main", { class: "container" }, [
        renderHeader("Error"),
        el("div", { class: "card" }, [
          el("p", { class: "hint", text: "Failed to load game data." }),
          el("button", { class: "btn", type: "button", onClick: () => location.reload(), text: "Reload" })
        ])
      ])
    );
  }
}

boot();

