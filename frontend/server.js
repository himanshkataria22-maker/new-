const express = require('express');
const axios = require('axios');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// API proxy to backend
const API_BASE_URL = process.env.API_URL || 'http://localhost:8000';

// Routes
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API endpoints that proxy to backend
app.post('/api/greet', async (req, res) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/greet`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/api/format-version', async (req, res) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/format-version`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/api/slugify', async (req, res) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/slugify`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/api/truncate', async (req, res) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/truncate`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.get('/api/health', async (req, res) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/health`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Handle missing API endpoints
app.use('/api/*', (req, res) => {
    res.status(404).json({ 
        error: 'Endpoint not found',
        message: `The endpoint ${req.method} ${req.originalUrl} does not exist`,
        availableEndpoints: [
            'POST /api/greet',
            'POST /api/format-version',
            'POST /api/slugify', 
            'POST /api/truncate',
            'GET /api/health'
        ]
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Frontend server running on port ${PORT}`);
    console.log(`Backend API at: ${API_BASE_URL}`);
});
