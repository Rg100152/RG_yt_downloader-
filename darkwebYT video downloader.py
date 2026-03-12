import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import re
import random
import time
from datetime import datetime
import subprocess

# Try to import yt-dlp
try:
    import yt_dlp
    YT_DLP_AVAILABLE = True
except:
    YT_DLP_AVAILABLE = False

class DarkWebDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("🌐 R.G DARKWEB DOWNLOADER v2.0")
        self.root.geometry("1200x800")
        
        # Dark Web Colors
        self.colors = {
            'bg': '#000000',           # Pure black
            'darker': '#0A0A0A',        # Slightly lighter black
            'card': '#111111',           # Dark card
            'terminal': '#0F0F0F',       # Terminal black
            'hacker_green': '#00FF00',   # Matrix green
            'blood_red': '#FF0000',       # Blood red
            'warning_yellow': '#FFFF00',  # Warning yellow
            'cyan_hacker': '#00FFFF',     # Hacker cyan
            'purple_dark': '#800080',      # Dark purple
            'text_green': '#00AA00',       # Dim green
            'text_red': '#AA0000',          # Dim red
            'glitch': '#FF00FF'              # Glitch pink
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Download variables
        self.download_path = os.path.expanduser("~/Downloads")
        self.is_downloading = False
        self.current_download = None
        self.quality_var = tk.StringVar(value="best")
        self.format_var = tk.StringVar(value="mp4")
        self.playlist_var = tk.BooleanVar(value=False)
        self.audio_only_var = tk.BooleanVar(value=False)
        
        # Glitch effect
        self.glitch_chars = ['█', '▓', '▒', '░', '║', '═', '╔', '╗', '╚', '╝']
        self.glitch_active = False
        
        # History
        self.download_history = []
        
        # Console lines
        self.console_lines = []
        
        self.setup_gui()
        self.type_effect("> Initializing darkweb connection...", 0)
        self.root.after(2000, lambda: self.type_effect("> Connection secured!", 1))
        self.root.after(4000, lambda: self.type_effect("> DarkWeb access granted!", 2))
        
    def setup_gui(self):
        """Setup the hacker GUI"""
        
        # Main container with border
        self.main = tk.Frame(
            self.root, 
            bg=self.colors['bg'],
            highlightbackground=self.colors['hacker_green'],
            highlightthickness=1
        )
        self.main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header with glitch effect
        self.create_header()
        
        # Terminal style URL input
        self.create_terminal_section()
        
        # Hacker options
        self.create_hacker_options()
        
        # Progress with matrix effect
        self.create_matrix_progress()
        
        # Console output
        self.create_console()
        
        # Status bar
        self.create_status_bar()
        
    def create_header(self):
        """Create hacker header"""
        header = tk.Frame(self.main, bg=self.colors['bg'])
        header.pack(fill=tk.X, pady=(5, 10))
        
        # ASCII Art
        ascii_art = """
    ░██████╗░██████╗      ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
    ██╔════╝░██╔══██╗     ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██║░░██╗░██████╔╝     ██║░░██║██████╦╝██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║██║░░██║██████╔╝█████╗░░██████╔╝
    ██║░░╚██╗██╔══██╗     ██║░░██║██╔══██╗██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██║░░██║██╔══██╗██╔══╝░░██╔══██╗
    ╚██████╔╝██║░░██║     ██████╔╝██████╦╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝╚█████╔╝██║░░██║███████╗██║░░██║
    ░╚═════╝░╚═╝░░╚═╝     ╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
        """
        
        ascii_label = tk.Label(
            header,
            text=ascii_art,
            font=("Courier", 8),
            bg=self.colors['bg'],
            fg=self.colors['hacker_green']
        )
        ascii_label.pack()
        
        # Warning text
        warning = tk.Frame(header, bg=self.colors['bg'])
        warning.pack(fill=tk.X, pady=5)
        
        tk.Label(
            warning,
            text="⚠️ DARKWEB ZONE - ENCRYPTED CONNECTION ⚠️",
            font=("Courier", 10, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['warning_yellow']
        ).pack()
        
        tk.Label(
            warning,
            text="[ FOR EDUCATIONAL PURPOSES ONLY ]",
            font=("Courier", 9),
            bg=self.colors['bg'],
            fg=self.colors['text_red']
        ).pack()
        
    def create_terminal_section(self):
        """Create terminal-style URL input"""
        terminal = tk.Frame(self.main, bg=self.colors['terminal'])
        terminal.pack(fill=tk.X, padx=10, pady=5)
        
        # Terminal header
        term_header = tk.Frame(terminal, bg=self.colors['darker'])
        term_header.pack(fill=tk.X)
        
        tk.Label(
            term_header,
            text="🌐 DARKWEB TERMINAL v2.0",
            font=("Courier", 9, "bold"),
            bg=self.colors['darker'],
            fg=self.colors['hacker_green']
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Label(
            term_header,
            text="[ENCRYPTED]",
            font=("Courier", 8),
            bg=self.colors['darker'],
            fg=self.colors['text_red']
        ).pack(side=tk.RIGHT, padx=5)
        
        # URL input with prompt
        url_frame = tk.Frame(terminal, bg=self.colors['terminal'])
        url_frame.pack(fill=tk.X, padx=5, pady=10)
        
        tk.Label(
            url_frame,
            text="root@darkweb:~$",
            font=("Courier", 11, "bold"),
            bg=self.colors['terminal'],
            fg=self.colors['hacker_green']
        ).pack(side=tk.LEFT)
        
        self.url_entry = tk.Entry(
            url_frame,
            font=("Courier", 11),
            bg=self.colors['darker'],
            fg=self.colors['hacker_green'],
            insertbackground=self.colors['hacker_green'],
            borderwidth=0,
            relief=tk.FLAT
        )
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipady=5)
        
        # Blinking cursor effect
        self.cursor_label = tk.Label(
            url_frame,
            text="█",
            font=("Courier", 11),
            bg=self.colors['terminal'],
            fg=self.colors['hacker_green']
        )
        self.cursor_label.pack(side=tk.LEFT)
        self.blink_cursor()
        
        # Terminal buttons
        btn_frame = tk.Frame(terminal, bg=self.colors['terminal'])
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        buttons = [
            ("[ EXECUTE ]", self.start_download, self.colors['hacker_green']),
            ("[ ANALYZE ]", self.get_video_info, self.colors['cyan_hacker']),
            ("[ CLEAR ]", self.clear_url, self.colors['warning_yellow']),
            ("[ PASTE ]", self.paste_url, self.colors['purple_dark'])
        ]
        
        for text, cmd, color in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                command=cmd,
                font=("Courier", 9, "bold"),
                bg=self.colors['darker'],
                fg=color,
                activebackground=self.colors['bg'],
                activeforeground=color,
                relief=tk.FLAT,
                cursor="hand2",
                borderwidth=1,
                highlightbackground=color
            )
            btn.pack(side=tk.LEFT, padx=2)
            
    def create_hacker_options(self):
        """Create hacker-style options panel"""
        options = tk.Frame(self.main, bg=self.colors['terminal'])
        options.pack(fill=tk.X, padx=10, pady=5)
        
        # Options header
        header = tk.Frame(options, bg=self.colors['darker'])
        header.pack(fill=tk.X)
        
        tk.Label(
            header,
            text="> ACCESS PARAMETERS <",
            font=("Courier", 10, "bold"),
            bg=self.colors['darker'],
            fg=self.colors['blood_red']
        ).pack()
        
        # Options grid
        grid = tk.Frame(options, bg=self.colors['terminal'])
        grid.pack(fill=tk.X, padx=10, pady=10)
        
        # Quality selection
        quality_frame = tk.Frame(grid, bg=self.colors['terminal'])
        quality_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            quality_frame,
            text="[>] QUALITY PROTOCOL:",
            font=("Courier", 9),
            bg=self.colors['terminal'],
            fg=self.colors['cyan_hacker']
        ).pack(side=tk.LEFT, padx=5)
        
        qualities = [
            ("MAXIMUM", "best"),
            ("1080p", "1080"),
            ("720p", "720"),
            ("480p", "480"),
            ("MINIMUM", "360")
        ]
        
        for text, value in qualities:
            rb = tk.Radiobutton(
                quality_frame,
                text=text,
                value=value,
                variable=self.quality_var,
                bg=self.colors['terminal'],
                fg=self.colors['hacker_green'],
                selectcolor=self.colors['bg'],
                activebackground=self.colors['terminal'],
                font=("Courier", 8)
            )
            rb.pack(side=tk.LEFT, padx=5)
            
        # Format and options
        bottom_frame = tk.Frame(grid, bg=self.colors['terminal'])
        bottom_frame.pack(fill=tk.X, pady=5)
        
        # Format
        tk.Label(
            bottom_frame,
            text="[>] ENCRYPTION:",
            font=("Courier", 9),
            bg=self.colors['terminal'],
            fg=self.colors['cyan_hacker']
        ).pack(side=tk.LEFT, padx=5)
        
        formats = [("MP4", "mp4"), ("WEBM", "webm"), ("MKV", "mkv")]
        for text, value in formats:
            rb = tk.Radiobutton(
                bottom_frame,
                text=text,
                value=value,
                variable=self.format_var,
                bg=self.colors['terminal'],
                fg=self.colors['hacker_green'],
                selectcolor=self.colors['bg'],
                activebackground=self.colors['terminal'],
                font=("Courier", 8)
            )
            rb.pack(side=tk.LEFT, padx=5)
            
        # Checkboxes
        cb_frame = tk.Frame(grid, bg=self.colors['terminal'])
        cb_frame.pack(fill=tk.X, pady=5)
        
        self.audio_cb = tk.Checkbutton(
            cb_frame,
            text="[x] AUDIO ONLY (MP3)",
            variable=self.audio_only_var,
            command=self.toggle_audio_only,
            bg=self.colors['terminal'],
            fg=self.colors['warning_yellow'],
            selectcolor=self.colors['bg'],
            activebackground=self.colors['terminal'],
            font=("Courier", 9)
        )
        self.audio_cb.pack(side=tk.LEFT, padx=10)
        
        self.playlist_cb = tk.Checkbutton(
            cb_frame,
            text="[x] PLAYLIST MODE",
            variable=self.playlist_var,
            bg=self.colors['terminal'],
            fg=self.colors['warning_yellow'],
            selectcolor=self.colors['bg'],
            activebackground=self.colors['terminal'],
            font=("Courier", 9)
        )
        self.playlist_cb.pack(side=tk.LEFT, padx=10)
        
        # Download path
        path_frame = tk.Frame(grid, bg=self.colors['terminal'])
        path_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            path_frame,
            text="[>] OUTPUT PATH:",
            font=("Courier", 9),
            bg=self.colors['terminal'],
            fg=self.colors['cyan_hacker']
        ).pack(side=tk.LEFT, padx=5)
        
        self.path_label = tk.Label(
            path_frame,
            text=self.download_path,
            font=("Courier", 8),
            bg=self.colors['terminal'],
            fg=self.colors['hacker_green']
        )
        self.path_label.pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            path_frame,
            text="[CHANGE]",
            command=self.browse_folder,
            font=("Courier", 8, "bold"),
            bg=self.colors['darker'],
            fg=self.colors['purple_dark'],
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.RIGHT, padx=5)
        
    def create_matrix_progress(self):
        """Create Matrix-style progress display"""
        progress = tk.Frame(self.main, bg=self.colors['terminal'])
        progress.pack(fill=tk.X, padx=10, pady=5)
        
        # Progress header
        header = tk.Frame(progress, bg=self.colors['darker'])
        header.pack(fill=tk.X)
        
        tk.Label(
            header,
            text="> DOWNLOAD PROGRESS <",
            font=("Courier", 10, "bold"),
            bg=self.colors['darker'],
            fg=self.colors['hacker_green']
        ).pack()
        
        # Progress bar (custom)
        self.progress_frame = tk.Frame(progress, bg=self.colors['terminal'])
        self.progress_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.progress_canvas = tk.Canvas(
            self.progress_frame,
            height=30,
            bg=self.colors['bg'],
            highlightthickness=1,
            highlightbackground=self.colors['hacker_green']
        )
        self.progress_canvas.pack(fill=tk.X)
        
        # Progress text
        text_frame = tk.Frame(progress, bg=self.colors['terminal'])
        text_frame.pack(fill=tk.X, padx=10, pady=(0, 5))
        
        self.progress_text = tk.Label(
            text_frame,
            text="[ WAITING FOR TARGET ]",
            font=("Courier", 9),
            bg=self.colors['terminal'],
            fg=self.colors['text_green']
        )
        self.progress_text.pack(side=tk.LEFT)
        
        self.speed_text = tk.Label(
            text_frame,
            text="",
            font=("Courier", 9),
            bg=self.colors['terminal'],
            fg=self.colors['cyan_hacker']
        )
        self.speed_text.pack(side=tk.RIGHT)
        
    def create_console(self):
        """Create hacker console output"""
        console = tk.Frame(self.main, bg=self.colors['terminal'])
        console.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Console header
        header = tk.Frame(console, bg=self.colors['darker'])
        header.pack(fill=tk.X)
        
        tk.Label(
            header,
            text="> CONSOLE OUTPUT <",
            font=("Courier", 10, "bold"),
            bg=self.colors['darker'],
            fg=self.colors['blood_red']
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            header,
            text="[CLEAR]",
            command=self.clear_console,
            font=("Courier", 8),
            bg=self.colors['darker'],
            fg=self.colors['warning_yellow'],
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.RIGHT, padx=5)
        
        # Console output
        console_frame = tk.Frame(console, bg=self.colors['terminal'])
        console_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(console_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.console = tk.Text(
            console_frame,
            bg=self.colors['bg'],
            fg=self.colors['hacker_green'],
            font=("Courier", 9),
            yscrollcommand=scrollbar.set,
            borderwidth=0,
            height=8
        )
        self.console.pack(fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.console.yview)
        
    def create_status_bar(self):
        """Create hacker status bar"""
        status = tk.Frame(self.main, bg=self.colors['darker'])
        status.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Status indicators
        indicators = [
            ("🌐", "DARKWEB", self.colors['hacker_green']),
            ("🔒", "ENCRYPTED", self.colors['cyan_hacker']),
            ("⚡", "ACTIVE", self.colors['warning_yellow']),
            ("💀", "ANONYMOUS", self.colors['blood_red'])
        ]
        
        for icon, text, color in indicators:
            frame = tk.Frame(status, bg=self.colors['darker'])
            frame.pack(side=tk.LEFT, padx=10)
            
            tk.Label(
                frame,
                text=icon,
                font=("Courier", 10),
                bg=self.colors['darker'],
                fg=color
            ).pack(side=tk.LEFT)
            
            tk.Label(
                frame,
                text=text,
                font=("Courier", 8),
                bg=self.colors['darker'],
                fg=color
            ).pack(side=tk.LEFT, padx=(2, 0))
            
        # Random hex
        hex_text = f"0x{random.randint(1000, 9999):X}"
        tk.Label(
            status,
            text=hex_text,
            font=("Courier", 8),
            bg=self.colors['darker'],
            fg=self.colors['text_green']
        ).pack(side=tk.RIGHT, padx=10)
        
    def blink_cursor(self):
        """Blink cursor effect"""
        current = self.cursor_label.cget('text')
        if current == '█':
            self.cursor_label.config(text=' ')
        else:
            self.cursor_label.config(text='█')
        self.root.after(500, self.blink_cursor)
        
    def type_effect(self, text, line):
        """Typewriter effect for console"""
        if line < len(self.console_lines):
            self.console_lines[line] = text
        else:
            self.console_lines.append(text)
            
        self.update_console()
        
    def update_console(self):
        """Update console display"""
        self.console.delete(1.0, tk.END)
        for line in self.console_lines[-15:]:  # Show last 15 lines
            self.console.insert(tk.END, line + '\n')
        self.console.see(tk.END)
        
    def console_print(self, text):
        """Print to console with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        line = f"[{timestamp}] {text}"
        self.console_lines.append(line)
        self.update_console()
        
    def glitch_text(self, text):
        """Create glitch effect text"""
        if random.random() < 0.1:  # 10% chance of glitch
            chars = list(text)
            for i in range(len(chars)):
                if random.random() < 0.3:
                    chars[i] = random.choice(self.glitch_chars)
            return ''.join(chars)
        return text
        
    def paste_url(self):
        """Paste URL from clipboard"""
        try:
            url = self.root.clipboard_get()
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)
            self.console_print(f"> URL loaded: {url[:50]}...")
        except:
            pass
            
    def clear_url(self):
        """Clear URL entry"""
        self.url_entry.delete(0, tk.END)
        self.console_print("> URL cleared")
        
    def browse_folder(self):
        """Browse for download folder"""
        folder = filedialog.askdirectory(
            title="Select Output Directory",
            initialdir=self.download_path
        )
        if folder:
            self.download_path = folder
            self.path_label.config(text=folder)
            self.console_print(f"> Output path changed: {folder}")
            
    def toggle_audio_only(self):
        """Toggle audio only mode"""
        if self.audio_only_var.get():
            self.console_print("> Audio extraction mode activated")
            
    def get_video_info(self):
        """Get video information"""
        url = self.url_entry.get().strip()
        if not url:
            self.console_print("> ERROR: No target URL")
            return
            
        self.console_print("> Analyzing target...")
        
        def fetch_info():
            try:
                ydl_opts = {'quiet': True, 'no_warnings': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    
                    if 'entries' in info:  # Playlist
                        title = info.get('title', 'Unknown')
                        count = len(info['entries'])
                        self.root.after(0, lambda: self.console_print(
                            f"> PLAYLIST: {title} | Videos: {count}"
                        ))
                    else:  # Single video
                        title = info.get('title', 'Unknown')
                        duration = info.get('duration', 0)
                        uploader = info.get('uploader', 'Unknown')
                        views = info.get('view_count', 0)
                        
                        minutes = duration // 60
                        seconds = duration % 60
                        
                        self.root.after(0, lambda: self.console_print(
                            f"> TITLE: {title}"
                        ))
                        self.root.after(0, lambda: self.console_print(
                            f"> UPLOADER: {uploader} | DURATION: {minutes}:{seconds:02d}"
                        ))
                        self.root.after(0, lambda: self.console_print(
                            f"> VIEWS: {views:,}"
                        ))
                        
            except Exception as e:
                self.root.after(0, lambda: self.console_print(f"> ERROR: {str(e)}"))
                
        thread = threading.Thread(target=fetch_info)
        thread.daemon = True
        thread.start()
        
    def start_download(self):
        """Start download"""
        url = self.url_entry.get().strip()
        if not url:
            self.console_print("> ERROR: No target URL")
            return
            
        if self.is_downloading:
            self.console_print("> ERROR: Download already in progress")
            return
            
        self.is_downloading = True
        self.console_print("> INITIATING DOWNLOAD PROTOCOL...")
        self.console_print("> Encrypting connection...")
        
        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.daemon = True
        thread.start()
        
    def download_video(self, url):
        """Download video"""
        try:
            # Prepare options
            if self.audio_only_var.get():
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.progress_hook],
                    'quiet': True,
                }
                self.root.after(0, lambda: self.console_print("> Audio extraction enabled"))
            else:
                quality = self.quality_var.get()
                if quality == 'best':
                    format_spec = 'bestvideo+bestaudio/best'
                else:
                    format_spec = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'
                    
                ydl_opts = {
                    'format': format_spec,
                    'merge_output_format': self.format_var.get(),
                    'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.progress_hook],
                    'quiet': True,
                }
                
            if self.playlist_var.get():
                ydl_opts['yes_playlist'] = True
                self.root.after(0, lambda: self.console_print("> Playlist mode activated"))
                
            self.root.after(0, lambda: self.console_print("> Connecting to darkweb servers..."))
            
            # Download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                if 'entries' in info:
                    title = info['title']
                    count = len(info['entries'])
                    self.root.after(0, lambda: self.console_print(
                        f"> SUCCESS: Playlist '{title}' downloaded ({count} videos)"
                    ))
                else:
                    title = info.get('title', 'Video')
                    self.root.after(0, lambda: self.console_print(
                        f"> SUCCESS: '{title}' downloaded to {self.download_path}"
                    ))
                    
        except Exception as e:
            self.root.after(0, lambda: self.console_print(f"> ERROR: {str(e)}"))
        finally:
            self.is_downloading = False
            
    def progress_hook(self, d):
        """Progress hook"""
        if d['status'] == 'downloading':
            if 'total_bytes' in d:
                total = d['total_bytes']
                downloaded = d['downloaded_bytes']
                percent = (downloaded / total) * 100
                
                downloaded_mb = downloaded / (1024 * 1024)
                total_mb = total / (1024 * 1024)
                
                # Update progress bar
                self.root.after(0, lambda: self.update_progress(percent))
                
                # Update text
                text = f"[ DOWNLOADING ] {downloaded_mb:.1f} MB / {total_mb:.1f} MB ({percent:.1f}%)"
                self.root.after(0, lambda: self.progress_text.config(text=text))
                
                # Speed
                if 'speed' in d and d['speed']:
                    speed = d['speed'] / (1024 * 1024)
                    self.root.after(0, lambda: self.speed_text.config(
                        text=f"⚡ {speed:.1f} MB/s"
                    ))
                    
        elif d['status'] == 'finished':
            self.root.after(0, lambda: self.progress_text.config(
                text="[ PROCESSING ] Converting..."
            ))
            
    def update_progress(self, percent):
        """Update progress bar"""
        self.progress_canvas.delete("all")
        width = self.progress_canvas.winfo_width()
        if width > 10:
            bar_width = width * percent / 100
            self.progress_canvas.create_rectangle(
                0, 0, bar_width, 30,
                fill=self.colors['hacker_green'],
                outline=""
            )
            
            # Matrix code effect
            for i in range(int(bar_width // 10)):
                x = i * 10 + random.randint(0, 5)
                y = random.randint(5, 25)
                char = random.choice(['0', '1', '█', '▓'])
                self.progress_canvas.create_text(
                    x, y, text=char,
                    fill=self.colors['bg'],
                    font=("Courier", 8)
                )
                
    def clear_console(self):
        """Clear console output"""
        self.console_lines = []
        self.console.delete(1.0, tk.END)
        self.console_print("> Console cleared")
        self.console_print("> System ready")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DarkWebDownloader(root)
    root.mainloop()