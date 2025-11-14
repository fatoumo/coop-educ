const fs = require('fs');
const path = require('path');

// Read the Excalidraw file
const excalidrawData = JSON.parse(fs.readFileSync('business-model-canvas.excalidraw', 'utf8'));

// Create an HTML file that displays the Excalidraw diagram
const html = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://unpkg.com/@excalidraw/excalidraw/dist/excalidraw.production.min.js"></script>
    <style>
        body { margin: 0; padding: 0; overflow: hidden; }
        #app { width: 100vw; height: 100vh; }
    </style>
</head>
<body>
    <div id="app"></div>
    <script>
        const excalidrawData = ${JSON.stringify(excalidrawData)};

        const App = () => {
            return React.createElement(
                ExcalidrawLib.Excalidraw,
                {
                    initialData: excalidrawData,
                    viewModeEnabled: true,
                    zenModeEnabled: true,
                    gridModeEnabled: false
                }
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('app'));
        root.render(React.createElement(App));
    </script>
</body>
</html>
`;

fs.writeFileSync('business-model-canvas.html', html);
console.log('HTML file created successfully!');
