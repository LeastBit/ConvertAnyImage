# 🖼️ ConvertAnyImage - Universal Image Format lossless Converter

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Custom-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

## ✨ Key Features

### 🎯 **Near-Lossless Conversion**
- **High Quality Preservation**: Default 100% quality setting to maximize original image quality
- **Smart DPI Handling**: Default 400 DPI high-resolution output ensures no detail loss
- **Transparency Protection**: Perfect handling of PNG/GIF transparent backgrounds, automatic white background for JPEG
- **Color Mode Optimization**: Intelligent color mode conversion to avoid color distortion

### 🚀 **Powerful Capabilities**
- **Full Format Support**: Convert between 20+ mainstream image formats
- **PDF to Image**: High-quality PDF page conversion to images
- **Batch Processing**: One-click conversion of entire folders
- **Multi-page PDF Handling**: Support for multi-page PDF merging or separate page saving

## 📋 Supported Formats

### Input Formats
```
Image Formats: JPG, JPEG, PNG, GIF, BMP, TIFF, TIF, WEBP, ICO, PPM, PGM, PBM, PNM, DIB, EPS, PCX, SGI, TGA, XBM, XPM, IM, MSP
Document Formats: PDF (multi-page support)
```

### Output Formats
```
JPEG, PNG, TIFF, BMP, GIF, WEBP, ICO, PPM, TGA, PCX
```

## 🛠️ Installation

### Requirements
- Python 3.7+
- pip

### Quick Install
```bash
# Clone the project
git clone https://github.com/yourusername/ConvertAnyImage.git
cd ConvertAnyImage

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
- `PyMuPDF>=1.23.0` - PDF processing
- `Pillow>=10.0.0` - Image processing

## 🚀 Usage

### Basic Syntax
```bash
python main.py <input_folder> [output_folder] [options]
```

### Quick Start
```bash
# Convert to PNG format (default, lossless)
python main.py ./input_folder

# Convert to WEBP format with 90% quality
python main.py ./input_folder -f WEBP -q 90

# Convert to JPEG with specified output folder
python main.py ./input_folder ./my_output -f JPEG -d 300 -q 95

# High-quality TIFF conversion
python main.py ./input_folder -f TIFF -d 600 -q 100
```

### Parameter Description

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| `input_folder` | Input folder path (required) | - | `./images` |
| `output_folder` | Output folder path (optional) | `output` | `./converted` |
| `-f, --format` | Output format | `PNG` | `WEBP`, `JPEG` |
| `-d, --dpi` | Output resolution | `400` | `300`, `600` |
| `-q, --quality` | Image quality (1-100) | `100` | `95`, `90` |

### Recommended DPI Settings
- **150 DPI**: Web display
- **300 DPI**: Standard printing
- **400 DPI**: High-quality output (default)
- **600 DPI**: Professional grade quality

## 📊 Conversion Examples

### Batch Conversion Results
```
Found 3 files, starting conversion to WEBP format...
Output quality: 95%, DPI: 400

[1/3] Converting: photo1.jpg -> photo1.webp
    Completed: 2.3MB -> 1.8MB
[2/3] Converting: document.pdf -> document.webp  
    Completed: 1.5MB -> 0.9MB
[3/3] Converting: image.png -> image.webp
    Completed: 4.1MB -> 2.2MB

Conversion completed! Success: 3/3, Time: 2.1s
Output files saved to: output
```

## 🔧 Advanced Features

### PDF Processing
- **Single-page PDF**: Direct conversion to specified format
- **Multi-page PDF**: 
  - TIFF format: Save as multi-page TIFF
  - Other formats: Merge into long image

### Transparency Handling
- **PNG/GIF**: Perfect preservation of transparent backgrounds
- **JPEG Conversion**: Automatic white background addition (JPEG doesn't support transparency)

### Color Mode Optimization
- Automatic detection and conversion to most suitable color mode
- Avoid unnecessary color space conversions
- Maintain original image color accuracy

<div align="center">

⭐ If this project helps you, please give it a Star!

Made with ❤️ by [leastbit](https://github.com/leastbit)

</div>