#!/usr/bin/env python3
"""
ConvertAnyImage - Universal Image Format Converter
Copyright (C) 2025 leastbit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

For more information about your rights and obligations under the GPL,
see the LICENSE file included with this program.
"""

import fitz  # PyMuPDF
from PIL import Image
import os
import sys
import time
import argparse
from pathlib import Path

# 支持的输入图像格式（通过PIL）
SUPPORTED_IMAGE_FORMATS = {
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', 
    '.ico', '.ppm', '.pgm', '.pbm', '.pnm', '.dib', '.eps', '.pcx', 
    '.sgi', '.tga', '.xbm', '.xpm', '.im', '.msp'
}

# 支持的输出格式及其配置
OUTPUT_FORMATS = {
    'JPEG': {'extension': '.jpg', 'mode': 'RGB', 'quality': 95},
    'PNG': {'extension': '.png', 'mode': 'RGBA'},
    'TIFF': {'extension': '.tiff', 'compression': 'tiff_lzw'},
    'BMP': {'extension': '.bmp'},
    'GIF': {'extension': '.gif'},
    'WEBP': {'extension': '.webp', 'quality': 95, 'lossless': True},
    'ICO': {'extension': '.ico'},
    'PPM': {'extension': '.ppm'},
    'TGA': {'extension': '.tga'},
    'PCX': {'extension': '.pcx'},
}

def show_license_info():
    """Display GPL license information"""
    print("=" * 70)
    print("ConvertAnyImage - Universal Image Format Converter")
    print("Copyright (C) 2025 leastbit")
    print("")
    print("This program is free software licensed under GPL v3.")
    print("You are free to redistribute and/or modify it under the terms")
    print("of the GNU General Public License as published by the Free")
    print("Software Foundation, either version 3 of the License, or")
    print("(at your option) any later version.")
    print("")
    print("This program is distributed in the hope that it will be useful,")
    print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
    print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.")
    print("")
    print("IMPORTANT: Any derivative works must also be licensed under GPL.")
    print("See the LICENSE file for complete terms and conditions.")
    print("Full license text: https://www.gnu.org/licenses/gpl-3.0.html")
    print("=" * 70)
    print("")

def show_copyright_notice():
    """Display brief copyright notice"""
    print("ConvertAnyImage v1.0 - Copyright (C) 2025 leastbit")
    print("Licensed under GPL v3 - This is free software with ABSOLUTELY NO WARRANTY.")
    print("Type '--license' for license information.")
    print("")

def show_full_license():
    """Display full license information"""
    license_text = """
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

[... Full GPL v3 text continues ...]

For the complete license text, see the LICENSE file included with this
program or visit: https://www.gnu.org/licenses/gpl-3.0.html

IMPORTANT NOTICE FOR DERIVATIVE WORKS:
If you modify this program or create derivative works based on it,
you MUST license your derivative work under the GPL v3 or later.
This ensures that all users continue to have the freedom to use,
study, modify, and distribute the software.
"""
    print(license_text)

def convert_image(input_file, output_file, output_format='PNG', dpi=None, quality=95):
    """
    将各种图像格式转换为指定格式（无损转换）
    
    参数:
        input_file: 输入文件路径
        output_file: 输出文件路径
        output_format: 输出格式（JPEG, PNG, TIFF, BMP, GIF, WEBP, ICO等）
        dpi: 分辨率（仅对支持的格式有效）
        quality: 质量（仅对JPEG和WEBP有效）
    """
    try:
        # 检查输入文件是否为PDF
        if input_file.lower().endswith('.pdf'):
            return convert_pdf_to_image(input_file, output_file, output_format, dpi, quality)
        
        # 处理其他图像格式
        with Image.open(input_file) as img:
            # 获取输出格式配置
            format_config = OUTPUT_FORMATS.get(output_format.upper(), OUTPUT_FORMATS['PNG'])
            
            # 处理透明度和颜色模式
            if output_format.upper() == 'JPEG' and img.mode in ('RGBA', 'LA', 'P'):
                # JPEG不支持透明度，需要转换为RGB
                if img.mode == 'P':
                    img = img.convert('RGBA')
                # 创建白色背景
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])
                img = background
            elif 'mode' in format_config:
                if img.mode != format_config['mode']:
                    img = img.convert(format_config['mode'])
            
            # 准备保存参数
            save_kwargs = {}
            
            # 设置DPI
            if dpi and output_format.upper() in ['TIFF', 'PNG', 'JPEG']:
                save_kwargs['dpi'] = (dpi, dpi)
            
            # 设置质量（仅对JPEG和WEBP）
            if output_format.upper() == 'JPEG':
                save_kwargs['quality'] = quality
                save_kwargs['optimize'] = True
            elif output_format.upper() == 'WEBP':
                if format_config.get('lossless', False):
                    save_kwargs['lossless'] = True
                else:
                    save_kwargs['quality'] = quality
            
            # 设置压缩（仅对TIFF）
            if output_format.upper() == 'TIFF' and 'compression' in format_config:
                save_kwargs['compression'] = format_config['compression']
            
            # 保存图像
            img.save(output_file, format=output_format.upper(), **save_kwargs)
            
        return True
        
    except Exception as e:
        print(f"转换 {input_file} 时出错: {e}")
        return False

