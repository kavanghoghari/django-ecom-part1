/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],

  theme: {
    extend: {},
  },
  plugins: [],
}
module.exports = {
  // ...
  plugins: [
    // ...
    require('@tailwindcss/aspect-ratio'),
  ],
}
