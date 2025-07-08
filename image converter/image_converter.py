import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import threading
from pathlib import Path
import io

class ModernImageConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter Pro")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")
        
        # Make window resizable
        self.root.resizable(True, True)
        
        # Center the window
        self.center_window()
        
        # Configure style
        self.setup_styles()
        
        # Variables
        self.selected_files = []
        self.output_format = tk.StringVar(value="jpg")
        self.output_quality = tk.IntVar(value=95)
        self.output_folder = tk.StringVar()
        
        # Create UI
        self.create_ui()
        
        # Supported formats
        self.input_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp', '.ico'}
        self.output_formats = ['jpg', 'png', 'bmp', 'tiff', 'webp', 'ico']
        
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        bg_color = "#1e1e1e"
        fg_color = "#ffffff"
        accent_color = "#4a9eff"
        button_color = "#2d2d2d"
        
        # Configure styles
        self.style.configure('Title.TLabel', 
                           background=bg_color, 
                           foreground=fg_color, 
                           font=('Segoe UI', 24, 'bold'))
        
        self.style.configure('Subtitle.TLabel', 
                           background=bg_color, 
                           foreground="#b0b0b0", 
                           font=('Segoe UI', 11))
        
        self.style.configure('Modern.TButton',
                           background=button_color,
                           foreground=fg_color,
                           borderwidth=0,
                           focuscolor='none',
                           relief='flat',
                           font=('Segoe UI', 10))
        
        self.style.map('Modern.TButton',
                      background=[('active', accent_color),
                                ('pressed', '#3a7ecf')])
        
        self.style.configure('Accent.TButton',
                           background=accent_color,
                           foreground=fg_color,
                           borderwidth=0,
                           focuscolor='none',
                           relief='flat',
                           font=('Segoe UI', 11, 'bold'))
        
        self.style.map('Accent.TButton',
                      background=[('active', '#3a7ecf'),
                                ('pressed', '#2e6bb8')])
        
        self.style.configure('Modern.TFrame', background=bg_color)
        self.style.configure('Card.TFrame', background="#2d2d2d", relief='flat', borderwidth=1)
        
        self.style.configure('Modern.TCombobox',
                           background=button_color,
                           foreground=fg_color,
                           fieldbackground=button_color,
                           borderwidth=0,
                           relief='flat')
        
    def create_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, style='Modern.TFrame')
        main_frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Title section
        title_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        title_frame.pack(fill='x', pady=(0, 30))
        
        title_label = ttk.Label(title_frame, text="Image Converter Pro", style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, 
                                 text="Convert your images to any format with ease", 
                                 style='Subtitle.TLabel')
        subtitle_label.pack(pady=(5, 0))
        
        # File selection section
        file_frame = ttk.Frame(main_frame, style='Card.TFrame')
        file_frame.pack(fill='x', pady=(0, 20), ipady=20, ipadx=20)
        
        file_label = ttk.Label(file_frame, text="Select Images", 
                              font=('Segoe UI', 14, 'bold'), 
                              background="#2d2d2d", foreground="#ffffff")
        file_label.pack(anchor='w', pady=(0, 10))
        
        file_button_frame = ttk.Frame(file_frame, style='Modern.TFrame')
        file_button_frame.pack(fill='x')
        
        select_btn = ttk.Button(file_button_frame, text="📁 Choose Files", 
                               command=self.select_files, style='Modern.TButton')
        select_btn.pack(side='left', padx=(0, 10))
        
        clear_btn = ttk.Button(file_button_frame, text="🗑️ Clear", 
                              command=self.clear_files, style='Modern.TButton')
        clear_btn.pack(side='left')
        
        # File list
        self.file_listbox = tk.Listbox(file_frame, 
                                      bg="#1e1e1e", 
                                      fg="#ffffff", 
                                      selectbackground="#4a9eff",
                                      borderwidth=0,
                                      font=('Segoe UI', 10),
                                      height=6)
        self.file_listbox.pack(fill='x', pady=(15, 0))
        
        # Settings section
        settings_frame = ttk.Frame(main_frame, style='Card.TFrame')
        settings_frame.pack(fill='x', pady=(0, 20), ipady=20, ipadx=20)
        
        settings_label = ttk.Label(settings_frame, text="Conversion Settings", 
                                  font=('Segoe UI', 14, 'bold'), 
                                  background="#2d2d2d", foreground="#ffffff")
        settings_label.pack(anchor='w', pady=(0, 15))
        
        # Format selection
        format_frame = ttk.Frame(settings_frame, style='Modern.TFrame')
        format_frame.pack(fill='x', pady=(0, 15))
        
        format_label = ttk.Label(format_frame, text="Output Format:", 
                                font=('Segoe UI', 11), 
                                background="#2d2d2d", foreground="#b0b0b0")
        format_label.pack(side='left')
        
        format_combo = ttk.Combobox(format_frame, 
                                   textvariable=self.output_format,
                                   values=self.output_formats,
                                   state='readonly',
                                   style='Modern.TCombobox',
                                   font=('Segoe UI', 10),
                                   width=15)
        format_combo.pack(side='right')
        
        # Quality selection
        quality_frame = ttk.Frame(settings_frame, style='Modern.TFrame')
        quality_frame.pack(fill='x', pady=(0, 15))
        
        quality_label = ttk.Label(quality_frame, text="Quality (for JPEG):", 
                                 font=('Segoe UI', 11), 
                                 background="#2d2d2d", foreground="#b0b0b0")
        quality_label.pack(side='left')
        
        quality_scale = tk.Scale(quality_frame, 
                               variable=self.output_quality,
                               from_=1, to=100,
                               orient='horizontal',
                               bg="#2d2d2d",
                               fg="#ffffff",
                               highlightthickness=0,
                               troughcolor="#1e1e1e",
                               activebackground="#4a9eff",
                               font=('Segoe UI', 9))
        quality_scale.pack(side='right', fill='x', expand=True, padx=(20, 0))
        
        # Output folder selection
        output_frame = ttk.Frame(settings_frame, style='Modern.TFrame')
        output_frame.pack(fill='x')
        
        output_label = ttk.Label(output_frame, text="Output Folder:", 
                                font=('Segoe UI', 11), 
                                background="#2d2d2d", foreground="#b0b0b0")
        output_label.pack(anchor='w', pady=(0, 5))
        
        output_path_frame = ttk.Frame(output_frame, style='Modern.TFrame')
        output_path_frame.pack(fill='x')
        
        self.output_entry = tk.Entry(output_path_frame, 
                                    textvariable=self.output_folder,
                                    bg="#1e1e1e", 
                                    fg="#ffffff",
                                    borderwidth=0,
                                    font=('Segoe UI', 10),
                                    insertbackground="#ffffff")
        self.output_entry.pack(side='left', fill='x', expand=True, ipady=8)
        
        browse_btn = ttk.Button(output_path_frame, text="Browse", 
                               command=self.select_output_folder, 
                               style='Modern.TButton')
        browse_btn.pack(side='right', padx=(10, 0))
        
        # Convert button
        convert_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        convert_frame.pack(fill='x', pady=(10, 0))
        
        self.convert_btn = ttk.Button(convert_frame, text="🚀 Convert Images", 
                                     command=self.start_conversion, 
                                     style='Accent.TButton')
        self.convert_btn.pack(fill='x', ipady=15)
        
        # Progress bar
        self.progress = ttk.Progressbar(convert_frame, mode='determinate')
        self.progress.pack(fill='x', pady=(15, 0))
        self.progress.pack_forget()  # Hide initially
        
        # Status label
        self.status_label = ttk.Label(convert_frame, text="", 
                                     font=('Segoe UI', 10), 
                                     background="#1e1e1e", foreground="#b0b0b0")
        self.status_label.pack(pady=(10, 0))
        
    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.ico"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("PNG files", "*.png"),
                ("BMP files", "*.bmp"),
                ("TIFF files", "*.tiff *.tif"),
                ("WebP files", "*.webp"),
                ("Icon files", "*.ico"),
                ("All files", "*.*")
            ]
        )
        
        if files:
            self.selected_files = list(files)
            self.update_file_list()
            
    def clear_files(self):
        self.selected_files = []
        self.update_file_list()
        
    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        for file_path in self.selected_files:
            filename = os.path.basename(file_path)
            self.file_listbox.insert(tk.END, filename)
            
    def select_output_folder(self):
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder.set(folder)
            
    def start_conversion(self):
        if not self.selected_files:
            messagebox.showwarning("No Files", "Please select images to convert.")
            return
            
        if not self.output_folder.get():
            messagebox.showwarning("No Output Folder", "Please select an output folder.")
            return
            
        # Start conversion in a separate thread
        self.convert_btn.configure(state='disabled')
        self.progress.pack(fill='x', pady=(15, 0))
        self.progress['maximum'] = len(self.selected_files)
        self.progress['value'] = 0
        
        thread = threading.Thread(target=self.convert_images)
        thread.daemon = True
        thread.start()
        
    def convert_images(self):
        output_format = self.output_format.get().lower()
        quality = self.output_quality.get()
        output_dir = self.output_folder.get()
        
        successful = 0
        failed = 0
        
        for i, file_path in enumerate(self.selected_files):
            try:
                # Update status
                filename = os.path.basename(file_path)
                self.root.after(0, lambda f=filename: self.status_label.configure(text=f"Converting: {f}"))
                
                # Open and convert image
                with Image.open(file_path) as img:
                    # Convert RGBA to RGB for JPEG
                    if output_format in ['jpg', 'jpeg'] and img.mode in ['RGBA', 'LA']:
                        # Create a white background
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        if img.mode == 'RGBA':
                            background.paste(img, mask=img.split()[-1])
                        else:
                            background.paste(img)
                        img = background
                    
                    # Generate output filename
                    base_name = os.path.splitext(filename)[0]
                    output_filename = f"{base_name}.{output_format}"
                    output_path = os.path.join(output_dir, output_filename)
                    
                    # Save with appropriate options
                    save_kwargs = {}
                    if output_format in ['jpg', 'jpeg']:
                        save_kwargs['quality'] = quality
                        save_kwargs['optimize'] = True
                    elif output_format == 'png':
                        save_kwargs['optimize'] = True
                    elif output_format == 'webp':
                        save_kwargs['quality'] = quality
                        save_kwargs['method'] = 6
                    
                    img.save(output_path, format=output_format.upper(), **save_kwargs)
                    successful += 1
                    
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")
                failed += 1
                
            # Update progress
            self.root.after(0, lambda v=i+1: self.progress.configure(value=v))
            
        # Conversion complete
        self.root.after(0, self.conversion_complete, successful, failed)
        
    def conversion_complete(self, successful, failed):
        self.convert_btn.configure(state='normal')
        self.progress.pack_forget()
        
        if failed == 0:
            self.status_label.configure(text=f"✅ Successfully converted {successful} images!")
            messagebox.showinfo("Success", f"Successfully converted {successful} images!")
        else:
            self.status_label.configure(text=f"⚠️ Converted {successful} images, {failed} failed")
            messagebox.showwarning("Conversion Complete", 
                                 f"Converted {successful} images successfully.\n{failed} conversions failed.")

def main():
    root = tk.Tk()
    app = ModernImageConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
