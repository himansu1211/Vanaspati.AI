# Vanaspati.AI - Backend Service 🌿

Express.js and MongoDB REST API for user authentication and plant disease knowledge retrieval.

## Features:
- JWT Authentication (Signup & Login) with Bcrypt hashing
- Plant disease details API (`/api/diseases/details?name=...`)
- High-resilience offline fallback database for all 38 plant classes

## Getting Started:
```bash
npm install
npm run dev
# Or for production:
npm start
```
Default port: `4000`