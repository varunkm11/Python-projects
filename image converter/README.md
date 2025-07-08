# Image Converter Pro

A modern, minimalist image converter built with Python and tkinter. Convert your images between various formats with an elegant and user-friendly interface.

## Features

- **Multiple Format Support**: Convert between JPG, PNG, BMP, TIFF, WebP, and ICO formats
- **Batch Processing**: Convert multiple images at once
- **Quality Control**: Adjust JPEG quality settings (1-100)
- **Modern UI**: Dark theme with clean, minimalist design
- **Progress Tracking**: Real-time conversion progress with status updates
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Supported Formats

### Input Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- WebP (.webp)
- ICO (.ico)

### Output Formats
- JPEG (.jpg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)
- ICO (.ico)

## Installation

1. Make sure you have Python 3.6 or higher installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python image_converter.py
   ```

2. **Select Images**: Click "📁 Choose Files" to select one or more images to convert

3. **Choose Settings**:
   - Select your desired output format from the dropdown
   - Adjust quality settings (for JPEG output)
   - Choose an output folder where converted images will be saved

4. **Convert**: Click "🚀 Convert Images" to start the conversion process

5. **Monitor Progress**: Watch the progress bar and status updates as your images are converted

## Features Explained

### Quality Settings
- **JPEG Quality**: Ranges from 1 (lowest quality, smallest file) to 100 (highest quality, largest file)
- **Optimization**: Automatically enabled for PNG and JPEG formats to reduce file size

### Batch Processing
- Select multiple images at once
- All images will be converted to the same output format
- Progress tracking shows current file being processed

### Error Handling
- Gracefully handles unsupported files
- Shows detailed success/failure statistics
- Continues processing remaining files if one fails

## Technical Details

- Built with Python's tkinter for the GUI
- Uses Pillow (PIL) for image processing
- Threaded conversion to prevent UI freezing
- Automatic RGBA to RGB conversion for JPEG compatibility
- Modern styling with custom ttk themes

## System Requirements

- Python 3.6+
- tkinter (usually included with Python)
- Pillow library
- Sufficient disk space for converted images

## Troubleshooting

### Common Issues

1. **"Module not found" error**: Make sure Pillow is installed
   ```bash
   pip install Pillow
   ```

2. **File permission errors**: Ensure you have write permissions to the output folder

3. **Large file processing**: Very large images may take longer to process - this is normal

4. **RGBA to RGB conversion**: When converting PNG with transparency to JPEG, a white background is automatically added

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!

---

**Image Converter Pro** - Making image conversion simple and beautiful.
