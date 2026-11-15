"""HEXPYRION native semantic reconstruction — module '__main__'.
Original .py bytes were not embedded.
by dimareverse"""

import tkinter
import cv2
import os
import subprocess
import threading
import time
import requests
import zipfile
import shutil
import sys
import glob
import platform
import ctypes
import numpy
import datetime





ttk = []
filedialog = []
messagebox = []
Image = []
ImageTk = []
def is_admin():
    return __import__('ctypes').windll.shell32.IsUserAnAdmin()

def elevate():
    try:
        script_path = platform.system()
        if script_path == 'Windows':
            python_exe = __import__('sys').argv[0]
            args = sub_181029cc0(python_exe)
            e = args.endswith
            _v1 = sub_18101ad50(e, ('.pyw',))
            if _v1:
                __import__('ntpath').join(__import__('sys').executable.replace(('python.exe', 'pythonw.exe')))
            _v6 = sub_18101ad50(args.endswith, ('.py',))
            if not _v6:
                sub_18101ad50(args.endswith, ('.pyw',))
            if sub_18101ad50(args.endswith, ('.pyw',)):
                pass
            _v12 = 'runas'
            _v13 = _v13[0]
            __import__('ctypes').windll.shell32.ShellExecuteW(None, _v12, _v13[0][0], via_PyUnicode_Join(' ', _v22[1:]), None, 1)
    except Exception:
        print(f"Error during elevation: {''}")
    return True

