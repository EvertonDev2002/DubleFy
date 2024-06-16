import { act } from "react"

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*./{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        custom: {
          black: "#0E0E0E",
          dark_gray: "#3C3C3C",
          very_dark_gray: "#242424",
          moderate_green: "#6DAE5D",
          light_cyan: "#67B9BE",
          lighter_dark_gray: "#3A3A3A",
          light_gray: "#BDBDBD",
        },
        hover: {
          medium_gray: "#505050",
          pastel_green: "#7FB872",
        },
        active: {
          dark_medium_gray: "#636363",
          light_pastel_green: "#91C286",
        },
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
      },
      borderRadius: {
        "4xl": "2rem",
      },
    },
  },
  plugins: [],
}
