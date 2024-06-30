import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import { VitePWA } from 'vite-plugin-pwa';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      manifest: {
        name: 'SimplifAI',
        short_name: 'SimplifAI',
        description: 'Understanding Medical Report made easy',
        start_url: '/',
        display: 'standalone',
        background_color: '#ffffff',
        theme_color: '#000000',
        icons: [
          {
            src: '/icons/logo48.png',
            type: 'image/png',
            sizes: '48x48',
          },
          {
            src: '/icons/logo72.png',
            type: 'image/png',
            sizes: '72x72',
          },
          {
            src: '/icons/logo96.png',
            type: 'image/png',
            sizes: '96x96',
          },
          {
            src: '/icons/logo144.png',
            type: 'image/png',
            sizes: '144x144',
          },
          {
            src: '/icons/logo192.png',
            type: 'image/png',
            sizes: '192x192',
          },
          {
            src: '/icons/logo512.png',
            type: 'image/png',
            sizes: '512x512',
          },
        ],
      },
    }),
  ],
});