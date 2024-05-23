/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html", "index.html", "./static/js/**/*.js"],
  theme: {
    extend: {
      gridTemplateColumns: {
        // Simple 16 column grid
        13: "repeat(13, minmax(100px, 1fr))",
        14: "repeat(14, minmax(100px, 1fr))",
        14: "repeat(15, minmax(100px, 1fr))",
        16: "repeat(16, minmax(100px, 1fr))",
        17: "repeat(17, minmax(100px, 1fr))",
      },
      gridColumn: {
        "span-13": "span 13 / span 13",
        "span-14": "span 14 / span 14",
        "span-15": "span 15 / span 15",
        "span-16": "span 16 / span 16",
        "span-17": "span 17 / span 17",
      },
      gridColumnStart: {
        13: "13",
        14: "14",
        15: "15",
        16: "16",
        17: "17",
      },
      gridColumnEnd: {
        13: "13",
        14: "14",
        15: "15",
        16: "16",
        17: "17",
      },
    },
    container: {
      center: true,
    },
    colors: {
      primary: "#141A21",
      secondary: "#63707D",
      bg_main: "#F6FAFF",
      bg_light_blue: "#E1EAF6",
      blue_500: "#0066FF",
      blue_700: "#0038FF",
      bg_nav_pills: "#EFF4FC",
      green_500: "#27AE60",
      green_700: "#16964C",
      red_500: "#EB5757",
      red_700: "#DB3F3F",
      red_100: "#F44242",
      border_light: "#E8EFFB",
    },
    fontFamily: {
      body: ['"Inter"', "sans-serif"],
    },
  },
  plugins: [
    "postcss-import",
    "tailwindcss",
    "autoprefixer",
    "prettier-plugin-tailwindcss",
    require("preline/plugin"),
  ],
};
