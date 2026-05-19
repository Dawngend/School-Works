<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photo Stories</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            display: flex;
            width: 100%;
            min-height: 80vh;
            border: 2px solid gray;
            background-color: white;
        }
        .story-column {
            flex: 1; 
            border-right: 1px solid gray;
            padding: 15px;
            text-align: center;
        }
        .story-column:last-child {
            border-right: none; 
        }
        .story-column img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin-bottom: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h2 style="text-align: center;">My Photo Stories</h2>
    <div class="container">