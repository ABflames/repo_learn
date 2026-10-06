const express = require('express');
const router = express.Router();

let students = [];

// GET /students
router.get('/', (req, res) => {
    res.json(students);
});

// POST /students  (JSON)
router.post('/', (req, res) => {
    students.push(req.body);
    res.json({
        message: "Student added successfully",
        data: req.body
    });
});

// POST /students/form  (Form data)
router.post('/form', (req, res) => {
    students.push(req.body);
    res.send("Form data received successfully");
});

// POST /students/feedback  (Text)
router.post('/feedback', (req, res) => {
    res.send(`Feedback received: ${req.body}`);
});

// POST /students/upload  (Raw data)
router.post('/upload', (req, res) => {
    res.send(`Raw data length: ${req.body.length}`);
});

module.exports = router;