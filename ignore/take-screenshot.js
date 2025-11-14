const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch({
        headless: 'new'
    });

    const page = await browser.newPage();

    // Set viewport to accommodate the canvas
    await page.setViewport({
        width: 1700,
        height: 850
    });

    // Load the HTML file
    const filePath = 'file://' + path.resolve('business-model-canvas.html');
    await page.goto(filePath, { waitUntil: 'networkidle0' });

    // Wait for content to render
    await new Promise(resolve => setTimeout(resolve, 3000));

    // Take screenshot
    await page.screenshot({
        path: 'business-model-canvas.png',
        fullPage: false
    });

    console.log('Screenshot captured successfully!');

    await browser.close();
})();
