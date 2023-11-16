import { defineStore } from 'pinia'

export const useToastStore = defineStore({
  id: 'toast',

  state: () => ({
    ms: 0,
    message: '',
    classes: '',
    isVisible: false
  }),

  actions: {
    showToast(ms, message) {
      console.log('toast show ')

      if (ms === 'inf') {
        // Infinite duration, don't automatically hide the toast
        this.isVisible = true
      } else {
        this.ms = parseInt(ms)
        this.message = message
        this.isVisible = true

        // Additional logic for hiding the toast after a specific duration
        setTimeout(() => {
          console.log('toast hide ')
          this.isVisible = false
        }, this.ms)
      }
    }
  }
})
