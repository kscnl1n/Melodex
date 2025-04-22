# Melodex

This is the code for the project **Melodex**, a website that takes your listening habits and tells you what your music says about you 🎵🎧💜

## Tech Stack
### Frontend
**React & Tailwind** for UI
### Backend
**FastAPI** for model storage
(We don't store your login data! Spotify API does)

### 🎵 Spotify Integration
**Spotify API** to access your spotify playlists

### 🧠 OpenAI integration
**OpenAI** for chatbot functionality

## Security
We do not store your login data! All logins/authentication is handled by Spotify API and OpenAI API, which *does* have access to the data we send over after we access SpotifyAPI. However, we have built this project so it only sees your public playlists, and nothing else.

This is why we don't utilize a database like MongoDB. This is an open-source project and we want your data to stay 100% yours.

Because of this, **we can't store past readings or take into consideration your listening habits outside of public playlists you have,** so make sure you take a screenshot of your results ~✨
