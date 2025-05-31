// validate-images.js
// Validates that all images in images/images.json exist in the images/ folder and vice versa.
// Usage: npm run validate-images

const fs = require('fs');
const path = require('path');

const imagesDir = path.join(__dirname, 'images');
const jsonPath = path.join(imagesDir, 'images.json');

function getImageFiles() {
  return fs.readdirSync(imagesDir)
    .filter(f => f.match(/\.(jpg|jpeg|png|gif|bmp|tiff|tif|svg|webp)$/i));
}

function getJsonImageList() {
  const json = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  return json.filter(entry => entry.src).map(entry => entry.src);
}

function main() {
  const imageFiles = getImageFiles();
  const jsonImages = getJsonImageList();

  let allGood = true;

  // Check for images in JSON but missing in folder
  const missingFiles = jsonImages.filter(img => !imageFiles.includes(img));
  if (missingFiles.length) {
    allGood = false;
    console.log('Images listed in images.json but missing in images/ folder:');
    missingFiles.forEach(f => console.log('  -', f));
  } else {
    console.log('All images listed in images.json exist in the images/ folder.');
  }

  // Check for files in folder but missing in JSON
  const missingJson = imageFiles.filter(img => !jsonImages.includes(img));
  if (missingJson.length) {
    allGood = false;
    console.log('\nImages present in images/ folder but missing from images.json:');
    missingJson.forEach(f => console.log('  -', f));
  } else {
    console.log('All image files in images/ are listed in images.json.');
  }

  // Summary
  if (allGood) {
    console.log('\nValidation successful: All images are accounted for in both images.json and the images/ folder.');
  } else {
    console.log('\nValidation failed: See above for missing images or entries.');
  }
}

main();
