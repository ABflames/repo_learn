const express = require('express');
const app = express();

// ✅ Correct path (very important)
const studentRouter = require('./routes/studentRoutes');

// -------- Middleware --------
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.text());
app.use(express.raw({ type: 'application/octet-stream' }));

// -------- Application Properties --------
app.locals.portalName = "Student Portal Application";

// -------- Static Files --------
app.use(express.static('public'));

// -------- Mount Router --------
app.use('/students', studentRouter);

// -------- Root Route --------
app.get('/', (req, res) => {
    res.send(`Welcome to ${app.locals.portalName}`);
});

// -------- Start Server --------
app.listen(3000, () => {
    console.log("Server running on http://localhost:3000");
});