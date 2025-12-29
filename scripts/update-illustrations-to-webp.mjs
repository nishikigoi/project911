import fs from "node:fs";

const jsonPath = "public/data/gameData.json";
const data = JSON.parse(fs.readFileSync(jsonPath, "utf8"));

for (const scene of data.scenes ?? []) {
  const id = String(scene.id ?? "");
  if (id.startsWith("scene")) {
    const n = Number(id.slice("scene".length));
    if (Number.isFinite(n) && n >= 1 && n <= 99) {
      scene.illustration = "/assets/scene" + String(n).padStart(2, "0") + ".webp";
    }
  }
}

for (const bad of data.badEnds ?? []) {
  const id = String(bad.id ?? "");
  const m = id.match(/^bad_scene(\d+)_b$/);
  if (m) {
    const nn = Number(m[1]);
    if (Number.isFinite(nn) && nn >= 1 && nn <= 99) {
      // Files provided by user: bad_scene01.png -> bad_scene01.webp
      bad.illustration = "/assets/bad_scene" + String(nn).padStart(2, "0") + ".webp";
    }
  }
}

if (data.clear && typeof data.clear === "object") {
  data.clear.illustration = "/assets/clear.webp";
}

fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2) + "\n", "utf8");
console.log("Updated illustration paths in " + jsonPath);
