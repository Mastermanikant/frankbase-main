const fs = require('fs');
const xml2js = require('xml2js');
const path = require('path');

const xmlFilePath = path.join(__dirname, 'frankbasenewsnetwork.WordPress.2026-03-04.xml');
const outputDir = path.join(__dirname, 'extracted_articles');

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const parser = new xml2js.Parser();

fs.readFile(xmlFilePath, function (err, data) {
    if (err) {
        console.error("Error reading XML file:", err);
        return;
    }

    parser.parseString(data, function (err, result) {
        if (err) {
            console.error("Error parsing XML:", err);
            return;
        }

        const items = result.rss.channel[0].item;
        let count = 0;

        items.forEach(item => {
            const postType = item['wp:post_type'] ? item['wp:post_type'][0] : '';
            if (postType === 'post') {
                const title = item.title[0] || 'Untitled';
                const safeTitle = title.replace(/[^a-z0-9]/gi, '_').toLowerCase();
                const content = item['content:encoded'] ? item['content:encoded'][0] : '';

                let tagsStr = '';
                if (item.category) {
                    const tags = item.category.filter(c => c['$'] && c['$'].domain === 'post_tag').map(c => c._);
                    if(tags.length > 0){
                        tagsStr = `<p><strong>Tags:</strong> ${tags.join(', ')}</p>\n`;
                    }
                }

                const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
        img { max-width: 100%; height: auto; }
    </style>
</head>
<body>
    <h1>${title}</h1>
    ${tagsStr}
    <hr>
    ${content}
</body>
</html>`;

                const filePath = path.join(outputDir, `${safeTitle}.html`);
                fs.writeFileSync(filePath, htmlContent, 'utf8');
                console.log(`Saved: ${filePath}`);
                count++;
            }
        });

        console.log(`\n✅ Successfully extracted ${count} articles to the '${outputDir}' folder.`);
    });
});
