require('dotenv').config();

const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const diseasesRoutes = require('./routes/diseases');
const userRoutes = require('./routes/user');
const knowledgeRoutes = require('./routes/knowledge');

const app = express();
const PORT = process.env.PORT || 4000;

// Middleware
app.use(cors({
    origin: '*',
    methods: ['GET', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE'],
    allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With'],
    credentials: true
}));

app.use(express.json());

app.use((req, res, next) => {
    console.log(`[Vanaspati.AI Backend] ${req.method} ${req.path}`);
    next();
});

// Root & Health endpoint
app.get('/', (req, res) => {
    res.json({
        name: 'Vanaspati.AI Backend API',
        version: '2.0.0',
        status: 'online',
        database: mongoose.connection.readyState === 1 ? 'connected' : 'disconnected (using fallback cache)',
        endpoints: [
            '/api/diseases/details?name=...',
            '/api/diseases/list',
            '/api/user/login',
            '/api/user/signup'
        ]
    });
});

app.get('/health', (req, res) => {
    res.json({ status: 'healthy', uptime: process.uptime() });
});

// API Routes
app.use('/api/diseases', diseasesRoutes);
app.use('/api/user', userRoutes);
app.use('/api/knowledge', knowledgeRoutes);

// Connect to Database and start server
mongoose.set('strictQuery', false);

const startServer = () => {
    app.listen(PORT, () => {
        console.log(`=======================================================`);
        console.log(`🌿 Vanaspati.AI Backend Service Listening on Port ${PORT}`);
        console.log(`📡 URL: http://localhost:${PORT}`);
        console.log(`=======================================================`);
    });
};

if (process.env.MONGO_URL) {
    mongoose.connect(process.env.MONGO_URL, {
        serverSelectionTimeoutMS: 5000 // fast timeout so server doesn't hang if offline
    })
    .then(() => {
        console.log('✅ [Vanaspati.AI] Successfully connected to MongoDB database');
        startServer();
    })
    .catch((err) => {
        console.warn('⚠️ [Vanaspati.AI] MongoDB Atlas connection error:', err.message);
        console.warn('⚡ [Vanaspati.AI] Starting server in offline/resilient mode with local knowledge fallback.');
        startServer();
    });
} else {
    console.warn('⚠️ [Vanaspati.AI] MONGO_URL not defined. Starting with local knowledge base.');
    startServer();
}

module.exports = app;
