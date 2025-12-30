import { defineConfig } from "vite";

export default defineConfig({
  // itch.io HTML5 runs the game under a subpath, so absolute URLs like
  // /assets/... will 404. Use a relative base so the build works anywhere.
  base: "./"
});