def convert_pdf_to_image(input_file, output_file, output_format='PNG', dpi=300, quality=95):
    """
    将PDF转换为图像格式
    """
    try:
        doc = fitz.open(input_file)
        images = []
        
        for page in doc:
            pix = page.get_pixmap(dpi=dpi, colorspace="rgb")
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)
        
        if images:
            if len(images) == 1:
                # 单页PDF，直接保存
                img = images[0]
            else:
                # 多页PDF，合并为一张长图或保存为TIFF多页
                if output_format.upper() == 'TIFF':
                    # TIFF支持多页
                    images[0].save(
                        output_file,
                        save_all=True,
                        append_images=images[1:],
                        compression="tiff_lzw",
                        dpi=(dpi, dpi) if dpi else None
                    )
                    doc.close()
                    return True
                else:
                    # 其他格式合并为长图
                    total_height = sum(img.height for img in images)
                    max_width = max(img.width for img in images)
                    
                    combined = Image.new('RGB', (max_width, total_height))
                    y_offset = 0
                    for img in images:
                        combined.paste(img, (0, y_offset))
                        y_offset += img.height
                    img = combined
            
            # 保存单页或合并后的图像
            save_kwargs = {}
            if dpi and output_format.upper() in ['TIFF', 'PNG', 'JPEG']:
                save_kwargs['dpi'] = (dpi, dpi)
            if output_format.upper() == 'JPEG':
                save_kwargs['quality'] = quality
                save_kwargs['optimize'] = True
            elif output_format.upper() == 'WEBP':
                save_kwargs['quality'] = quality
            
            img.save(output_file, format=output_format.upper(), **save_kwargs)
        
        doc.close()
        return True
        
    except Exception as e:
        print(f"转换PDF {input_file} 时出错: {e}")
        return False

def batch_convert_files(input_folder, output_folder=None, output_format='PNG', dpi=400, quality=100):
    """
    批量转换文件夹中所有支持的图像文件
    
    参数:
        input_folder: 输入文件夹路径
        output_folder: 输出文件夹路径，默认为"output"文件夹
        output_format: 输出格式（JPEG, PNG, TIFF, BMP, GIF, WEBP等）
        dpi: 转换分辨率，默认400
        quality: 图像质量（无损100%），默认100
    """
    # 确保输入文件夹存在
    if not os.path.exists(input_folder) or not os.path.isdir(input_folder):
        print(f"错误: 输入文件夹 '{input_folder}' 不存在!")
        return
        
    # 如果未指定输出文件夹，使用"output"文件夹
    if output_folder is None:
        output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # 获取所有支持的文件（包括PDF和所有图像格式）
    all_supported_extensions = SUPPORTED_IMAGE_FORMATS.union({'.pdf'})
    supported_files = [f for f in os.listdir(input_folder) 
                      if Path(f).suffix.lower() in all_supported_extensions]
    
    if not supported_files:
        print(f"未在 '{input_folder}' 找到支持的文件!")
        print(f"支持的格式: {', '.join(sorted(all_supported_extensions))}")
        return

    total = len(supported_files)
    succeeded = 0
    failed_files = []
    
    # 获取输出格式的文件扩展名
    output_ext = OUTPUT_FORMATS.get(output_format.upper(), OUTPUT_FORMATS['PNG'])['extension']
    
    print(f"找到 {total} 个文件，开始转换为 {output_format.upper()} 格式...")
    print(f"输出质量: {quality}%, DPI: {dpi}")
    start_time = time.time()

    # 逐个转换文件
    for i, file in enumerate(supported_files, 1):
        input_path = os.path.join(input_folder, file)
        output_filename = Path(file).stem + output_ext
        output_path = os.path.join(output_folder, output_filename)
        
        print(f"[{i}/{total}] 正在转换: {file} -> {output_filename}")
        
        success = convert_image(input_path, output_path, output_format, dpi, quality)
        if success:
            succeeded += 1
            # 显示文件大小信息
            try:
                input_size = os.path.getsize(input_path) / 1024 / 1024  # MB
                output_size = os.path.getsize(output_path) / 1024 / 1024  # MB
                print(f"    完成: {input_size:.1f}MB -> {output_size:.1f}MB")
            except:
                print(f"    完成")
        else:
            failed_files.append(file)

    end_time = time.time()
    elapsed = end_time - start_time
    
    print(f"\n转换完成! 成功: {succeeded}/{total}, 用时: {elapsed:.1f}秒")
    print(f"输出文件保存至: {output_folder}")
    
    if failed_files:
        print(f"\n转换失败的文件:")
        for file in failed_files:
            print(f"  - {file}")