APP_BASE_DIR = sub_181029da0(sub_181029cc0(__import__('sys').argv[0]))
BUNDLE_DIR = getattr(__import__('sys'), '_MEIPASS', APP_BASE_DIR)
APP_NAME = 'VIDEO RECORDER'
FFMPEG_DOWNLOAD_URL = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'
FFMPEG_EXE_NAME = 'ffmpeg.exe'
LOCAL_FFMPEG = __import__('ntpath').join(BUNDLE_DIR, FFMPEG_EXE_NAME)
SUBDIR_FFMPEG = __import__('ntpath').join(APP_BASE_DIR, 'ffmpeg_bin', FFMPEG_EXE_NAME)
FFMPEG_PATH = LOCAL_FFMPEG
FFMPEG_DIR = BUNDLE_DIR
APP_BASE_DIR = sub_181029da0(__import__('sys').executable)
APP_BASE_DIR = sub_181029da0(sub_181029cc0(__file__))
BUNDLE_DIR = APP_BASE_DIR
FFMPEG_PATH = LOCAL_FFMPEG
FFMPEG_DIR = BUNDLE_DIR
FFMPEG_PATH = SUBDIR_FFMPEG
FFMPEG_DIR = sub_181029da0(FFMPEG_PATH)
ICON_CAMERA = next(sub_180003b80(('📷', '⏱️', '●', '■')))
ICON_DURATION = next(sub_180003b80(('📷', '⏱️', '●', '■')))
ICON_RECORD = next(sub_180003b80(('📷', '⏱️', '●', '■')))
ICON_STOP = next(sub_180003b80(('📷', '⏱️', '●', '■')))
ICON_SETTINGS = next(sub_180003b80(('⚙️', '📁', '🔗', '🔄')))
ICON_FOLDER = next(sub_180003b80(('⚙️', '📁', '🔗', '🔄')))
ICON_MERGE = next(sub_180003b80(('⚙️', '📁', '🔗', '🔄')))
ICON_REFRESH = next(sub_180003b80(('⚙️', '📁', '🔗', '🔄')))
ICON_GUIDE = next(sub_180003b80(('🎯', '➡️')))
ICON_CONVERT = next(sub_180003b80(('🎯', '➡️')))
COLOR_SUCCESS_BG = next(sub_180003b80(('#1B3320', '#81C784')))
COLOR_SUCCESS_FG = sub_1800040a0(sub_180003b80(('#1B3320', '#81C784')), 1)
COLOR_ERROR_BG = next(sub_180003b80(('#3B1A1A', '#E57373')))
COLOR_ERROR_FG = sub_1800040a0(sub_180003b80(('#3B1A1A', '#E57373')), 1)
COLOR_INFO_BG = next(sub_180003b80((THEME_PANEL, THEME_FG)))
COLOR_INFO_FG = sub_1800040a0(sub_180003b80((THEME_PANEL, THEME_FG)), 1)
COLOR_WARNING_BG = next(sub_180003b80(('#332B18', '#FFD54F')))
COLOR_WARNING_FG = sub_1800040a0(sub_180003b80(('#332B18', '#FFD54F')), 1)
class Y4MVideoRecorderApp(THEME_PANEL, THEME_FG):

    def __init__(self, root):
        self.root = root
        btn = self.root.title(APP_NAME)
        self.root.geometry('1150x650')
        self.root.minsize(850, 600)
        self.root.resizable(False, False)
        self.cap = None
        self.ffmpeg_process = None
        self.is_recording = False
        self.video_preview_thread = None
        self.stop_event = threading.Event()
        self.camera_info_str = tk.StringVar(value='Camera: N/A')
        self.current_resolution = None
        self.recordings_folder_path = __import__('ntpath').join(APP_BASE_DIR, RECORDINGS_FOLDER_NAME)
        __import__('os').makedirs(self.recordings_folder_path, exist_ok=True)
        self.setup_gui()
        _v12 = self.ensure_ffmpeg()
        if _v12:
            self.update_camera_list()
            self.refresh_recorded_videos_list()
            self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        else:
            self.update_status('FFmpeg setup incomplete. Functionality will be limited.', 'error')
            for btn in sub_180003b80(('start_button', 'merge_button', 'convert_external_button')):
                while True:
                    getattr(self, _v18, 0).config(state=tk.DISABLED)
                    try:
                        next(sub_180003b80(('start_button', 'merge_button', 'convert_external_button')))
                    except StopIteration:
                        pass
            self.update_camera_list()
            self.refresh_recorded_videos_list()
            self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def _center_window(self, window, width, height):
        window.update_idletasks()
        x = self.root.winfo_x()
        y = x
        window.geometry(f'{width}x{height}+{y + self.root.winfo_width() // 2 - width // 2}+{self.root.winfo_y() + self.root.winfo_height() // 2 - height // 2}')

    def ensure_ffmpeg(self):
        progress_window = sub_181029e10(FFMPEG_PATH)
        if progress_window:
            progress_details_var = f'FFmpeg found: {FFMPEG_PATH}'
            self.update_status(progress_details_var, 'info')
        elif messagebox.askyesno('FFmpeg Downloader', f'{FFMPEG_EXE_NAME} is required. Download now?', parent=self.root):
            _v9 = tk.Toplevel(self.root)
            sub_18101ad50(_v9.title, ('FFmpeg Setup',))
            self._center_window(_v9, 450, 180)
            _v9.grab_set()
            _v13 = tk.StringVar(value='Initializing...')
            _v23 = tk.StringVar(value='')
            _v27 = self._perform_ffmpeg_download_and_setup(_v9, _v13, _v23, ttk.Progressbar(_v9, orient='horizontal', length=410, mode='determinate'))
            _v9.destroy()
            if _v27:
                self.update_status('FFmpeg setup complete', 'success')
            else:
                self.update_status('FFmpeg setup failed.', 'error')
        else:
            self.update_status('FFmpeg download cancelled by user.', 'warning')
        return self._perform_ffmpeg_download_and_setup(tk.Toplevel(self.root), tk.StringVar(value='Initializing...'), tk.StringVar(value=''), ttk.Progressbar(tk.Toplevel(self.root), orient='horizontal', length=410, mode='determinate'))

    def _perform_ffmpeg_download_and_setup(self, progress_window, status_var, details_var, p_bar):
        try:
            zip_download_path = {'exist_ok': True}
            response = __import__('os').makedirs(FFMPEG_DIR, exist_ok=True)
            total_size = 'ffmpeg.zip'
            downloaded_size = __import__('ntpath').join(APP_BASE_DIR, total_size)
            status_var.set('Downloading FFmpeg...')
            details_var.set('Connecting...')
            p_bar['value'] = 0
            progress_window.update_idletasks()
            f = {'stream': True, 'timeout': 60}
            chunk = requests.get(FFMPEG_DOWNLOAD_URL, stream=True, timeout=60)
            chunk.raise_for_status()
            percent = chunk.headers.get(('content-length', 0))
            temp_extract_dir = int(percent)
            p_bar['maximum'] = temp_extract_dir if temp_extract_dir else 100
            zip_ref = 0
            member = open(downloaded_size, 'wb', 0)
            extracted_ffmpeg_exe_source_path = member.__enter__()
            e = member.__exit__
        except Exception:
            progress_window.winfo_exists()
            return f"FFmpeg setup error: {''}"
        try:
            _v1 = iter(requests.get(FFMPEG_DOWNLOAD_URL, stream=True, timeout=60).iter_content(chunk_size=8192))
            via_PyErr_Format(_v1)
            while True:
                if _v42:
                    open(__import__('ntpath').join(APP_BASE_DIR, 'ffmpeg.zip'), 'wb', 0).__enter__().write(_v42)
                    sub_1810336f0(len(_v42))
                if int(requests.get(FFMPEG_DOWNLOAD_URL, stream=True, timeout=60).headers.get(('content-length', 0))) > 0:
                    p_bar['value'] = 0
                    details_var.set(f"{0 // 1024}KB / {int(requests.get(FFMPEG_DOWNLOAD_URL, stream=True, timeout=60).headers.get(('content-length', 0))) // 1024}KB ({0 / int(requests.get(FFMPEG_DOWNLOAD_URL, stream=True, timeout=60).headers.get(('content-length', 0))) * 100:.1f}%)")
                    progress_window.update_idletasks()
                    via_PyErr_Format(_v1)
                    continue
                if p_bar['mode'] != 'indeterminate':
                    p_bar['mode'] = 'indeterminate'
                    p_bar.start(10)
        except StopIteration:
            open(__import__('ntpath').join(APP_BASE_DIR, 'ffmpeg.zip'), 'wb', 0).__exit__((None, None, None))
            p_bar.stop()
            p_bar['mode'] = 'determinate'
            p_bar['value'] = p_bar['maximum']
            details_var.set('Download complete.')
            time.sleep(0.5)
            _v25 = 'ffmpeg_temp_extract'
            status_var.set('Extracting FFmpeg...')
            p_bar['mode'] = 'indeterminate'
            p_bar.start()
            progress_window.update_idletasks()
            time.sleep(0.5)
            _v30 = zipfile.ZipFile(__import__('ntpath').join(APP_BASE_DIR, 'ffmpeg.zip'), 'r')
            _v31 = _v30.__enter__()
            _v32 = _v30.__exit__
            iter(_v31.infolist())
            _v34 = via_PyErr_Format(iter(_v31.infolist()))
            _v34.filename.endswith(FFMPEG_EXE_NAME)
            _v31.extract(_v34, __import__('ntpath').join(APP_BASE_DIR, _v25, APP_BASE_DIR, 'ffmpeg.zip', open(__import__('ntpath').join(APP_BASE_DIR, 'ffmpeg.zip'), 'wb', 0).__enter__()))
            __import__('ntpath').join(__import__('ntpath').join(APP_BASE_DIR, _v25, APP_BASE_DIR, 'ffmpeg.zip', open(__import__('ntpath').join(APP_BASE_DIR, 'ffmpeg.zip'), 'wb', 0).__enter__()), _v34.filename)
            _v32((None, None, None))
            _v32()
            raise Exception(f'{FFMPEG_EXE_NAME} not found in archive.')

    def setup_gui(self):
        top_controls_frame = self.root.configure(bg=THEME_BG)
        main_content_frame = {'padding': (10, 10, 10, 5)}
        right_sidebar_frame = ttk.Frame(self.root, padding=(10, 10, 10, 5))
        recorded_videos_lf = tk.X
        list_scrollbar_y = right_sidebar_frame.pack(fill=recorded_videos_lf)
        bottom_preview_controls_frame = f'{ICON_CAMERA} Camera:'
        self.camera_var = tk.StringVar()
        self.camera_combo = ttk.Combobox(right_sidebar_frame, textvariable=self.camera_var, state='readonly', width=35, font=STYLE_FONT_DEFAULT)
        self.camera_combo.bind('<<ComboboxSelected>>', self.on_camera_select)
        self.duration_var = tk.IntVar(value=10)
        self.duration_entry = ttk.Entry(right_sidebar_frame, textvariable=self.duration_var, width=6, font=STYLE_FONT_DEFAULT)
        self.start_button = ttk.Button(right_sidebar_frame, text=f'{ICON_RECORD} Start', command=self.start_recording, style='Accent.TButton', width=12)
        self.stop_button = ttk.Button(right_sidebar_frame, text=f'{ICON_STOP} Stop', command=self.stop_recording, state=tk.DISABLED, style='Outline.TButton', width=12)
        self.video_label = ttk.Label(ttk.Frame(self.root, padding=(10, 0, 10, 10)), text='Video Preview Area\nSelect a camera to start.', anchor=tk.CENTER, background='#000000', foreground=THEME_FG_DIM, font=('Segoe UI', 12))
        _v70 = '10'
        self.recorded_videos_listbox = tk.Listbox(ttk.LabelFrame(ttk.Frame(ttk.Frame(self.root, padding=(10, 0, 10, 10))), text=f'  {ICON_FOLDER} Recorded Y4M Videos  ', padding=_v70), selectmode=tk.EXTENDED, bg=THEME_ENTRY, fg=THEME_FG, relief=tk.FLAT, selectbackground=THEME_ACCENT, selectforeground='white', font=STYLE_FONT_DEFAULT, borderwidth=0, highlightthickness=1, highlightcolor=THEME_PANEL, highlightbackground=THEME_PANEL)
        ttk.Scrollbar(ttk.LabelFrame(ttk.Frame(ttk.Frame(self.root, padding=(10, 0, 10, 10))), text=f'  {ICON_FOLDER} Recorded Y4M Videos  ', padding=_v70), orient=tk.VERTICAL, command=self.recorded_videos_listbox.yview)
        _v96 = ttk.LabelFrame(ttk.Frame(ttk.Frame(self.root, padding=(10, 0, 10, 10))), text='  File Operations  ', padding='10')
        self.merge_button = ttk.Button(_v96, text=f'{ICON_MERGE} Merge', command=self.merge_videos, style='Accent.TButton')
        self.open_folder_button = ttk.Button(_v96, text=f'{ICON_FOLDER} Folder', command=self.open_recordings_folder, style='Outline.TButton')
        self.convert_external_button = ttk.Button(_v96, text=f'{ICON_CONVERT} Convert to Y4M', command=self.convert_external_video_to_y4m, style='Outline.TButton')
        self.guide_ovals_var = tk.BooleanVar(value=True)
        self.guide_ovals_check = ttk.Checkbutton(ttk.Frame(ttk.Frame(self.root, padding=(10, 0, 10, 10)), padding=(0, 5, 0, 0)), text=f'{ICON_GUIDE} Liveness Guides', variable=self.guide_ovals_var, style='TCheckbutton')
        self.camera_info_label = ttk.Label(ttk.Frame(ttk.Frame(self.root, padding=(10, 0, 10, 10)), padding=(0, 5, 0, 0)), textvariable=self.camera_info_str, font=STYLE_FONT_SMALL, padding=5, anchor=tk.E, foreground=THEME_FG_DIM)
        self.status_var = tk.StringVar(value='Ready.')
        self.status_label = ttk.Label(self.root, textvariable=self.status_var, relief=tk.FLAT, anchor=tk.W, padding=(10, 5), font=STYLE_FONT_BOLD, background=THEME_PANEL, foreground=THEME_FG)
        self.update_status('Ready.', 'default_revert')
        self._apply_styles()

    def _apply_styles(self):
        style = ttk.Style(self.root).theme_names()
        if 'clam' in style:
            style.theme_use('clam')
        style.configure('.', background=THEME_BG, foreground=THEME_FG, font=STYLE_FONT_DEFAULT)
        style.configure('TFrame', background=THEME_BG)
        style.configure('TLabel', background=THEME_BG, foreground=THEME_FG)
        style.configure('TLabelframe', background=THEME_BG, foreground=THEME_FG, bordercolor=THEME_PANEL)
        style.configure('TLabelframe.Label', background=THEME_BG, foreground=THEME_ACCENT, font=STYLE_FONT_BOLD)
        style.configure('TCheckbutton', background=THEME_BG, foreground=THEME_FG)
        style.map('TCheckbutton', background=[('active', THEME_BG)])
        style.configure('Accent.TButton', font=STYLE_FONT_BOLD, background=THEME_ACCENT, foreground='white', borderwidth=0, padding=6)
        style.map('Accent.TButton', background=[('active', THEME_ACCENT_HOVER), ('disabled', THEME_PANEL)], foreground=[('disabled', THEME_FG_DIM)])
        style.configure('Outline.TButton', font=STYLE_FONT_DEFAULT, background=THEME_PANEL, foreground=THEME_FG, borderwidth=0, padding=6)
        style.map('Outline.TButton', background=[('active', THEME_ENTRY), ('disabled', THEME_BG)], foreground=[('disabled', THEME_FG_DIM)])
        style.configure('TCombobox', fieldbackground=THEME_ENTRY, background=THEME_PANEL, foreground=THEME_FG, arrowcolor=THEME_FG, borderwidth=0)
        style.map('TCombobox', fieldbackground=[('readonly', THEME_ENTRY)], selectbackground=[('readonly', THEME_ACCENT)], selectforeground=[('readonly', 'white')])
        style.configure('TEntry', fieldbackground=THEME_ENTRY, foreground=THEME_FG, borderwidth=0, padding=4)

    def update_status(self, message, level = 'info'):
        sub_181020db0('status_var')
        bg_color = None.status_var
        if bg_color:
            None.status_var.set(message)
            sub_181020db0('status_label')
            if None.status_label:
                for bg_color in sub_180003b80((THEME_PANEL, THEME_FG)):
                    pass
                next(sub_180003b80((THEME_PANEL, THEME_FG)))
            else:
                sub_181020db0('root')
                _v6 = None.root.winfo_exists()
                if _v6:
                    None.root.update_idletasks()
            return None
        if level != 'default_revert':
            sub_181020db0('root')
            _v10 = None.root.winfo_exists()
            if _v10:
                _v12 = 4000
                _v13 = lambda f: getattr('update_status', ('', 'default_revert'))()
                _v13 = lambda f: getattr('update_status', ('', 'default_revert'))()
                None.root.after(_v12, _v13)
        return None

    def refresh_recorded_videos_list(self):
        sub_181020db0(self, 'recorded_videos_listbox')
        y4m_files = 0
        f_path = self.recorded_videos_listbox.delete(y4m_files, tk.END)
        _v2 = '*.y4m'
        _v4 = glob.glob(__import__('ntpath').join(self.recordings_folder_path, _v2, 0))
        _v6 = True
        if sorted(_v4, key=__import__('ntpath').getmtime, reverse=_v6):
            for y4m_files in sorted(_v4, key=__import__('ntpath').getmtime, reverse=_v6):
                self.recorded_videos_listbox.insert(tk.END, sub_18100ec30(' ', sub_181029d30(y4m_files)))
        else:
            self.recorded_videos_listbox.insert(tk.END, ' No Y4M videos found.', _v4, self.recordings_folder_path, _v2, sorted(_v4, key=__import__('ntpath').getmtime, reverse=_v6), __import__('ntpath').getmtime, _v6)
            self.recorded_videos_listbox.itemconfig(0, {'fg': 'grey'}, _v4, self.recordings_folder_path, _v2, sorted(_v4, key=__import__('ntpath').getmtime, reverse=_v6), __import__('ntpath').getmtime, _v6)

    def _get_ffmpeg_dshow_devices(self):
        command = sub_181029e10(FFMPEG_PATH)
        return si if command else command

    def update_camera_list(self):
        self.update_status('Scanning for cameras using FFmpeg...', 'info')
        available_cameras = self._get_ffmpeg_dshow_devices()
        if available_cameras:
            self.camera_combo['values'] = available_cameras
            self.camera_combo.current(0)
            self.on_camera_select()
            _v9 = f'Found {len(available_cameras)} cameras.'
            self.update_status(_v9, 'success')
        else:
            self.camera_combo['values'] = []
            self.camera_var.set('')
            self.update_status('No cameras found by FFmpeg.', 'error')

    def on_camera_select(self, event = None):
        selected_camera_str = self.camera_var.get()
        if selected_camera_str:
            try:
                camera_index = self.camera_combo['values']
            except ValueError:
                _v8 = f"Selected camera '{selected_camera_str}' not in list."
                self.update_status(_v8, 'error')
            _v2 = sub_181022e70(sub_181023a50(self.camera_combo['values']), selected_camera_str)
            if self.is_recording:
                pass
            else:
                self._start_preview(_v2, selected_camera_str)

    def _stop_preview(self):
        if self.video_preview_thread:
            self.video_preview_thread.is_alive()
        if self.video_preview_thread.is_alive():
            self.stop_event.set()
        if self.cap:
            self.cap.release()
            self.cap = None
        self.stop_event.clear()
        if self.video_label:
            pass

    def _start_preview(self, camera_index, camera_name):
        self._stop_preview()
        self.current_resolution = None
        self.cap = width
        height = self.cap.isOpened()
        if height:
            pass
        else:
            fps = cv2.VideoCapture(camera_index)
            self.cap = fps
        _v3 = self.cap.isOpened()
        if _v3:
            self.cap.get(cv2.CAP_PROP_FPS)
            self.current_resolution = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            _v18 = f'{ICON_CAMERA} {int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))} | {camera_name}'
            self.camera_info_str.set(_v18)
            self.video_preview_thread = threading.Thread(target=self._video_preview_loop, daemon=True)
            self.video_preview_thread.start()
        else:
            self.cap = None
            self.camera_info_str.set(f'Camera: {camera_name} (Preview Failed)')
            if self.video_label:
                pass

    def _video_preview_loop(self):
        target_interval = sub_181010fa0(1.0, TARGET_RECORDING_FPS)
        try:
            while True:
                ret = self.stop_event.is_set()
                if ret is not True:
                    if ret is False:
                        pass
                    elif ret is not None:
                        if ret:
                            pass
                        else:
                            break
                try:
                    if False is True:
                        pass
                    else:
                        if False is None:
                            pass
                        else:
                            if False:
                                pass
                            if _v116 is not True:
                                if _v116 is False:
                                    pass
                                elif _v116 is not None:
                                    if _v116:
                                        pass
                                    else:
                                        break
                            frame = time.perf_counter()
                            adjusted_frame = self.cap
                            for adjusted_frame in adjusted_frame.read():
                                if adjusted_frame:
                                    h_f = next(iter(adjusted_frame.read())).copy()
                                else:
                                    break
                                if self.guide_ovals_var.get() is not True:
                                    if self.guide_ovals_var.get() is False:
                                        pass
                                    elif self.guide_ovals_var.get() is not None:
                                        if self.guide_ovals_var.get():
                                            pass
                                        else:
                                            break
                                getattr(self, 'face_cascade', None)
                                w_f = cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml'
                                _ = cv2.CascadeClassifier(w_f)
                                self.face_cascade = _
                                oz_positions = getattr(self, 'current_oval_idx', 0)
                                self.current_oval_idx = oz_positions
                                cx_n = getattr(self, 'all_ovals_done', False)
                                self.all_ovals_done = cx_n
                                for rx_n in next(iter(adjusted_frame.read())).copy().shape:
                                    ry_n = self.all_ovals_done
                                    if ry_n:
                                        cx = 'ALL 4 POSITIONS DONE! (Uncheck/Check guides to reset)'
                                        cy = (40, 50)
                                        rx = 0.8
                                        ry = (0, 255, 0)
                                        gray = 2
                                        scale = cv2.putText(next(iter(adjusted_frame.read())).copy(), cx, cy, cv2.FONT_HERSHEY_SIMPLEX, rx, ry, gray, cv2.LINE_AA)
                                        faces = self.video_label.winfo_exists()
                                        if faces is not True:
                                            if faces is False:
                                                pass
                                            elif faces is not None:
                                                if faces:
                                                    pass
                                                else:
                                                    break
                                        face_in_oval = cv2.cvtColor(_v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                                        fx = Image.fromarray(face_in_oval)
                                        fw = self.video_label.winfo_width()
                                        face_cx = self.video_label.winfo_height()
                                        if fw > 1:
                                            if face_cx > 1:
                                                face_cy = fx.width / fx.height
                                                dx = fw / face_cy
                                                dy = int(dx)
                                                if dy > face_cx:
                                                    mask = face_cx * face_cy
                                                    white_overlay = int(mask)
                                                    continue
                                                continue
                                            continue
                                        continue
                                    for new_h in [(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]:
                                        _ndx_value_0 = sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1)
                                        sub_180003f80(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 4)
                                        _ndx_value_2 = int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h)
                                        (_ndx_value_2, int(rx_n * new_h))
                                        int(rx_n * new_h)
                                        for sleep_duration in sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1)))):
                                            sub_180003f80(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1)))), 2)
                                            _ndx_value_1 = int(new_h)
                                            next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h
                                            (next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h, int(rx_n * imgtk))
                                            _ndx_value_3 = int(rx_n * imgtk)
                                            rx_n * new_h
                                            for e in sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk))):
                                                sub_180003f80(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk))), 2)
                                                _ndx_value_0 = cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))
                                                _ndx_value_1 = cv2.equalizeHist(new_h)
                                                next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h
                                                _ndx_value_2 = next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0
                                                _ndx_value_3 = int(rx_n * imgtk)
                                                rx_n * new_h
                                                _ndx_value_4 = (rx_n * new_h, int(rx_n / 4.0))
                                                int(rx_n / 4.0)
                                                _ndx_value_7 = cv2.resize(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h, int(rx_n * new_h), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255)
                                                _ndx_value_8 = self.face_cascade.detectMultiScale(_ndx_value_7, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                                                len(_ndx_value_8)
                                                if len(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))) > 0:
                                                    for imgtk in max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda f: f[2] * f[3]):
                                                        sub_180003f80(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda f: f[2] * f[3])), 4)
                                                        _ndx_value_0 = imgtk * 4.0
                                                        _ndx_value_1 = int(new_h)
                                                        next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h
                                                        (next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h, int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval)
                                                        _ndx_value_2 = next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0
                                                        _ndx_value_3 = int(rx_n * imgtk)
                                                        rx_n * new_h
                                                        _ndx_value_4 = next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0
                                                        _ndx_value_5 = int(int(rx_n * new_h))
                                                        rx_n / 4.0
                                                        _ndx_value_6 = next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0
                                                        for target_interval in sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval)):
                                                            sub_180003f80(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval)), 4)
                                                            _ndx_value_0 = next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) // 2
                                                            _ndx_value_1 = target_interval + new_h
                                                            _ndx_value_2 = next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) // 2
                                                            _ndx_value_3 = next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) + rx_n * imgtk
                                                            _ndx_value_4 = next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h - sleep_duration
                                                            _ndx_value_5 = max(1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, _v117, cv2.COLOR_BGR2RGB)
                                                            _ndx_value_6 = int(rx_n * new_h) / rx_n / 4.0
                                                            _ndx_value_7 = rx_n * new_h - next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1)))))
                                                            _ndx_value_9 = int(int(rx_n / 4.0)) / max(1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, _v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                                                            int(rx_n / 4.0) * int(rx_n / 4.0) + _ndx_value_9 * _ndx_value_9
                                                            if target_interval + next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) // 2 - sleep_duration / max(1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, _v117, cv2.COLOR_BGR2RGB) * target_interval + next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) // 2 - sleep_duration / max(1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, _v117, cv2.COLOR_BGR2RGB) + next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) + next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) // 2 - next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1))))) / max(1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, _v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS) * next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) + next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) // 2 - next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1))))) / max(1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, _v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS) < 1.0:
                                                                if next(sub_180003b80((int(imgtk * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), int(next(iter(max(self.face_cascade.detectMultiScale(cv2.resize(cv2.equalizeHist(cv2.cvtColor(next(iter(adjusted_frame.read())).copy(), cv2.COLOR_BGR2GRAY, _v119, (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), (int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) / 4.0), int(rx_n / 4.0)), 1, e, 1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda *_args: None))) * 4.0), target_interval))) >= e * 0.5:
                                                                    continue
                                                else:
                                                    _ndx_value_0 = (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)))
                                                    _ndx_value_1 = np.zeros(new_h, dtype=np.uint8)
                                                    _ndx_value_2 = (sleep_duration, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1))))))
                                                    _ndx_value_3 = (e, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))
                                                    cv2.ellipse(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h, rx_n * imgtk, rx_n * new_h, 0, 0, 360, 255, -1)
                                                    _ndx_value_4 = (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3)
                                                    _ndx_value_5 = np.full(int(rx_n * new_h), 255, dtype=np.uint8)
                                                    _ndx_value_6 = cv2.addWeighted(next(iter(adjusted_frame.read())).copy(), 0.25, rx_n / 4.0, 0.75, 0, next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h, rx_n * imgtk, rx_n * new_h)
                                                    _ndx_value_7 = next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h[slice(None, None, None), slice(None, None, None), np.newaxis]
                                                    _ndx_value_8 = int(int(rx_n / 4.0)) == 255
                                                    _ndx_value_9 = np.where(max(1, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))), (rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, _v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS), next(iter(adjusted_frame.read())).copy(), int(rx_n / 4.0), 0, self._update_video_label, _v120, next(iter(adjusted_frame.read())).copy(), 0.25)
                                                    if _v71:
                                                        pass
                                                    _ndx_value_10 = (sleep_duration, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1))))))
                                                    _ndx_value_11 = (e, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))
                                                    cv2.ellipse(np.where(np.zeros((rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape))), dtype=np.uint8)[slice(None, None, None), slice(None, None, None), np.newaxis] == 255, next(iter(adjusted_frame.read())).copy(), cv2.addWeighted(next(iter(adjusted_frame.read())).copy(), 0.25, np.full((rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, dtype=np.uint8), 0.75, 0, np.zeros((rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape))), dtype=np.uint8), (sleep_duration, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1)))))), (e, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), 0, self._update_video_label, _v120, next(iter(adjusted_frame.read())).copy(), 0.25), int(rx_n / 4.0) * int(rx_n / 4.0), _ndx_value_9 * _ndx_value_9, 0, 0, 360, _v96, 3)
                                                    cv2.putText(np.where(np.zeros((rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape))), dtype=np.uint8)[slice(None, None, None), slice(None, None, None), np.newaxis] == 255, next(iter(adjusted_frame.read())).copy(), cv2.addWeighted(next(iter(adjusted_frame.read())).copy(), 0.25, np.full((rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape)), 3), 255, dtype=np.uint8), 0.75, 0, np.zeros((rx_n, next(iter(next(iter(adjusted_frame.read())).copy().shape))), dtype=np.uint8), (sleep_duration, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * new_h), int(rx_n * sub_1800040a0(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]), 1)))))), (e, next(sub_180003b80((int(next(iter(next(iter(adjusted_frame.read())).copy().shape)) * next(iter([(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]))), int(rx_n * imgtk)))))), 0, self._update_video_label, _v120, next(iter(adjusted_frame.read())).copy(), 0.25), _v121, (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, _v115, 2, cv2.LINE_AA)
                                                    faces = self.video_label.winfo_exists()
                                                    if faces is not True:
                                                        if faces is False:
                                                            pass
                                                        elif faces is not None:
                                                            if faces:
                                                                pass
                                                            else:
                                                                break
                                                    face_in_oval = cv2.cvtColor(_v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                                                    fx = Image.fromarray(face_in_oval)
                                                    fw = self.video_label.winfo_width()
                                                    face_cx = self.video_label.winfo_height()
                                                    if fw > 1:
                                                        if face_cx > 1:
                                                            face_cy = fx.width / fx.height
                                                            dx = fw / face_cy
                                                            dy = int(dx)
                                                            if dy > face_cx:
                                                                mask = face_cx * face_cy
                                                                white_overlay = int(mask)
                                                                continue
                                                            continue
                                                        continue
                                                    continue
                        if _v116 is not True:
                            if _v116 is False:
                                pass
                            elif _v116 is not None:
                                if _v116:
                                    pass
                                else:
                                    break
                        frame = time.perf_counter()
                        _ndx_value_0 = self.cap.read()
                        if adjusted_frame:
                            h_f = next(iter(adjusted_frame.read())).copy()
                        else:
                            break
                        _ = self.guide_ovals_var.get()
                        if _ is not True:
                            if _ is False:
                                pass
                            elif _ is not None:
                                if _:
                                    pass
                                else:
                                    break
                        getattr(self, 'face_cascade', None)
                        w_f = cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml'
                        _ = cv2.CascadeClassifier(w_f)
                        self.face_cascade = _
                        oz_positions = getattr(self, 'current_oval_idx', 0)
                        self.current_oval_idx = oz_positions
                        cx_n = getattr(self, 'all_ovals_done', False)
                        self.all_ovals_done = cx_n
                        cy_n = h_f.shape
                        ry_n = self.all_ovals_done
                        if ry_n:
                            cx = 'ALL 4 POSITIONS DONE! (Uncheck/Check guides to reset)'
                            cy = (40, 50)
                            rx = 0.8
                            ry = (0, 255, 0)
                            gray = 2
                            scale = cv2.putText(h_f, cx, cy, cv2.FONT_HERSHEY_SIMPLEX, rx, ry, gray, cv2.LINE_AA)
                            faces = self.video_label.winfo_exists()
                            if faces is not True:
                                if faces is False:
                                    pass
                                elif faces is not None:
                                    if faces:
                                        pass
                                    else:
                                        break
                            face_in_oval = cv2.cvtColor(_v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                            fx = Image.fromarray(face_in_oval)
                            fw = self.video_label.winfo_width()
                            face_cx = self.video_label.winfo_height()
                            if fw > 1:
                                if face_cx > 1:
                                    face_cy = fx.width / fx.height
                                    dx = fw / face_cy
                                    dy = int(dx)
                                    if dy > face_cx:
                                        mask = face_cx * face_cy
                                        white_overlay = int(mask)
                                        continue
                                    continue
                                continue
                            continue
                        _v10 = [(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]
                        sub_180003f80(iter(_v10), 4)
                        _ndx_value_0 = int(cy * next(iter(_v10)))
                        _ndx_value_1 = int(rx_n * sub_1800040a0(iter(_v10), 1))
                        _v16 = (new_h, cy * new_h)
                        sleep_duration = next(sub_180003b80(_v16))
                        sleep_duration = next(sub_180003b80(_v16))
                        _v20 = next(sub_180003b80(_v16))
                        _v20 = next(sub_180003b80(_v16))
                        sub_180003f80(sub_180003b80(_v16), 2)
                        _ndx_value_2 = int(cy * next(iter(_v10)))
                        _ndx_value_3 = int(rx_n * next(iter(_v10)))
                        _v23 = (rx_n * imgtk, rx_n * new_h)
                        e = next(sub_180003b80(_v23))
                        e = next(sub_180003b80(_v23))
                        _v27 = next(sub_180003b80(_v23))
                        _v27 = next(sub_180003b80(_v23))
                        sub_180003f80(sub_180003b80(_v23), 2)
                        _ndx_value_4 = cv2.cvtColor(h_f, cv2.COLOR_BGR2GRAY, _v119, (int(cy / 4.0), int(rx_n / 4.0)), 1, next(sub_180003b80(_v23)), 1, next(sub_180003b80(_v23)))
                        _ndx_value_5 = cv2.equalizeHist(int(rx_n * new_h))
                        _v30 = 4.0
                        _ndx_value_6 = int(cy / _v30)
                        _ndx_value_7 = int(rx_n / _v30)
                        _v33 = (int(rx_n / _v30), int(int(rx_n / _v30)))
                        _ndx_value_8 = cv2.resize(rx_n / _v30, _v33, 1, next(sub_180003b80(_v23)), 1, next(sub_180003b80(_v23)), (rx_n, cy, 3), 255)
                        _v36 = max(1, _v27, (rx_n, cy, 3), 255, _v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                        _ndx_value_9 = self.face_cascade.detectMultiScale(_v36, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                        if len(self.face_cascade.detectMultiScale(_v36, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))) > 0:
                            _ndx_value_0 = max(self.face_cascade.detectMultiScale(_v36, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), key=lambda f: f[2] * f[3])
                            sub_180003f80(iter(new_h), 4)
                            _ndx_value_1 = int(next(iter(new_h)) * _v30)
                            _v47 = (cy * new_h, int(next(iter(new_h)) * _v30), int(next(iter(new_h)) * _v30), int(next(iter(new_h)) * _v30))
                            _ndx_value_2 = int(next(iter(new_h)) * _v30)
                            _ndx_value_3 = int(next(iter(new_h)) * _v30)
                            _ndx_value_4 = int(next(iter(new_h)) * _v30)
                            int(rx_n * new_h)
                            next(sub_180003b80(_v47))
                            next(sub_180003b80(_v47))
                            _v55 = next(sub_180003b80(_v47))
                            _v55 = next(sub_180003b80(_v47))
                            next(sub_180003b80(_v47))
                            sub_180003f80(sub_180003b80(_v47), 4)
                            _v63 = next(sub_180003b80(_v47)) + next(sub_180003b80(_v47)) // 2 - sleep_duration / max(1, e, 1, next(sub_180003b80((int(cy * next(iter(_v10))), int(rx_n * imgtk)))), (rx_n, cy, 3), 255, _v117, cv2.COLOR_BGR2RGB)
                            _v66 = next(sub_180003b80(_v47)) + next(sub_180003b80(_v47)) // 2 - _v20 / max(1, _v27, (rx_n, cy, 3), 255, _v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                            if _v63 * _v63 + _v66 * _v66 < 1.0:
                                _v70 = e * 0.5
                                if _v55 >= _v70:
                                    continue
                                continue
                            continue
                        _v72 = (rx_n, cy)
                        _v73 = np.uint8
                        _v74 = np.zeros(_v72, dtype=_v73)
                        _v75 = (sleep_duration, _v20)
                        _v76 = (e, _v27)
                        cv2.ellipse(_v74, _v75, _v76, 0, 0, 360, 255, -1)
                        _v78 = (rx_n, cy, 3)
                        _v79 = np.uint8
                        _v80 = 255
                        np.full(_v78, _v80, dtype=_v79)
                        cv2.addWeighted(h_f, 0.25, np.full(_v78, _v80, dtype=_v79), 0.75, 0, _v74, _v75, _v76)
                        _v85 = np.newaxis
                        _v83 = (slice(None, None, None), slice(None, None, None), _v85)
                        _v86 = _v74[slice(None, None, None), slice(None, None, None), _v85]
                        _v87 = _v74[slice(None, None, None), slice(None, None, None), _v85] == 255
                        _v88 = np.where(_v74[slice(None, None, None), slice(None, None, None), _v85] == 255, h_f, cv2.addWeighted(h_f, 0.25, np.full(_v78, _v80, dtype=_v79), 0.75, 0, _v74, _v75, _v76), 0, self._update_video_label, _v120, h_f, 0.25)
                        if True:
                            pass
                        _v107 = 0
                        _v109 = cv2.ellipse(_v88, (sleep_duration, _v20), (e, _v27), _v107, _v107, 360, _v96, 3)
                        cv2.putText(_v88, _v121, (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, _v115, 2, cv2.LINE_AA)
                        faces = self.video_label.winfo_exists()
                        if faces is not True:
                            if faces is False:
                                pass
                            elif faces is not None:
                                if faces:
                                    pass
                                else:
                                    break
                        face_in_oval = cv2.cvtColor(_v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                        fx = Image.fromarray(face_in_oval)
                        fw = self.video_label.winfo_width()
                        face_cx = self.video_label.winfo_height()
                        if fw > 1:
                            if face_cx > 1:
                                face_cy = fx.width / fx.height
                                dx = fw / face_cy
                                dy = int(dx)
                                if dy > face_cx:
                                    mask = face_cx * face_cy
                                    white_overlay = int(mask)
                                    continue
                                continue
                            continue
                        continue
                    if self.cap:
                        self.cap.isOpened()
                    if _v116 is not True:
                        if _v116 is False:
                            pass
                        elif _v116 is not None:
                            if _v116:
                                pass
                            else:
                                break
                    frame = time.perf_counter()
                    _ndx_value_0 = self.cap.read()
                    if adjusted_frame:
                        h_f = next(iter(adjusted_frame.read())).copy()
                    else:
                        break
                    _ = self.guide_ovals_var.get()
                    if _ is not True:
                        if _ is False:
                            pass
                        elif _ is not None:
                            if _:
                                pass
                            else:
                                break
                    getattr(self, 'face_cascade', None)
                    w_f = cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml'
                    _ = cv2.CascadeClassifier(w_f)
                    self.face_cascade = _
                    oz_positions = getattr(self, 'current_oval_idx', 0)
                    self.current_oval_idx = oz_positions
                    cx_n = getattr(self, 'all_ovals_done', False)
                    self.all_ovals_done = cx_n
                    cy_n = h_f.shape
                    ry_n = self.all_ovals_done
                    if ry_n:
                        cx = 'ALL 4 POSITIONS DONE! (Uncheck/Check guides to reset)'
                        cy = (40, 50)
                        rx = 0.8
                        ry = (0, 255, 0)
                        gray = 2
                        scale = cv2.putText(h_f, cx, cy, cv2.FONT_HERSHEY_SIMPLEX, rx, ry, gray, cv2.LINE_AA)
                        faces = self.video_label.winfo_exists()
                        if faces is not True:
                            if faces is False:
                                pass
                            elif faces is not None:
                                if faces:
                                    pass
                                else:
                                    break
                        face_in_oval = cv2.cvtColor(_v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                        fx = Image.fromarray(face_in_oval)
                        fw = self.video_label.winfo_width()
                        face_cx = self.video_label.winfo_height()
                        if fw > 1:
                            if face_cx > 1:
                                face_cy = fx.width / fx.height
                                dx = fw / face_cy
                                dy = int(dx)
                                if dy > face_cx:
                                    mask = face_cx * face_cy
                                    white_overlay = int(mask)
                                    continue
                                continue
                            continue
                        continue
                    _v10 = [(0.416, 0.422, 0.1522, 0.4271), (0.584, 0.422, 0.1522, 0.4271), (0.584, 0.578, 0.1522, 0.4271), (0.416, 0.578, 0.1522, 0.4271)][self.current_oval_idx]
                    sub_1800040a0(iter(_v10), 1)
                    sub_180003f80(iter(_v10), 4)
                    _v14 = cy * next(iter(_v10))
                    _ndx_value_0 = int(cy * next(iter(_v10)))
                    _v17 = rx_n * sub_1800040a0(iter(_v10), 1)
                    _ndx_value_1 = int(rx_n * sub_1800040a0(iter(_v10), 1))
                    _v16 = (new_h, cy * next(iter(_v10)))
                    sleep_duration = next(sub_180003b80(_v16))
                    sleep_duration = next(sub_180003b80(_v16))
                    _v20 = next(sub_180003b80(_v16))
                    _v20 = next(sub_180003b80(_v16))
                    sub_180003f80(sub_180003b80(_v16), 2)
                    _v21 = cy * next(iter(_v10))
                    _ndx_value_2 = int(cy * next(iter(_v10)))
                    _v22 = rx_n * imgtk
                    _v24 = rx_n * next(iter(_v10))
                    _ndx_value_3 = int(rx_n * next(iter(_v10)))
                    _v23 = (rx_n * next(iter(_v10)), rx_n * new_h)
                    e = next(sub_180003b80(_v23))
                    e = next(sub_180003b80(_v23))
                    _v27 = next(sub_180003b80(_v23))
                    _v27 = next(sub_180003b80(_v23))
                    sub_180003f80(sub_180003b80(_v23), 2)
                    _ndx_value_4 = cv2.cvtColor(h_f, cv2.COLOR_BGR2GRAY, _v119, (int(cy / 4.0), int(rx_n / 4.0)), 1, next(sub_180003b80(_v23)), 1, next(sub_180003b80(_v23)))
                    int(rx_n * new_h)
                    _ndx_value_5 = cv2.equalizeHist(int(rx_n * new_h))
                    _v29 = rx_n / 4.0
                    _v30 = 4.0
                    _v31 = cy / _v30
                    _ndx_value_6 = int(_v31)
                    int(rx_n / _v30)
                    _v34 = rx_n / _v30
                    _ndx_value_7 = int(_v34)
                    _v33 = (int(_v34), int(int(_v34)))
                    _ndx_value_8 = cv2.resize(_v34, _v33, 1, next(sub_180003b80(_v23)), 1, next(sub_180003b80(_v23)), (rx_n, cy, 3), 255)
                    _v36 = max(1, _v27, (rx_n, cy, 3), 255, _v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                    _ndx_value_9 = self.face_cascade.detectMultiScale(_v36, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                    if len(_ndx_value_9) > 0:
                        _ndx_value_0 = max(_ndx_value_9, key=lambda f: f[2] * f[3])
                        sub_180003f80(iter(new_h), 4)
                        _v45 = next(iter(new_h)) * _v30
                        _ndx_value_1 = int(next(iter(new_h)) * _v30)
                        _v46 = cy * next(iter(_v10))
                        _v47 = (cy * next(iter(_v10)), int(next(iter(new_h)) * _v30), int(next(iter(new_h)) * _v30), int(next(iter(new_h)) * _v30))
                        _v48 = next(iter(new_h)) * _v30
                        _ndx_value_2 = int(next(iter(new_h)) * _v30)
                        _v50 = next(iter(new_h)) * _v30
                        _ndx_value_3 = int(next(iter(new_h)) * _v30)
                        _v52 = next(iter(new_h)) * _v30
                        _ndx_value_4 = int(next(iter(new_h)) * _v30)
                        int(rx_n * new_h)
                        next(sub_180003b80(_v47))
                        next(sub_180003b80(_v47))
                        _v55 = next(sub_180003b80(_v47))
                        _v55 = next(sub_180003b80(_v47))
                        next(sub_180003b80(_v47))
                        sub_180003f80(sub_180003b80(_v47), 4)
                        _v57 = next(sub_180003b80(_v47)) // 2
                        _v58 = next(sub_180003b80(_v47)) + next(sub_180003b80(_v47)) // 2
                        _v59 = next(sub_180003b80(_v47)) // 2
                        _v60 = next(sub_180003b80(_v47)) + next(sub_180003b80(_v47)) // 2
                        _v61 = next(sub_180003b80(_v47)) + next(sub_180003b80(_v47)) // 2 - sleep_duration
                        _v62 = max(1, e, 1, next(sub_180003b80((rx_n * next(iter(_v10)), int(rx_n * next(iter(_v10)))))), (rx_n, cy, 3), 255, _v117, cv2.COLOR_BGR2RGB)
                        _v63 = next(sub_180003b80(_v47)) + next(sub_180003b80(_v47)) // 2 - sleep_duration / _v62
                        _v64 = next(sub_180003b80(_v47)) + next(sub_180003b80(_v47)) // 2 - _v20
                        _v65 = max(1, _v27, (rx_n, cy, 3), 255, _v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                        _v66 = next(sub_180003b80(_v47)) + next(sub_180003b80(_v47)) // 2 - _v20 / _v65
                        _v67 = _v63 * _v63
                        _v68 = _v66 * _v66
                        if _v63 * _v63 + _v66 * _v66 < 1.0:
                            _v70 = e * 0.5
                            if _v55 >= _v70:
                                continue
                            continue
                        continue
                    _v72 = (rx_n, cy)
                    _v73 = np.uint8
                    _v74 = np.zeros(_v72, dtype=_v73)
                    _v75 = (sleep_duration, _v20)
                    _v76 = (e, _v27)
                    cv2.ellipse(_v74, _v75, _v76, 0, 0, 360, 255, -1)
                    _v78 = (rx_n, cy, 3)
                    _v79 = np.uint8
                    _v80 = 255
                    np.full(_v78, _v80, dtype=_v79)
                    cv2.addWeighted(h_f, 0.25, np.full(_v78, _v80, dtype=_v79), 0.75, 0, _v74, _v75, _v76)
                    _v85 = np.newaxis
                    _v83 = (slice(None, None, None), slice(None, None, None), _v85)
                    _v86 = _v74[slice(None, None, None), slice(None, None, None), _v85]
                    _v87 = _v74[slice(None, None, None), slice(None, None, None), _v85] == 255
                    _v88 = np.where(_v74[slice(None, None, None), slice(None, None, None), _v85] == 255, h_f, cv2.addWeighted(h_f, 0.25, np.full(_v78, _v80, dtype=_v79), 0.75, 0, _v74, _v75, _v76), 0, self._update_video_label, _v120, h_f, 0.25)
                    if True:
                        pass
                    _v107 = 0
                    _v109 = cv2.ellipse(_v88, (sleep_duration, _v20), (e, _v27), _v107, _v107, 360, _v96, 3)
                    cv2.putText(_v88, _v121, (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, _v115, 2, cv2.LINE_AA)
                    faces = self.video_label.winfo_exists()
                    if faces is not True:
                        if faces is False:
                            pass
                        elif faces is not None:
                            if faces:
                                pass
                            else:
                                break
                    face_in_oval = cv2.cvtColor(_v117, cv2.COLOR_BGR2RGB, (_v109, _v118), Image.LANCZOS)
                    fx = Image.fromarray(face_in_oval)
                    fw = self.video_label.winfo_width()
                    face_cx = self.video_label.winfo_height()
                    if fw > 1:
                        if face_cx > 1:
                            face_cy = fx.width / fx.height
                            dx = fw / face_cy
                            dy = int(dx)
                            if dy > face_cx:
                                mask = face_cx * face_cy
                                white_overlay = int(mask)
                                continue
                            continue
                        continue
                    continue
                except StopIteration:
                    pass
        except StopIteration:
            pass

    def _update_video_label(self, imgtk):
        _v2 = self.video_label.winfo_exists()
        if _v2:
            self.video_label.image = imgtk

    def start_recording(self):
        device_name = self.camera_var.get()
        if device_name:
            duration_seconds = self.is_recording
            if duration_seconds:
                ts = messagebox.showwarning
                y4m_filename = self.root
            else:
                ffmpeg_cmd = sub_181029e10(FFMPEG_PATH)
                if ffmpeg_cmd:
                    self.is_recording = True
                    width = tk.DISABLED
                    height = self.start_button.config(state=width)
                    si = tk.NORMAL
                    cf = self.stop_button.config(state=si)
                    e = self.camera_combo.config(state='readonly')
                    self.update_status('Stopping preview to begin recording...', 'info')
                    self._stop_preview()
                    time.sleep(0.5)
                    _v3 = datetime.now().strftime('%Y%m%d_%H%M%S')
                    _v8 = f'{device_name}_{_v3}.y4m'
                    self.output_y4m_path = _v9
                    if self.current_resolution:
                        for device_name in self.current_resolution:
                            return None
                        return None
                    _v16 = '-i'
                    _v19 = f'video={device_name}'
                    sub_181022c00([FFMPEG_PATH, '-y', '-f', 'dshow'], [_v16, _v19, '-c:v', 'rawvideo', '-pix_fmt', 'yuv420p', '-f', 'yuv4mpegpipe', '-t', str(self.duration_var.get()), '-loglevel', 'error'])
                    [FFMPEG_PATH, '-y', '-f', 'dshow'].append(self.output_y4m_path)
                    _v21 = subprocess.STARTUPINFO()
                    via_PyErr_Format(subprocess.STARTF_USESHOWWINDOW)
                    _v21.dwFlags = _v21.dwFlags
                    _v21.wShowWindow = subprocess.SW_HIDE
                    try:
                        self.ffmpeg_process = subprocess.Popen([FFMPEG_PATH, '-y', '-f', 'dshow'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding='utf-8')
                        _v32 = f'Recording started: {_v8}'
                        threading.Thread(target=self._monitor_ffmpeg, daemon=True).start()
                    except Exception:
                        pass
                return None
        CALL_VECTOR_WITH_KEYWORDS(_v41, _v52)
        return None

    def _monitor_ffmpeg(self):
        if self.ffmpeg_process:
            self.ffmpeg_process.wait()
            if self.is_recording:
                self.root.after(0, self.stop_recording)

    def stop_recording(self, is_error = False):
        was_actively_recording = self.is_recording
        self.is_recording = False
        try:
            current_y4m_file_path = self.ffmpeg_process
        except Exception:
            self.ffmpeg_process.kill()
        if self.ffmpeg_process:
            self.ffmpeg_process.poll()
        sub_181020db0(self, 'start_button')
        _v4 = self.start_button.winfo_exists()
        if _v4:
            pass
        sub_181020db0(self, 'stop_button')
        _v8 = self.stop_button.winfo_exists()
        if _v8:
            pass
        sub_181020db0(self, 'camera_combo')
        _v12 = self.camera_combo.winfo_exists()
        if _v12:
            pass
        _v14 = getattr(self, 'output_y4m_path', None)
        self.output_y4m_path = None
        if is_error:
            self.update_status()
            _v16 = self.root.winfo_exists()
            if _v16:
                self.root.after(100, self.refresh_recorded_videos_list)
                self.root.after(200, self.on_camera_select)
        else:
            if _v14:
                _v21 = sub_181029e10(_v14)
                if _v21:
                    pass
            if was_actively_recording:
                self.update_status()
            _v16 = self.root.winfo_exists()
            if _v16:
                self.root.after(100, self.refresh_recorded_videos_list)
                self.root.after(200, self.on_camera_select)

    def convert_external_video_to_y4m(self):
        pass

    def _perform_ffmpeg_conversion(self, source_path, output_path):
        cmd = 'Converting '
        si = sub_181029d30(source_path)
        cf = (cmd, format(si, ''), '...')
        process = f'Converting {si}...'
        e = 'info'
        self.update_status(f'Converting {si}...', e)
        via_PyErr_Format(subprocess.STARTF_USESHOWWINDOW)
        subprocess.STARTUPINFO().dwFlags = subprocess.STARTUPINFO().dwFlags
        str(TARGET_RECORDING_FPS)

    def open_recordings_folder(self):
        __import__('os').startfile(self.recordings_folder_path)

    def merge_videos(self):
        indices = sub_181029e10(FFMPEG_PATH)
        paths = ('Merge Videos', 'Please select at least two videos.') if indices else ('FFmpeg Error', 'FFmpeg not found.')
        merged_filename = CALL_VECTOR_WITH_KEYWORDS(messagebox.showwarning if indices else messagebox.showerror, ('Merge Videos', 'Please select at least two videos.') if indices else ('FFmpeg Error', 'FFmpeg not found.'))

    def on_closing(self):
        self.stop_event.set()
        if self.is_recording:
            self.stop_recording()
        if self.video_preview_thread:
            self.video_preview_thread.is_alive()
        if self.video_preview_thread.is_alive():
            pass
        if self.cap:
            self.cap.release()
        if self.ffmpeg_process:
            self.ffmpeg_process.kill()
        _v15 = self.root.winfo_exists()
        if _v15:
            self.root.destroy()

def show_admin_required_message_interactive():
    root_temp = tk.Tk()
    root_temp.withdraw()
    result = 'Administrator Privileges Recommended'
    _v1 = 'This application may require administrator privileges for some operations.\n\nRestart with administrator privileges now?'
    root_temp.destroy()
    return messagebox.askokcancel(title=result, message=_v1, icon=messagebox.WARNING, parent=None)

# Entry boundary inferred: the native code no longer proves the original __name__ guard.
if __name__ == "__main__":
    try:
        _v81 = ttk.Style(root)
        style.theme_use('clam')
        Y4MVideoRecorderApp(root)
        root.mainloop()
        _v78 = is_admin()
        if _v78:
            pass
        else:
            _v79 = show_admin_required_message_interactive()
            if _v79:
                _v80 = elevate()
                if _v80:
                    raise SystemExit(0)
        _v79 = show_admin_required_message_interactive()
        if _v79:
            _v80 = elevate()
            if _v80:
                raise SystemExit(0)
        _v80 = elevate()
        if _v80:
            raise SystemExit(0)
        else:
            tk.Tk()
            _v81 = ttk.Style(root)
            style.theme_use('clam')
            Y4MVideoRecorderApp(root)
            root.mainloop()
    except Exception:
        pass
    e_theme = 'e_theme'
    print(f'Theme application error: {e_theme}')