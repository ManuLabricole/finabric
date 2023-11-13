/** @type {import('tailwindcss').Config} */
export const content = ['./index.html', './src/**/*.{js,vue}']
export const theme = {
  extend: {
    colors: {
      finaryYellow: {
        50: '#FFF8F0', // lightest peach
        100: '#FEEEDC',
        200: '#FDDDC9',
        300: '#FCCBB6',
        400: '#FBBAa3',
        500: '#F0C086', // base peach
        600: '#D6A370',
        700: '#BC865A',
        800: '#A26944',
        900: '#883C2E' // darkest peach
      },
      finaryBlue: {
        50: '#E4E2EA', // lightest deep purple
        100: '#C7C5D4',
        200: '#AAA7BE',
        300: '#8C8AA8',
        400: '#6F6C92',
        500: '#262043', // base deep purple
        600: '#211B3B',
        700: '#1C1633',
        800: '#17112B',
        900: '#120C23' // darkest deep purple
      },
      bg: {
        'top-gradient-yellow': '#2C2419',
        'top-gradient-blue': '#0B0A10'
      },
      
      primary: '#EDF0F4',
      secondary: '#6E727A',
      black: '#131314',
      danger: '#E54948',
      success: '#1EC090',
      warning: '#F49352',
      
      button: {
        primary: '#EDF0F4',
        secondary: '#262043',
        google: '#3A83DD',
        apple: '#FFFFFF'
      }
    }
  }
}
export const plugins = [require('@tailwindcss/forms')]
