// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],
  runtimeConfig: {
    // Keys within public, will be also exposed to the client-side
    public: {
      backend_host: "http://localhost:8081"
    }
  }
})
