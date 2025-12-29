import fs from "node:fs";
import path from "node:path";
import sharp from "sharp";

const assetsDir = path.resolve("public", "assets");

function listPngFiles(dir) {
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((ent) => ent.isFile())
    .map((ent) => ent.name)
    .filter((name) => name.toLowerCase().endsWith(".png"))
    .sort();
}

const pngFiles = listPngFiles(assetsDir);
if (pngFiles.length === 0) {
  console.log("No PNG files found in public/assets. Nothing to convert.");
  process.exit(0);
}

const quality = Number(process.env.WEBP_QUALITY ?? 82);

console.log();

for (const pngName of pngFiles) {
  const inPath = path.join(assetsDir, pngName);
  const outName = pngName.replace(/\.png$/i, ".webp");
  const outPath = path.join(assetsDir, outName);

  // For illustration-style PNGs, lossy WebP at ~80-85 is usually a good tradeoff.
  await sharp(inPath)
    .webp({ quality, effort: 5 })
    .toFile(outPath);

  const inSize = fs.statSync(inPath).size;
  const outSize = fs.statSync(outPath).size;
  const ratio = ((outSize / inSize) * 100).toFixed(1);
  console.log();
}

console.log("Done.");
