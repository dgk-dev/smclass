import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: "media",
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#F4F7FE",
          100: "#E9EFFD",
          200: "#D3DFFC",
          300: "#BED0FA",
          400: "#A8C0F9",
          500: "#92B0F7",
          600: "#7CA0F6",
          700: "#6691F4",
          800: "#5081F3",
          900: "#3A71F1",
        },
        surface: {
          50: "#FFFFFF",
          100: "#FAFAFA",
          200: "#F5F5F5",
          300: "#E5E5E5",
          400: "#D4D4D4",
          500: "#A3A3A3",
          600: "#737373",
          700: "#525252",
          800: "#262626",
          900: "#171717",
        },
        accent: {
          blue: "#2563EB",
          green: "#16A34A",
          red: "#DC2626",
        },
      },
      fontFamily: {
        sans: ["var(--font-geist-sans)", "system-ui", "sans-serif"],
        mono: ["var(--font-geist-mono)", "monospace"],
      },
      boxShadow: {
        'surface': '0px 1px 0px 0px rgba(0,0,0,0.05)',
        'surface-hover': '0px 4px 8px -2px rgba(0,0,0,0.05), 0px 1px 0px 0px rgba(0,0,0,0.05)',
        'float': '0px 2px 4px -1px rgba(0,0,0,0.02), 0px 4px 6px -1px rgba(0,0,0,0.03)',
        'float-hover': '0px 8px 16px -4px rgba(0,0,0,0.05), 0px 2px 4px -1px rgba(0,0,0,0.02)',
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'slide-up': 'slideUp 0.5s ease-out',
        'slide-down': 'slideDown 0.2s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(8px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-8px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
      spacing: {
        'card': '1.25rem',
        'section': '5rem',
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.25rem',
        '3xl': '1.5rem',
      },
    },
  },
  plugins: [],
} satisfies Config;
