import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig(({ mode }) => {
  // loadEnv returns all env vars for the given mode as strings
  const env = loadEnv(mode, process.cwd(), "VITE_"); // only loads vars starting with VITE_

  const debug = env.VITE_DEBUG === "true"; // convert to boolean

  return {
    plugins: [react()],
    server: debug
      ? {
          proxy: {
            "/api": {
              target: "http://localhost:8000",
              changeOrigin: true,
              secure: false,
            },
          },
        }
      : {},
  };
});