def main():
    parser = argparse.ArgumentParser(
        description='ConvertAnyImage - Universal Image Format Converter (GPL v3)',
        epilog='This program is free software licensed under GPL v3. Use --license for details.'
    )
    parser.add_argument('input_folder', nargs='?', help='Input folder path')
    parser.add_argument('output_folder', nargs='?', help='Output folder path (optional, default: output)')
    parser.add_argument('-f', '--format', default='PNG',
                       choices=list(OUTPUT_FORMATS.keys()),
                       help='Output format (default: PNG)')
    parser.add_argument('-d', '--dpi', type=int, default=400,
                       help='Output resolution DPI (default: 400)')
    parser.add_argument('-q', '--quality', type=int, default=100,
                       help='Image quality 1-100 (default: 100 lossless)')
    parser.add_argument('--license', action='store_true',
                       help='Show license information and exit')
    parser.add_argument('--copyright', action='store_true',
                       help='Show copyright notice and exit')

    args = parser.parse_args()

    # Handle license and copyright options
    if args.license:
        show_full_license()
        return

    if args.copyright:
        show_license_info()
        return

    # Show brief copyright notice at startup
    show_copyright_notice()

    # Check if input folder is provided
    if not args.input_folder:
        parser.print_help()
        print("\nERROR: Input folder is required.")
        return
    
    # 验证质量参数
    if not 1 <= args.quality <= 100:
        print("quality must be in range 1-100")
        return
    
    batch_convert_files(
        input_folder=args.input_folder,
        output_folder=args.output_folder,
        output_format=args.format,
        dpi=args.dpi,
        quality=args.quality
    )

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        # Display help information if no arguments or argument errors
        print("\n" + "=" * 60)
        print("ConvertAnyImage - Universal Image Format Converter")
        print("Copyright (C) 2025 leastbit - Licensed under GPL v3")
        print("=" * 60)
        print("\n=== USAGE ===")
        print("python main.py <input_folder> [output_folder] [options]")
        print("\n=== EXAMPLES ===")
        print("python main.py ./input_folder -f WEBP -d 400 -q 90")
        print("python main.py ./input_folder ./my_output -f JPEG -d 300 -q 95")
        print("python main.py ./input_folder -f PNG")
        print("python main.py --license    # Show license information")
        print("\n=== PARAMETERS ===")
        print("input_folder:  Required, folder containing files to convert")
        print("output_folder: Optional, default 'output' folder")
        print("-f format:     Optional, default PNG")
        print("               Supported: JPEG, PNG, TIFF, BMP, GIF, WEBP, ICO, PPM, TGA, PCX")
        print("-d DPI:        Optional, default 400")
        print("               Recommended: 150(web) 300(print) 600(high-quality)")
        print("-q quality:    Optional, default 100(lossless), range 1-100")
        print("--license:     Show full license information")
        print("--copyright:   Show copyright and license summary")
        print("\n=== SUPPORTED INPUT FORMATS ===")
        print("Images: JPG, JPEG, PNG, GIF, BMP, TIFF, WEBP, ICO, PPM, PGM, PBM,")
        print("        PNM, DIB, EPS, PCX, SGI, TGA, XBM, XPM, IM, MSP")
        print("Documents: PDF (multi-page support)")
        print("\n=== GPL LICENSE NOTICE ===")
        print("This is free software: you are free to change and redistribute it.")
        print("There is NO WARRANTY, to the extent permitted by law.")
        print("Any derivative works must also be licensed under GPL v3.")
        print("Use --license for complete license terms.")
        print("=" * 60)
