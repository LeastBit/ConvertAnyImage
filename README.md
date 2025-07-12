# 🖼️ ConvertAnyImage - 通用图像格式无损转换工具

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-AGPL-3.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

[中文](./README.md) | [English](./README_EN.md) | [B站教程]()

</div>

## ✨ 核心特色

### 🎯 **几乎无损转换**
- **高质量保持**: 默认100%质量设置，最大程度保持原图质量
- **智能DPI处理**: 默认400 DPI高分辨率输出，确保细节不丢失
- **透明度保护**: 完美处理PNG/GIF透明背景，JPEG自动添加白色背景
- **颜色模式优化**: 智能转换颜色模式，避免色彩失真

### 🚀 **强大功能**
- **全格式支持**: 支持多种主流图像格式互转
- **PDF转图像**: 高质量PDF页面转换为图像
- **批量处理**: 一键转换整个文件夹
- **多页PDF处理**: 支持多页PDF合并或分页保存

## 📋 支持格式

### 输入格式
```
图像格式: JPG, JPEG, PNG, GIF, BMP, TIFF, TIF, WEBP, ICO, PPM, PGM, PBM, PNM, DIB, EPS, PCX, SGI, TGA, XBM, XPM, IM, MSP
文档格式: PDF (多页支持)
```

### 输出格式
```
JPEG, PNG, TIFF, BMP, GIF, WEBP, ICO, PPM, TGA, PCX
```

## 🛠️ 安装

### 环境要求
- Python 3.7+
- pip

### 快速安装
```bash
# 克隆项目
git clone https://github.com/LeastBit/ConvertAnyImage.git
cd ConvertAnyImage

# 安装依赖
pip install -r requirements.txt
```

### 依赖包
- `PyMuPDF>=1.23.0` - PDF处理
- `Pillow>=10.0.0` - 图像处理

## 🚀 使用方法

### 基本语法
```bash
python main.py <输入文件夹> [输出文件夹] [选项]
```

### 快速开始
```bash
# 转换为PNG格式（默认，无损）
python main.py ./input_folder

# 转换为WEBP格式，90%质量
python main.py ./input_folder -f WEBP -q 90

# 转换为JPEG，指定输出文件夹
python main.py ./input_folder ./my_output -f JPEG -d 300 -q 95

# 高质量TIFF转换
python main.py ./input_folder -f TIFF -d 600 -q 100
```

### 参数说明

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `input_folder` | 输入文件夹路径（必需） | - | `./images` |
| `output_folder` | 输出文件夹路径（可选） | `output` | `./converted` |
| `-f, --format` | 输出格式 | `PNG` | `WEBP`, `JPEG` |
| `-d, --dpi` | 输出分辨率 | `400` | `300`, `600` |
| `-q, --quality` | 图像质量(1-100) | `100` | `95`, `90` |

### DPI推荐设置
- **150 DPI**: 网页显示
- **300 DPI**: 标准打印
- **400 DPI**: 高质量输出（默认）
- **600 DPI**: 专业级质量

## 📊 转换示例

### 批量转换效果
```
找到 3 个文件，开始转换为 WEBP 格式...
输出质量: 95%, DPI: 400

[1/3] 正在转换: photo1.jpg -> photo1.webp
    完成: 2.3MB -> 1.8MB
[2/3] 正在转换: document.pdf -> document.webp  
    完成: 1.5MB -> 0.9MB
[3/3] 正在转换: image.png -> image.webp
    完成: 4.1MB -> 2.2MB

转换完成! 成功: 3/3, 用时: 2.1秒
输出文件保存至: output
```

## 🔧 高级功能

### PDF处理
- **单页PDF**: 直接转换为指定格式
- **多页PDF**: 
  - TIFF格式: 保存为多页TIFF
  - 其他格式: 合并为长图

### 透明度处理
- **PNG/GIF**: 完美保持透明背景
- **JPEG转换**: 自动添加白色背景（JPEG不支持透明）

### 颜色模式优化
- 自动检测并转换最适合的颜色模式
- 避免不必要的色彩空间转换
- 保持原图色彩准确性

<div align="center">

⭐ 如果这个项目对您有帮助，请给个Star支持一下！

Made with ❤️ by [leastbit](https://github.com/leastbit)

</div>
