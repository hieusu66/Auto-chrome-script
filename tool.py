import subprocess
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time, json, threading, logging, sched, os, shutil, pyperclip, pickle, random
from datetime import datetime
from sympy import sympify
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import cv2
import pyautogui
import numpy as np
from PIL import Image, ImageGrab

# ================== NGÔN NGỮ ==================
class Language:
    VIETNAMESE = {
        "app_title": "🔧 Auto Chrome Script GUI",
        "tab_script": "📝 Quản lý Script",
        "tab_settings": "⚙️ Thêm bước & Cài đặt",
        "tab_arrange": "🪟 Sắp xếp cửa sổ",
        "saved_scripts": "📜 Script đã lưu:",
        "current_steps": "📝 Các bước Script:",
        "refresh": "🔄 Tải lại",
        "view_profiles": "📂 Xem Profiles",
        "delete_profiles": "🗑️ Xóa Profiles",
        "install_chromedriver": "⚙️ Cài Chromedriver",
        "update_app": "🔄 Cập nhật app",
        "guide": "❓ Hướng dẫn",
        "edit_step": "✏️ Chỉnh sửa",
        "delete_step": "🗑️ Xóa bước",
        "save_script": "💾 Lưu Script",
        "add_new_step": "➕ Thêm bước mới",
        "action": "Hành động:",
        "value": "Giá trị:",
        "add_step": "➕ Thêm bước",
        "add_field": "➕ Thêm trường",
        "load_accounts": "📄 Tải tài khoản",
        "run_settings": "⚡ Cài đặt chạy",
        "threads": "Số luồng:",
        "chrome_size": "Kích thước Chrome:",
        "hide_chrome": "Ẩn Chrome (headless)",
        "auto_close_chrome": "Tự đóng Chrome khi xong",
        "auto_create_profiles": "Tạo profile tự động",
        "delete_profiles_after": "Xóa profile sau khi chạy",
        "schedule_run": "Hẹn giờ chạy:",
        "hour": "Giờ:",
        "minute": "Phút:",
        "schedule_button": "🕑 Hẹn giờ",
        "run_script": "▶️ CHẠY SCRIPT",
        "ready": "Sẵn sàng...",
        "language_label": "🌐 Ngôn ngữ:",
        "language_option_vn": "Tiếng Việt",
        "language_option_en": "English",
        "auto_load_accounts": "📥 Tự động tải account.txt",
        "show_steps_window": "📋 Hiện cửa sổ bước",
        "steps_window_title": "📋 Các bước Script",
        "step": "Bước",
        "action_col": "Hành động",
        "value_col": "Giá trị",
        "close": "Đóng",
        "no_accounts": "Chưa có tài khoản",
        "select_field": "Chọn trường",
        "accounts_loaded": "Tài khoản đã tải",
        "loading_accounts": "Đang tải tài khoản...",
        "accounts_file_not_found": "Không tìm thấy file account.txt",
        "load_success": "Tải thành công",
        "load_failed": "Tải thất bại",
        "select_template": "Chọn template hình ảnh:",
        "refresh_templates": "🔄 Làm mới",
        "action_label": "Hành động:",
        "offset_x": "Offset X:",
        "offset_y": "Offset Y:",
        "confidence": "Độ chính xác (0.1-1.0):",
        "text_for_type": "Văn bản (cho type):",
        "save_action": "Lưu hành động",
        "custom_code_title": "Thêm mã Python tùy chỉnh",
        "enter_code": "Nhập đoạn mã Python cần thực thi:",
        "save_code_action": "Lưu hành động",
        "guide_title": "Hướng dẫn sử dụng",
        "profiles_title": "Danh sách Chrome Profiles",
        "profiles_list": "Các profile hiện có:",
        "close_button": "Đóng",
        "confirm_delete": "Xác nhận xóa",
        "delete_all_profiles": "Bạn có chắc chắn muốn xóa tất cả profiles?",
        "yes": "Có",
        "no": "Không",
        "success": "Thành công",
        "error": "Lỗi",
        "warning": "Cảnh báo",
        "info": "Thông tin",
        "profiles_deleted": "Đã xóa tất cả profile Chrome",
        "no_profiles": "Không có profile nào để xóa",
        "delete_failed": "Không thể xóa profiles",
        "fields": "Các trường",
        "select_profile_to_run": "Chọn profile để chạy",
        "manage_random_xpaths": "Quản lý XPath Random",
        "random_xpath_popup_title": "Quản lý XPath Random",
        "random_xpath_list": "Danh sách XPath Random",
        "add_xpath": "➕ Thêm XPath",
        "delete_xpath": "🗑️ Xóa XPath",
        "click_random_xpath": "Click Random XPath",
        "click_random_xpath_1": "Click Random 1 XPath",
        "click_random_xpath_2": "Click Random 2 XPath",
        "click_random_xpath_3": "Click Random 3 XPath",
        "click_random_xpath_5": "Click Random 5 XPath",
        "click_random_xpath_10": "Click Random 10 XPath",
        "click_random_xpath_custom": "Click Random XPath (tùy chỉnh)",
        "xpath_added": "Đã thêm XPath",
        "xpath_deleted": "Đã xóa XPath",
        "no_xpath_selected": "Vui lòng chọn XPath để xóa",
        "confirm_delete_xpath": "Bạn có chắc chắn muốn xóa XPath này?",
        "random_xpaths_empty": "Danh sách XPath random trống",
        "add_xpath_first": "Vui lòng thêm XPath trước",
        "add_random_xpath_to_script": "Thêm XPath vào danh sách Random",
        "enter_xpath_to_add": "Nhập XPath để thêm vào danh sách Random:",
        "random_count_label": "Số lượng XPath random:",
        "random_count_custom": "Tùy chỉnh...",
        "enter_random_count": "Nhập số lượng XPath random (1-100):",
        "manage_xpath_groups": "XPath Random",
        "save_xpath_groups": "💾 Lưu nhóm XPath",
        "load_xpath_groups": "📂 Tải nhóm XPath",
        "clear_all_groups": "🗑️ Xóa tất cả nhóm",
        "xpath_group_1": "Nhóm 1 (cho Random 1 XPath)",
        "xpath_group_2": "Nhóm 2 (cho Random 2 XPath)",
        "xpath_group_3": "Nhóm 3 (cho Random 3 XPath)",
        "xpath_group_5": "Nhóm 5 (cho Random 5 XPath)",
        "xpath_group_10": "Nhóm 10 (cho Random 10 XPath)",
        "xpath_group_custom": "Nhóm Custom (tùy chỉnh)",
        "xpath_groups_saved": "Đã lưu nhóm XPath",
        "xpath_groups_loaded": "Đã tải nhóm XPath",
        "xpath_groups_cleared": "Đã xóa tất cả nhóm XPath",
        "arrange_windows": "📐 Sắp xếp cửa sổ",
        "arrange_windows_title": "Sắp xếp cửa sổ Chrome",
        "arrange_settings_title": "Cài đặt sắp xếp cửa sổ",
        "arrange_columns": "Số cột:",
        "arrange_rows": "Số hàng:",
        "arrange_gap": "Khoảng cách:",
        "arrange_button": "Sắp xếp ngay",
        "arrange_success": "Đã sắp xếp cửa sổ",
        "arrange_auto": "Tự động sắp xếp khi chạy script",
        "arrange_auto_desc": "Tự động sắp xếp các cửa sổ Chrome khi bắt đầu chạy script",
        "arrange_notes": "Lưu ý: Chỉ sắp xếp được các cửa sổ Chrome đang mở\nbởi tool này (chạy ở chế độ không headless)",
        "dashboard": "📊 Dashboard",
        "quick_actions": "⚡ Thao tác nhanh",
        "running_threads": "Luồng đang chạy",
        "total_steps": "Tổng số bước",
        "profiles_count": "Số profiles",
        "accounts_count": "Số tài khoản",
        "system_status": "📈 Trạng thái hệ thống",
        "dark_mode": "🌙 Chế độ tối",
        "light_mode": "☀️ Chế độ sáng",
        "run_script_quick": "▶️ Chạy Script Nhanh"
    }
    
    ENGLISH = {
        "app_title": "🔧 Auto Chrome Script GUI (English)",
        "tab_script": "📝 Script Management",
        "tab_settings": "⚙️ Add Steps & Settings",
        "tab_arrange": "🪟 Arrange Windows",
        "saved_scripts": "📜 Saved Scripts:",
        "current_steps": "📝 Current Script Steps:",
        "refresh": "🔄 Reload",
        "view_profiles": "📂 View Profiles",
        "delete_profiles": "🗑️ Delete Profiles",
        "install_chromedriver": "⚙️ Install Chromedriver",
        "update_app": "🔄 Update App",
        "guide": "❓ Guide",
        "edit_step": "✏️ Edit",
        "delete_step": "🗑️ Delete Step",
        "save_script": "💾 Save Script",
        "add_new_step": "➕ Add New Step",
        "action": "Action:",
        "value": "Value:",
        "add_step": "➕ Add Step",
        "add_field": "➕ Add Field",
        "load_accounts": "📄 Load Accounts",
        "run_settings": "⚡ Run Settings",
        "threads": "Threads:",
        "chrome_size": "Chrome Size:",
        "hide_chrome": "Hide Chrome (headless)",
        "auto_close_chrome": "Auto Close Chrome when done",
        "auto_create_profiles": "Auto create profiles",
        "delete_profiles_after": "Delete profiles after run",
        "schedule_run": "Schedule run:",
        "hour": "Hour:",
        "minute": "Minute:",
        "schedule_button": "🕑 Schedule",
        "run_script": "▶️ RUN SCRIPT",
        "ready": "Ready...",
        "language_label": "🌐 Language:",
        "language_option_vn": "Vietnamese",
        "language_option_en": "English",
        "auto_load_accounts": "📥 Auto load account.txt",
        "show_steps_window": "📋 Show Steps Window",
        "steps_window_title": "📋 Script Steps",
        "step": "Step",
        "action_col": "Action",
        "value_col": "Value",
        "close": "Close",
        "no_accounts": "No accounts",
        "select_field": "Select field",
        "accounts_loaded": "Accounts loaded",
        "loading_accounts": "Loading accounts...",
        "accounts_file_not_found": "account.txt file not found",
        "load_success": "Load successful",
        "load_failed": "Load failed",
        "select_template": "Select image template:",
        "refresh_templates": "🔄 Refresh",
        "action_label": "Action:",
        "offset_x": "Offset X:",
        "offset_y": "Offset Y:",
        "confidence": "Confidence (0.1-1.0):",
        "text_for_type": "Text (for type):",
        "save_action": "Save Action",
        "custom_code_title": "Add Custom Python Code",
        "enter_code": "Enter Python code to execute:",
        "save_code_action": "Save Action",
        "guide_title": "User Guide",
        "profiles_title": "Chrome Profiles List",
        "profiles_list": "Available profiles:",
        "close_button": "Close",
        "confirm_delete": "Confirm Delete",
        "delete_all_profiles": "Are you sure you want to delete all profiles?",
        "yes": "Yes",
        "no": "No",
        "success": "Success",
        "error": "Error",
        "warning": "Warning",
        "info": "Info",
        "profiles_deleted": "All Chrome profiles deleted",
        "no_profiles": "No profiles to delete",
        "delete_failed": "Failed to delete profiles",
        "fields": "Fields",
        "select_profile_to_run": "Select profile to run",
        "manage_random_xpaths": "Manage Random XPaths",
        "random_xpath_popup_title": "Manage Random XPaths",
        "random_xpath_list": "Random XPath List",
        "add_xpath": "➕ Add XPath",
        "delete_xpath": "🗑️ Delete XPath",
        "click_random_xpath": "Click Random XPath",
        "click_random_xpath_1": "Click Random 1 XPath",
        "click_random_xpath_2": "Click Random 2 XPath",
        "click_random_xpath_3": "Click Random 3 XPath",
        "click_random_xpath_5": "Click Random 5 XPath",
        "click_random_xpath_10": "Click Random 10 XPath",
        "click_random_xpath_custom": "Click Random XPath (custom)",
        "xpath_added": "XPath added",
        "xpath_deleted": "XPath deleted",
        "no_xpath_selected": "Please select XPath to delete",
        "confirm_delete_xpath": "Are you sure you want to delete this XPath?",
        "random_xpaths_empty": "Random XPath list is empty",
        "add_xpath_first": "Please add XPath first",
        "add_random_xpath_to_script": "Add XPath to Random List",
        "enter_xpath_to_add": "Enter XPath to add to Random List:",
        "random_count_label": "Random XPath count:",
        "random_count_custom": "Custom...",
        "enter_random_count": "Enter random XPath count (1-100):",
        "manage_xpath_groups": "Manage Random XPath Groups",
        "save_xpath_groups": "💾 Save XPath Groups",
        "load_xpath_groups": "📂 Load XPath Groups",
        "clear_all_groups": "🗑️ Clear All Groups",
        "xpath_group_1": "Group 1 (for Random 1 XPath)",
        "xpath_group_2": "Group 2 (for Random 2 XPath)",
        "xpath_group_3": "Group 3 (for Random 3 XPath)",
        "xpath_group_5": "Group 5 (for Random 5 XPath)",
        "xpath_group_10": "Group 10 (for Random 10 XPath)",
        "xpath_group_custom": "Group Custom (custom)",
        "xpath_groups_saved": "XPath groups saved",
        "xpath_groups_loaded": "XPath groups loaded",
        "xpath_groups_cleared": "All XPath groups cleared",
        "arrange_windows": "📐 Arrange Windows",
        "arrange_windows_title": "Arrange Chrome Windows",
        "arrange_settings_title": "Window Arrangement Settings",
        "arrange_columns": "Columns:",
        "arrange_rows": "Rows:",
        "arrange_gap": "Gap:",
        "arrange_button": "Arrange Now",
        "arrange_success": "Windows arranged",
        "arrange_auto": "Auto arrange when running script",
        "arrange_auto_desc": "Automatically arrange Chrome windows when starting script",
        "arrange_notes": "Note: Only arranges Chrome windows opened\nby this tool (running in non-headless mode)",
        "dashboard": "📊 Dashboard",
        "quick_actions": "⚡ Quick Actions",
        "running_threads": "Running Threads",
        "total_steps": "Total Steps",
        "profiles_count": "Profiles Count",
        "accounts_count": "Accounts Count",
        "system_status": "📈 System Status",
        "dark_mode": "🌙 Dark Mode",
        "light_mode": "☀️ Light Mode",
        "run_script_quick": "▶️ Run Script Quick"
    }

# ================== BIẾN TOÀN CỤC ==================
current_language = Language.VIETNAMESE
current_theme = "darkly"
script_steps = []
accounts = []
active_drivers = []
random_xpath_groups = {
    "group_1": [],  "group_2": [],  "group_3": [],
    "group_5": [],  "group_10": [], "group_custom": []
}

# Đường dẫn
CHROMEDRIVER_PATH = "chromedriver.exe"
PROFILES_DIR = os.path.join(os.path.dirname(__file__), "profiles")
IMAGE_TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "image_templates")
SETTINGS_FILE = "settings.txt"

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(IMAGE_TEMPLATES_DIR):
    os.makedirs(IMAGE_TEMPLATES_DIR)

# ================== HÀM CẬP NHẬT UI NGÔN NGỮ ==================
def update_ui_language():
    try:
        if 'root' in globals():
            root.title(current_language["app_title"])
        if 'notebook' in globals():
            notebook.tab(0, text=current_language["dashboard"])
            notebook.tab(1, text=current_language["tab_script"])
            notebook.tab(2, text=current_language["tab_settings"])
            notebook.tab(3, text=current_language["tab_arrange"])
        
        if 'dashboard_title' in globals():
            dashboard_title.config(text=current_language["dashboard"])
        if 'quick_actions_label' in globals():
            quick_actions_label.config(text=current_language["quick_actions"])
        if 'system_status_label' in globals():
            system_status_label.config(text=current_language["system_status"])
        
        # Cập nhật card titles
        if 'threads_card' in globals() and threads_card.winfo_exists():
            threads_card.winfo_children()[0].winfo_children()[1].config(text=current_language["running_threads"])
        if 'steps_card' in globals() and steps_card.winfo_exists():
            steps_card.winfo_children()[0].winfo_children()[1].config(text=current_language["total_steps"])
        if 'profiles_card' in globals() and profiles_card.winfo_exists():
            profiles_card.winfo_children()[0].winfo_children()[1].config(text=current_language["profiles_count"])
        if 'accounts_card' in globals() and accounts_card.winfo_exists():
            accounts_card.winfo_children()[0].winfo_children()[1].config(text=current_language["accounts_count"])
        
        # Cập nhật các nút trên dashboard
        for btn_text, btn in dashboard_buttons.items():
            if btn_text == "refresh":
                btn.config(text=current_language["refresh"])
            elif btn_text == "view_profiles":
                btn.config(text=current_language["view_profiles"])
            elif btn_text == "delete_profiles":
                btn.config(text=current_language["delete_profiles"])
            elif btn_text == "install_chrome":
                btn.config(text=current_language["install_chromedriver"])
            elif btn_text == "update_app":
                btn.config(text=current_language["update_app"])
            elif btn_text == "guide":
                btn.config(text=current_language["guide"])
            elif btn_text == "show_steps":
                btn.config(text=current_language["show_steps_window"])
            elif btn_text == "arrange_windows":
                btn.config(text=current_language["arrange_windows"])
        
        # Cập nhật các nút trong tab script
        if 'edit_step_btn' in globals() and edit_step_btn.winfo_exists():
            edit_step_btn.config(text=current_language["edit_step"])
        if 'delete_step_btn' in globals() and delete_step_btn.winfo_exists():
            delete_step_btn.config(text=current_language["delete_step"])
        if 'save_script_btn' in globals() and save_script_btn.winfo_exists():
            save_script_btn.config(text=current_language["save_script"])
        
        # Cập nhật các thành phần trong tab settings
        if 'add_step_frame' in globals() and add_step_frame.winfo_exists():
            add_step_frame.config(text=current_language["add_new_step"])
        if 'action_label' in globals() and action_label.winfo_exists():
            action_label.config(text=current_language["action"])
        if 'value_label' in globals() and value_label.winfo_exists():
            value_label.config(text=current_language["value"])
        if 'add_field_btn' in globals() and add_field_btn.winfo_exists():
            add_field_btn.config(text=current_language["add_field"])
        if 'load_accounts_btn' in globals() and load_accounts_btn.winfo_exists():
            load_accounts_btn.config(text=current_language["load_accounts"])
        if 'add_step_btn' in globals() and add_step_btn.winfo_exists():
            add_step_btn.config(text=current_language["add_step"])
        if 'run_settings_frame' in globals() and run_settings_frame.winfo_exists():
            run_settings_frame.config(text=current_language["run_settings"])
        if 'auto_load_checkbox' in globals() and auto_load_checkbox.winfo_exists():
            auto_load_checkbox.config(text=current_language["auto_load_accounts"])
        if 'threads_label' in globals() and threads_label.winfo_exists():
            threads_label.config(text=current_language["threads"])
        if 'chrome_size_label' in globals() and chrome_size_label.winfo_exists():
            chrome_size_label.config(text=current_language["chrome_size"])
        if 'hide_chrome_check' in globals() and hide_chrome_check.winfo_exists():
            hide_chrome_check.config(text=current_language["hide_chrome"])
        if 'auto_close_check' in globals() and auto_close_check.winfo_exists():
            auto_close_check.config(text=current_language["auto_close_chrome"])
        if 'auto_create_check' in globals() and auto_create_check.winfo_exists():
            auto_create_check.config(text=current_language["auto_create_profiles"])
        if 'delete_profiles_check' in globals() and delete_profiles_check.winfo_exists():
            delete_profiles_check.config(text=current_language["delete_profiles_after"])
        if 'schedule_label' in globals() and schedule_label.winfo_exists():
            schedule_label.config(text=current_language["schedule_run"])
        if 'hour_label' in globals() and hour_label.winfo_exists():
            hour_label.config(text=current_language["hour"])
        if 'minute_label' in globals() and minute_label.winfo_exists():
            minute_label.config(text=current_language["minute"])
        if 'schedule_btn' in globals() and schedule_btn.winfo_exists():
            schedule_btn.config(text=current_language["schedule_button"])
        if 'run_script_btn' in globals() and run_script_btn.winfo_exists():
            run_script_btn.config(text=current_language["run_script"])
        if 'progress_label' in globals() and progress_label.winfo_exists():
            progress_label.config(text=current_language["ready"])
        if 'use_profile_checkbox' in globals() and use_profile_checkbox.winfo_exists():
            use_profile_checkbox.config(text=current_language["select_profile_to_run"])
        if 'random_xpath_btn' in globals() and random_xpath_btn.winfo_exists():
            random_xpath_btn.config(text=current_language["manage_xpath_groups"])
        
        # Cập nhật combobox ngôn ngữ
        if 'language_combo' in globals() and language_combo.winfo_exists():
            language_combo.set(current_language["language_option_vn"] if current_language == Language.VIETNAMESE else current_language["language_option_en"])
        
        # Cập nhật giá trị trong action combo
        if 'action_combo' in globals() and action_combo.winfo_exists():
            action_combo['values'] = [
                "Mở URL",
                "Ngủ",
                "Click XPath",
                "Gửi ký tự (XPath|Text)",
                "Swipe (Hướng|Pixel đầu|Pixel cuối)",
                "Click Full XPath",
                "Tìm kiếm hình ảnh",
                "Chụp màn hình và lưu template",
                "Tùy chỉnh",
                "Tìm và Nhập (Text|Value)",
                "Tìm và Nhập vào Phần Tử Gần Kề (Text|Value|Position|ElementType)",
                current_language["click_random_xpath_1"],
                current_language["click_random_xpath_2"],
                current_language["click_random_xpath_3"],
                current_language["click_random_xpath_5"],
                current_language["click_random_xpath_10"],
                current_language["click_random_xpath_custom"]
            ]
        
        # Cập nhật tab arrange windows
        if 'arrange_settings_label' in globals() and arrange_settings_label.winfo_exists():
            arrange_settings_label.config(text=current_language["arrange_settings_title"])
        if 'arrange_columns_label' in globals() and arrange_columns_label.winfo_exists():
            arrange_columns_label.config(text=current_language["arrange_columns"])
        if 'arrange_rows_label' in globals() and arrange_rows_label.winfo_exists():
            arrange_rows_label.config(text=current_language["arrange_rows"])
        if 'arrange_gap_label' in globals() and arrange_gap_label.winfo_exists():
            arrange_gap_label.config(text=current_language["arrange_gap"])
        if 'arrange_auto_checkbox' in globals() and arrange_auto_checkbox.winfo_exists():
            arrange_auto_checkbox.config(text=current_language["arrange_auto"])
        if 'arrange_auto_desc_label' in globals() and arrange_auto_desc_label.winfo_exists():
            arrange_auto_desc_label.config(text=current_language["arrange_auto_desc"])
        if 'arrange_now_btn' in globals() and arrange_now_btn.winfo_exists():
            arrange_now_btn.config(text=current_language["arrange_button"])
        if 'arrange_notes_label' in globals() and arrange_notes_label.winfo_exists():
            arrange_notes_label.config(text=current_language["arrange_notes"])
        
        # Cập nhật floating action button
        if 'fab' in globals() and fab.winfo_exists():
            fab.config(text="▶️")
        
    except Exception as e:
        logging.error(f"Error updating UI language: {e}")

# ================== CÁC HÀM LOGIC TỪ CODE CŨ ==================

# Cấu hình logging
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def load_settings():
    settings = {
        "threads": "1", "width": "1200", "height": "800",
        "auto_create_profiles": "True", "delete_profiles_after_run": "False",
        "language": "vi", "auto_load_accounts": "True", "theme": "darkly",
        "arrange_auto": "False", "arrange_columns": "3", "arrange_rows": "2", "arrange_gap": "10"
    }
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    if '=' in line:
                        k, v = line.strip().split('=', 1)
                        settings[k] = v
        except Exception as e:
            logging.error(f"Lỗi khi tải settings: {e}")
    return settings

def save_settings():
    try:
        lang_code = "vi" if current_language == Language.VIETNAMESE else "en"
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            f.write(f"threads={threads_entry.get()}\n")
            f.write(f"width={chrome_width.get()}\n")
            f.write(f"height={chrome_height.get()}\n")
            f.write(f"auto_create_profiles={auto_create_profiles_var.get()}\n")
            f.write(f"delete_profiles_after_run={delete_profiles_after_run_var.get()}\n")
            f.write(f"language={lang_code}\n")
            f.write(f"auto_load_accounts={auto_load_accounts_var.get()}\n")
            f.write(f"theme={current_theme}\n")
            f.write(f"arrange_auto={arrange_auto_var.get()}\n")
            f.write(f"arrange_columns={arrange_columns_entry.get()}\n")
            f.write(f"arrange_rows={arrange_rows_entry.get()}\n")
            f.write(f"arrange_gap={arrange_gap_entry.get()}\n")
    except Exception as e:
        logging.error(f"Lỗi khi lưu settings: {e}")

def change_language(lang_code):
    global current_language
    if lang_code == "en":
        current_language = Language.ENGLISH
    else:
        current_language = Language.VIETNAMESE
    update_ui_language()

def change_theme(theme_name):
    global current_theme
    current_theme = theme_name
    style.theme_use(theme_name)
    update_theme_dependent_widgets()

def update_theme_dependent_widgets():
    pass

def create_profile_dir(profile_id):
    try:
        if not os.path.exists(PROFILES_DIR):
            os.makedirs(PROFILES_DIR)
            logging.info(f"Tạo thư mục profiles: {PROFILES_DIR}")
        profile_path = os.path.join(PROFILES_DIR, f"chrome_profile_{profile_id}")
        if os.path.exists(profile_path):
            logging.info(f"Tái sử dụng profile hiện có: {profile_path}")
        else:
            os.makedirs(profile_path)
            logging.info(f"Tạo profile mới: {profile_path}")
        return profile_path
    except Exception as e:
        logging.error(f"Lỗi khi tạo profile {profile_id}: {e}")
        raise

def clear_profiles():
    try:
        if os.path.exists(PROFILES_DIR):
            if messagebox.askyesno(
                current_language["confirm_delete"],
                current_language["delete_all_profiles"],
                parent=root
            ):
                shutil.rmtree(PROFILES_DIR)
                logging.info("Đã xóa tất cả thư mục profile")
                messagebox.showinfo(current_language["success"], current_language["profiles_deleted"])
        else:
            messagebox.showinfo(current_language["info"], current_language["no_profiles"])
    except Exception as e:
        logging.error(f"Lỗi khi xóa profiles: {e}")
        messagebox.showerror(current_language["error"], f"{current_language['delete_failed']}: {e}")

def list_profiles():
    try:
        if not os.path.exists(PROFILES_DIR):
            return []
        profiles = [f for f in os.listdir(PROFILES_DIR) if f.startswith("chrome_profile_")]
        return profiles
    except Exception as e:
        logging.error(f"Lỗi khi liệt kê profiles: {e}")
        return []

def show_profiles():
    profiles = list_profiles()
    win = tk.Toplevel(root)
    win.title(current_language["profiles_title"])
    win.geometry("300x300")
    tk.Label(win, text=current_language["profiles_list"], font=("Arial", 10, "bold")).pack(pady=5)
    profile_listbox = tk.Listbox(win, width=30, height=10)
    profile_listbox.pack(pady=5)
    for profile in profiles:
        profile_listbox.insert(tk.END, profile)
    if not profiles:
        profile_listbox.insert(tk.END, current_language["no_profiles"])
    tk.Button(win, text=current_language["close_button"], command=win.destroy).pack(pady=5)

def show_guide():
    guide_text = """
    1. Nhập tay các bước đăng nhập Google:
    - Bước 1: Chọn 'Mở URL', nhập 'https://accounts.google.com'.
    - Bước 2: Chọn 'Gửi ký tự (XPath|Text)', nhập '//*[@id="identifierId"]|your_email@gmail.com'.
    - Bước 3: Chọn 'Click XPath', nhập '//*[@id="identifierNext"]/div/button'.
    - Bước 4: Chọn 'Ngủ', nhập '2' (giây).
    - Bước 5: Chọn 'Gửi ký tự (XPath|Text)', nhập '//input[@name="Passwd"]|your_password'.
    - Bước 6: Chọn 'Click XPath', nhập '//*[@id="passwordNext"]/div/button'.
    - Bước 7: Chọn 'Ngủ', nhập '5' (giây).
    
    2. Các hành động khác:
    - Mở URL: Nhập đường dẫn website.
    - Ngủ: Nhập số giây cần chờ.
    - Click XPath: Nhập XPath của nút cần click.
    - Gửi ký tự (XPath|Text): Nhập XPath và nội dung.
    - Swipe (Hướng|Pixel đầu|Pixel cuối): Nhập hướng, số pixel đầu và cuối.
    - Click Full XPath: Nhập XPath, dùng JavaScript để click.
    - Tìm kiếm hình ảnh: Tìm và click vào hình ảnh trên màn hình.
    - Chụp màn hình và lưu template: Chụp khu vực màn hình để tạo template.
    - Tùy chỉnh: Viết mã Python tùy chỉnh.
    
    3. HỆ THỐNG NHÓM XPATH RANDOM:
    - 'Click Random 1 XPath': Click 1 XPath ngẫu nhiên từ Nhóm 1
    - 'Click Random 2 XPath': Click 2 XPath ngẫu nhiên từ Nhóm 2
    - 'Click Random 3 XPath': Click 3 XPath ngẫu nhiên từ Nhóm 3
    - 'Click Random 5 XPath': Click 5 XPath ngẫu nhiên từ Nhóm 5
    - 'Click Random 10 XPath': Click 10 XPath ngẫu nhiên từ Nhóm 10
    - 'Click Random XPath (tùy chỉnh)': Click XPath từ Nhóm Custom
    
    4. TÍNH NĂNG MỚI - SẮP XẾP CỬA SỔ:
    - Chuyển sang tab '🪟 Sắp xếp cửa sổ' để cấu hình
    - Có thể chọn số cột, số hàng và khoảng cách giữa các cửa sổ
    - Bật 'Tự động sắp xếp khi chạy script' để tự động sắp xếp khi bắt đầu
    - Cửa sổ sẽ được sắp xếp tự động thành lưới trên màn hình
    
    5. Quản lý Chrome Profiles:
    - Bật 'Tạo profile tự động' để tạo thư mục profile.
    - Tắt 'Xóa profile sau khi chạy' để giữ cookies.
    - Nhấn 'Xem Profiles' để kiểm tra danh sách profile.
    - Nhấn 'Xóa Tất Cả Profiles' để xóa toàn bộ profile.
    """
    messagebox.showinfo(current_language["guide_title"], guide_text)

def find_image_on_screen(template_path, confidence=0.8, grayscale=True):
    try:
        screenshot = pyautogui.screenshot()
        screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        template = cv2.imread(template_path)
        if template is None:
            logging.error(f"Không thể đọc template: {template_path}")
            return None
        
        if grayscale:
            screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
            template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        else:
            screenshot_gray = screenshot_np
            template_gray = template
        
        result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= confidence:
            h, w = template_gray.shape[:2]
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            return (center_x, center_y)
        else:
            return None
    except Exception as e:
        logging.error(f"Lỗi khi tìm kiếm hình ảnh {template_path}: {e}")
        return None

def capture_template_area():
    try:
        messagebox.showinfo("Chụp template", "Chuẩn bị chụp template.")
        time.sleep(2)
        
        print("Nhấn Enter khi chuột ở góc trên bên trái...")
        input()
        x1, y1 = pyautogui.position()
        
        print("Di chuyển chuột đến góc dưới bên phải và nhấn Enter...")
        input()
        x2, y2 = pyautogui.position()
        
        if x2 <= x1 or y2 <= y1:
            messagebox.showerror("Lỗi", "Tọa độ không hợp lệ")
            return None
        
        width = x2 - x1
        height = y2 - y1
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        
        name = simpledialog.askstring("Tên template", "Nhập tên template:")
        if not name:
            return None
        
        file_path = os.path.join(IMAGE_TEMPLATES_DIR, f"{name}.png")
        screenshot.save(file_path)
        messagebox.showinfo("Thành công", f"Đã lưu template: {file_path}")
        return (x1, y1, width, height)
    except Exception as e:
        logging.error(f"Lỗi khi chụp template: {e}")
        return None

def image_search_action(template_name, action="click", offset_x=0, offset_y=0, confidence=0.8, **kwargs):
    template_path = os.path.join(IMAGE_TEMPLATES_DIR, template_name)
    if not os.path.exists(template_path):
        logging.error(f"Template không tồn tại: {template_path}")
        return False
    
    position = find_image_on_screen(template_path, confidence)
    if position:
        x, y = position
        target_x = x + offset_x
        target_y = y + offset_y
        
        if action == "click":
            pyautogui.click(target_x, target_y)
            logging.info(f"Đã click tại ({target_x}, {target_y})")
            return True
        elif action == "double_click":
            pyautogui.doubleClick(target_x, target_y)
            logging.info(f"Đã double click tại ({target_x}, {target_y})")
            return True
        elif action == "type":
            text = kwargs.get('text', '')
            if text:
                pyautogui.click(target_x, target_y)
                time.sleep(0.1)
                pyautogui.write(text)
                logging.info(f"Đã nhập '{text}' tại ({target_x}, {target_y})")
                return True
    return False

def auto_load_accounts():
    try:
        account_file = "account.txt"
        if os.path.exists(account_file):
            logging.info(f"Tìm thấy file {account_file}, đang tải tự động...")
            if load_accounts_from_file(account_file):
                messagebox.showinfo(
                    current_language["success"],
                    f"{current_language['accounts_loaded']}: {len(accounts)}"
                )
                return True
        else:
            logging.info(f"Không tìm thấy file {account_file}")
            return False
    except Exception as e:
        logging.error(f"Lỗi khi tự động tải account.txt: {e}")
        return False

def load_accounts_from_file(filepath):
    try:
        global accounts
        accounts = []
        with open(filepath, "r", encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
        if not lines:
            messagebox.showwarning(current_language["warning"], "File rỗng")
            return False
        
        headers = lines[0].split("|")
        for ln in lines[1:]:
            vals = ln.split("|")
            acc = {h: vals[i] if i < len(vals) else "" for i, h in enumerate(headers)}
            accounts.append(acc)
        
        logging.info(f"Đã tải {len(accounts)} tài khoản từ {filepath}")
        return True
    except Exception as e:
        logging.error(f"Lỗi khi tải tài khoản từ {filepath}: {e}")
        return False

def load_accounts_from_text():
    try:
        fp = filedialog.askopenfilename(
            title=current_language["load_accounts"],
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not fp:
            return
        
        if load_accounts_from_file(fp):
            messagebox.showinfo(
                current_language["success"],
                f"{current_language['accounts_loaded']}: {len(accounts)}"
            )
    except Exception as e:
        logging.error(f"Lỗi khi tải tài khoản: {e}")

def show_steps_window():
    try:
        steps_win = tk.Toplevel(root)
        steps_win.title(current_language["steps_window_title"])
        steps_win.geometry("800x500")
        
        main_frame = tk.Frame(steps_win)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        columns = ("step", "action", "value")
        tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=20)
        
        tree.heading("step", text=current_language["step"])
        tree.heading("action", text=current_language["action_col"])
        tree.heading("value", text=current_language["value_col"])
        
        tree.column("step", width=50, anchor="center")
        tree.column("action", width=200)
        tree.column("value", width=500)
        
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        for i, (action, value) in enumerate(script_steps, 1):
            tree.insert("", tk.END, values=(i, action, value))
        
        button_frame = tk.Frame(steps_win)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(button_frame, text=current_language["close_button"], 
                 command=steps_win.destroy).pack(side=tk.RIGHT, padx=5)
        
    except Exception as e:
        logging.error(f"Lỗi khi mở cửa sổ hiển thị bước: {e}")

def update_main_script_listbox():
    try:
        script_listbox.delete(0, tk.END)
        for a, v in script_steps:
            display_text = f"{a} | {v[:50]}{'...' if len(v) > 50 else ''}"
            script_listbox.insert(tk.END, display_text)
        update_dashboard_stats()
    except Exception as e:
        logging.error(f"Lỗi khi cập nhật listbox chính: {e}")

def update_steps_listbox_tab2():
    try:
        tab2_steps_listbox.delete(0, tk.END)
        for a, v in script_steps:
            display_text = f"{a} | {v[:50]}{'...' if len(v) > 50 else ''}"
            tab2_steps_listbox.insert(tk.END, display_text)
    except Exception as e:
        logging.error(f"Lỗi khi cập nhật listbox tab 2: {e}")

def edit_step_window(step_index):
    try:
        old_action, old_value = script_steps[step_index]
        win = tk.Toplevel(root)
        win.title(f"Chỉnh sửa bước {step_index + 1}")
        win.geometry("450x450")
        
        tk.Label(win, text="Hành động:", font=('Arial', 10)).pack(pady=5)
        action_entry = ttk.Combobox(win, values=action_combo['values'], width=30)
        action_entry.set(old_action)
        action_entry.pack(pady=5)
        
        tk.Label(win, text="Giá trị:", font=('Arial', 10)).pack(pady=5)
        value_entry_edit = tk.Text(win, width=50, height=8)
        value_entry_edit.insert("1.0", old_value)
        value_entry_edit.pack(pady=5)
        
        def save_edit():
            try:
                new_action = action_entry.get()
                new_value = value_entry_edit.get("1.0", tk.END).strip()
                if not new_action:
                    messagebox.showwarning(current_language["warning"], "Hành động không được để trống.")
                    return
                
                script_steps[step_index] = (new_action, new_value)
                update_main_script_listbox()
                update_steps_listbox_tab2()
                win.destroy()
                messagebox.showinfo(current_language["success"], "Đã cập nhật bước thành công!")
            except Exception as e:
                logging.error(f"Lỗi khi chỉnh sửa bước: {e}")
        
        tk.Button(win, text="Lưu", command=save_edit, bg="lightgreen").pack(pady=10)
        
    except Exception as e:
        logging.error(f"Lỗi khi mở cửa sổ chỉnh sửa bước: {e}")

def edit_step(event=None):
    try:
        sel = script_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        if idx < len(script_steps):
            edit_step_window(idx)
    except Exception as e:
        logging.error(f"Lỗi khi mở cửa sổ chỉnh sửa bước: {e}")

def edit_step_tab2(event=None):
    try:
        sel = tab2_steps_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        if idx < len(script_steps):
            edit_step_window(idx)
    except Exception as e:
        logging.error(f"Lỗi khi chỉnh sửa bước từ tab 2: {e}")

def delete_step():
    try:
        sel = script_listbox.curselection()
        if not sel:
            messagebox.showwarning(current_language["warning"], "Chọn bước cần xóa.")
            return
        idx = sel[0]
        if idx < len(script_steps):
            del script_steps[idx]
            update_main_script_listbox()
            update_steps_listbox_tab2()
    except Exception as e:
        logging.error(f"Lỗi khi xóa bước: {e}")

def delete_step_tab2():
    try:
        sel = tab2_steps_listbox.curselection()
        if not sel:
            messagebox.showwarning(current_language["warning"], "Chọn bước cần xóa.")
            return
        idx = sel[0]
        if idx < len(script_steps):
            del script_steps[idx]
            update_main_script_listbox()
            update_steps_listbox_tab2()
    except Exception as e:
        logging.error(f"Lỗi khi xóa bước từ tab 2: {e}")

def refresh_script_list():
    try:
        if not os.path.exists("script"):
            os.makedirs("script")
        files = [f for f in os.listdir("script") if f.endswith((".json", ".txt"))]
        script_option_listbox.delete(0, tk.END)
        for f in files:
            script_option_listbox.insert(tk.END, f)
    except Exception as e:
        logging.error(f"Lỗi khi tải danh sách script: {e}")

def on_script_option_select(event=None):
    try:
        sel = script_option_listbox.curselection()
        if not sel:
            return
        fname = script_option_listbox.get(sel[0])
        fp = os.path.join("script", fname)
        global script_steps
        script_steps = []
        if fname.endswith(".json"):
            with open(fp, "r", encoding="utf-8") as f:
                script_steps = json.load(f)
        elif fname.endswith(".txt"):
            with open(fp, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("|", 1)
                    script_steps.append((parts[0], parts[1] if len(parts) > 1 else ""))
        update_main_script_listbox()
        update_steps_listbox_tab2()
        messagebox.showinfo(current_language["success"], f"Đã tải script: {fname}")
    except Exception as e:
        logging.error(f"Lỗi khi tải script {fname}: {e}")

def save_script():
    try:
        if not os.path.exists("script"):
            os.makedirs("script")
        win = tk.Toplevel(root)
        win.title("Lưu script")
        win.geometry("400x300")
        tk.Label(win, text="Tên script (để trống = timestamp):").pack(pady=5)
        ne = tk.Entry(win, width=30)
        ne.pack(pady=5)
        tk.Label(win, text="Hoặc dán nội dung TXT (Action|Value mỗi dòng):").pack(pady=5)
        txt = tk.Text(win, height=5, width=30)
        txt.pack(pady=5)
        def on_save():
            try:
                name = ne.get().strip() or datetime.now().strftime("%H_%M_%S-%d-%m-%Y")
                fp = os.path.join("script", name + ".json")
                steps = script_steps.copy()
                txt_content = txt.get("1.0", tk.END).strip()
                if txt_content:
                    steps = []
                    for line in txt_content.splitlines():
                        line = line.strip()
                        if not line:
                            continue
                        parts = line.split("|", 1)
                        steps.append([parts[0], parts[1] if len(parts) > 1 else ""])
                else:
                    steps = [[a, v] for a, v in steps]
                with open(fp, "w", encoding="utf-8") as f:
                    json.dump(steps, f, ensure_ascii=False, indent=2)
                messagebox.showinfo(current_language["success"], f"Đã lưu script vào: {fp}")
                win.destroy()
                refresh_script_list()
            except Exception as e:
                logging.error(f"Lỗi khi lưu script: {e}")
        tk.Button(win, text="Lưu", command=on_save).pack(pady=10)
    except Exception as e:
        logging.error(f"Lỗi khi mở cửa sổ lưu script: {e}")

def add_step():
    action = action_combo.get()
    value = value_entry.get().strip()
    
    if action == "Tùy chỉnh":
        open_custom_code_popup()
        return
    elif action == "Chụp màn hình và lưu template":
        capture_template_area()
        return
    elif action == "Tìm kiếm hình ảnh":
        open_image_search_popup()
        return
    
    # Xử lý các hành động click random
    elif action == current_language["click_random_xpath_1"]:
        group_name = "group_1"
    elif action == current_language["click_random_xpath_2"]:
        group_name = "group_2"
    elif action == current_language["click_random_xpath_3"]:
        group_name = "group_3"
    elif action == current_language["click_random_xpath_5"]:
        group_name = "group_5"
    elif action == current_language["click_random_xpath_10"]:
        group_name = "group_10"
    elif action == current_language["click_random_xpath_custom"]:
        group_name = "group_custom"
        count = simpledialog.askinteger(
            "Số lượng XPath",
            f"Nhập số lượng XPath random cần click (1-100):",
            parent=root,
            minvalue=1,
            maxvalue=100
        )
        if not count:
            return
        value = str(count)
    else:
        # Các action khác
        if not action:
            messagebox.showwarning(current_language["warning"], "Vui lòng chọn thao tác.")
            return
        
        script_steps.append((action, value))
        update_main_script_listbox()
        update_steps_listbox_tab2()
        value_entry.delete(0, tk.END)
        return
    
    # Thêm vào script steps
    script_steps.append((action, value))
    update_main_script_listbox()
    update_steps_listbox_tab2()
    value_entry.delete(0, tk.END)

def open_custom_code_popup():
    try:
        win = tk.Toplevel(root)
        win.title(current_language["custom_code_title"])
        win.geometry("600x450")
        tk.Label(win, text=current_language["enter_code"], font=("Arial", 10, "bold")).pack(pady=5)
        code_text = tk.Text(win, width=70, height=18, font=("Consolas", 10))
        code_text.pack(pady=5)
        def save_code_action():
            try:
                user_code = code_text.get("1.0", tk.END).strip()
                if user_code:
                    script_steps.append(("Tùy chỉnh", user_code))
                    update_main_script_listbox()
                    update_steps_listbox_tab2()
                    win.destroy()
                else:
                    messagebox.showwarning(current_language["warning"], "Bạn chưa nhập mã Python.")
            except Exception as e:
                logging.error(f"Lỗi khi lưu mã tùy chỉnh: {e}")
        tk.Button(win, text=current_language["save_code_action"], command=save_code_action).pack(pady=10)
    except Exception as e:
        logging.error(f"Lỗi khi mở cửa sổ mã tùy chỉnh: {e}")

def open_image_search_popup():
    try:
        win = tk.Toplevel(root)
        win.title("Tìm kiếm hình ảnh")
        win.geometry("650x400")
        
        tk.Label(win, text=current_language["select_template"], font=("Arial", 10, "bold")).pack(pady=5)
        
        template_frame = tk.Frame(win)
        template_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        template_listbox_local = tk.Listbox(template_frame, height=8)
        template_listbox_local.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(template_frame, orient="vertical", command=template_listbox_local.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        template_listbox_local.config(yscrollcommand=scrollbar.set)
        
        if not os.path.exists(IMAGE_TEMPLATES_DIR):
            os.makedirs(IMAGE_TEMPLATES_DIR)
        files = [f for f in os.listdir(IMAGE_TEMPLATES_DIR) if f.endswith((".png", ".jpg", ".jpeg", ".bmp"))]
        for f in files:
            template_listbox_local.insert(tk.END, f)
        
        def save_image_action():
            try:
                sel = template_listbox_local.curselection()
                if not sel:
                    messagebox.showwarning(current_language["warning"], "Vui lòng chọn template.")
                    return
                
                template_name = template_listbox_local.get(sel[0])
                script_steps.append(("Tìm kiếm hình ảnh", f"{template_name}|click|0|0|0.8"))
                update_main_script_listbox()
                update_steps_listbox_tab2()
                win.destroy()
                
            except Exception as e:
                logging.error(f"Lỗi khi lưu hành động hình ảnh: {e}")
        
        tk.Button(win, text=current_language["save_action"], command=save_image_action).pack(pady=10)
        
    except Exception as e:
        logging.error(f"Lỗi khi mở cửa sổ tìm kiếm hình ảnh: {e}")

def click_random_xpaths_from_group(driver, group_name="group_1", count=1):
    try:
        xpaths = random_xpath_groups.get(group_name, [])
        
        if not xpaths:
            logging.warning(f"Nhóm XPath '{group_name}' trống")
            return False
        
        actual_count = min(count, len(xpaths))
        
        if actual_count == len(xpaths):
            selected_xpaths = xpaths.copy()
        else:
            selected_xpaths = random.sample(xpaths, actual_count)
        
        success_count = 0
        
        for i, xpath in enumerate(selected_xpaths, 1):
            try:
                elements = driver.find_elements(By.XPATH, xpath)
                if not elements:
                    logging.error(f"Không tìm thấy element với XPath: {xpath}")
                    continue
                
                element = elements[0]
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                time.sleep(0.3)
                
                element.click()
                logging.info(f"Đã click XPath từ nhóm {group_name} ({i}/{actual_count})")
                success_count += 1
                time.sleep(0.5)
                
            except Exception as e:
                logging.error(f"Không thể click XPath {xpath}: {e}")
        
        logging.info(f"Đã click thành công {success_count}/{actual_count} XPath từ nhóm {group_name}")
        return success_count > 0
                
    except Exception as e:
        logging.error(f"Lỗi khi click XPath từ nhóm {group_name}: {e}")
        return False

def run_script_instance(account=None, headless=False, profile_path=None, use_specific_profile=None):
    try:
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        if use_specific_profile and profile_path:
            options.add_argument(f"--user-data-dir={profile_path}")
        elif profile_path:
            options.add_argument(f"--user-data-dir={profile_path}")
            
        if os.path.exists(CHROMEDRIVER_PATH):
            service = Service(CHROMEDRIVER_PATH)
            driver = webdriver.Chrome(service=service, options=options)
        else:
            import undetected_chromedriver as uc
            driver = uc.Chrome(options=options)

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        if not headless:
            active_drivers.append(driver)
            
        try:
            w = int(chrome_width.get())
            h = int(chrome_height.get())
            driver.set_window_size(w, h)
        except Exception as e:
            logging.error(f"Lỗi khi đặt kích thước cửa sổ: {e}")

        for action, value in script_steps:
            try:
                if action == "Mở URL":
                    driver.get(value)
                elif action == "Ngủ":
                    time.sleep(float(value))
                elif action == "Click XPath":
                    element = driver.find_element(By.XPATH, value)
                    element.click()
                elif action == current_language["click_random_xpath_1"]:
                    click_random_xpaths_from_group(driver, "group_1", 1)
                elif action == current_language["click_random_xpath_2"]:
                    click_random_xpaths_from_group(driver, "group_2", 2)
                elif action == current_language["click_random_xpath_3"]:
                    click_random_xpaths_from_group(driver, "group_3", 3)
                elif action == current_language["click_random_xpath_5"]:
                    click_random_xpaths_from_group(driver, "group_5", 5)
                elif action == current_language["click_random_xpath_10"]:
                    click_random_xpaths_from_group(driver, "group_10", 10)
                elif action == current_language["click_random_xpath_custom"]:
                    try:
                        count = int(value.strip())
                        if count < 1: count = 1
                        elif count > 100: count = 100
                        click_random_xpaths_from_group(driver, "group_custom", count)
                    except:
                        click_random_xpaths_from_group(driver, "group_custom", 1)
                elif action in ["Gửi ký tự (XPath|Text)", "Send Keys (XPath|Text)"]:
                    xpath, text = value.split("|", 1)
                    if account:
                        for k, v in account.items():
                            text = text.replace(f"{{{k}}}", str(v or ""))
                    driver.find_element(By.XPATH, xpath).send_keys(text)
                elif action == "Click Full XPath":
                    element = driver.find_element(By.XPATH, value)
                    driver.execute_script("arguments[0].click();", element)
                elif action == "Tìm kiếm hình ảnh":
                    parts = value.split("|")
                    template_name = parts[0]
                    img_action = parts[1] if len(parts) > 1 else "click"
                    offset_x = int(parts[2]) if len(parts) > 2 else 0
                    offset_y = int(parts[3]) if len(parts) > 3 else 0
                    confidence = float(parts[4]) if len(parts) > 4 else 0.8
                    
                    kwargs = {}
                    if img_action == "type" and len(parts) > 5:
                        kwargs['text'] = parts[5]
                        if account:
                            for k, v in account.items():
                                kwargs['text'] = kwargs['text'].replace(f"{{{k}}}", str(v or ""))
                    
                    image_search_action(template_name, img_action, offset_x, offset_y, confidence, **kwargs)
                elif action == "Chụp màn hình và lưu template":
                    capture_template_area()
                elif action == "Tùy chỉnh":
                    value = value.replace("{profile_path}", profile_path if profile_path else "")
                    if account:
                        for k, v in account.items():
                            value = value.replace(f"{{{k}}}", str(v or ""))
                    local_vars = {
                        "driver": driver,
                        "account": account,
                        "By": By,
                        "time": time,
                        "pyautogui": pyautogui,
                        "cv2": cv2,
                        "np": np,
                        "find_image_on_screen": find_image_on_screen,
                        "image_search_action": image_search_action,
                        "click_random_xpaths_from_group": click_random_xpaths_from_group,
                        "sympify": sympify   # <--- THÊM DÒNG NÀY
                    }
                    exec(value, {}, local_vars)
                    
            except Exception as e:
                logging.error(f"Lỗi khi thực thi hành động '{action}': {e}")
        
        logging.info("Hoàn thành 1 phiên chạy")
        if auto_quit_var.get():
            if driver in active_drivers:
                active_drivers.remove(driver)
            driver.quit()
    except Exception as e:
        logging.error(f"Lỗi khi chạy script instance: {e}")

def arrange_windows_auto():
    """Hàm tự động sắp xếp cửa sổ khi chạy script"""
    try:
        if not active_drivers:
            logging.info("Không có cửa sổ Chrome nào để sắp xếp")
            return
        
        if headless_var.get():
            logging.info("Chế độ headless - không sắp xếp cửa sổ")
            return
        
        if not arrange_auto_var.get():
            logging.info("Tự động sắp xếp đã tắt - không sắp xếp cửa sổ")
            return
        
        cols = int(arrange_columns_entry.get())
        rows = int(arrange_rows_entry.get())
        gap = int(arrange_gap_entry.get())
        
        if cols <= 0 or rows <= 0:
            logging.error("Số cột và số hàng phải lớn hơn 0")
            return
        
        screen_width, screen_height = pyautogui.size()
        window_width = (screen_width - (cols + 1) * gap) // cols
        window_height = (screen_height - (rows + 1) * gap) // rows
        
        arranged_count = 0
        for i, driver in enumerate(active_drivers):
            if i >= cols * rows:
                break
            
            try:
                row = i // cols
                col = i % cols
                
                x = col * (window_width + gap) + gap
                y = row * (window_height + gap) + gap
                
                driver.set_window_position(x, y)
                driver.set_window_size(window_width, window_height)
                
                arranged_count += 1
                logging.info(f"Đã tự động sắp xếp cửa sổ {i+1} tại ({x}, {y})")
                
            except Exception as e:
                logging.error(f"Không thể tự động sắp xếp cửa sổ {i+1}: {e}")
        
        if arranged_count > 0:
            logging.info(f"Đã tự động sắp xếp {arranged_count} cửa sổ Chrome")
                    
    except ValueError:
        logging.error("Vui lòng nhập số nguyên hợp lệ cho cài đặt sắp xếp")
    except Exception as e:
        logging.error(f"Lỗi khi tự động sắp xếp cửa sổ: {e}")

def run_multithread():
    try:
        n = int(threads_entry.get())
        head = headless_var.get()
        use_specific_profile = use_specific_profile_var.get() if n == 1 else False
        
        if not script_steps:
            messagebox.showwarning(current_language["warning"], "Vui lòng thêm bước trước khi chạy.")
            return
        
        # Xóa danh sách active_drivers cũ
        global active_drivers
        active_drivers = []
            
        progress_var.set(0)
        progressbar['maximum'] = n
        progress_label.config(text="Đang chạy...")
        threads = []
        tot = n

        profile_paths = []
        if auto_create_profiles_var.get():
            for i in range(n):
                profile_path = create_profile_dir(i + 1)
                profile_paths.append(profile_path)
        else:
            profile_paths = [None] * n

        def wrapper(acc, hd, profile_path, use_specific):
            try:
                run_script_instance(acc, hd, profile_path, use_specific)
                progress_var.set(progress_var.get() + 1)
                progressbar.update()
                progress_label.config(text=f"Đã xong {progress_var.get()}/{tot}")
                if delete_profiles_after_run_var.get() and profile_path:
                    try:
                        shutil.rmtree(profile_path)
                        logging.info(f"Đã xóa profile: {profile_path}")
                    except Exception as e:
                        logging.error(f"Lỗi khi xóa profile {profile_path}: {e}")
            except Exception as e:
                logging.error(f"Lỗi trong luồng {profile_path}: {e}")
                progress_var.set(progress_var.get() + 1)
                progressbar.update()
                progress_label.config(text=f"Đã xong {progress_var.get()}/{tot}")

        for i in range(n):
            acc = accounts[i % len(accounts)] if accounts else None
            profile_path = profile_paths[i % len(profile_paths)] if profile_paths else None
            
            use_specific = use_specific_profile if n == 1 else False
            
            t = threading.Thread(target=wrapper, args=(acc, head, profile_path, use_specific), daemon=True)
            t.start()
            threads.append(t)

        # Nếu bật tự động sắp xếp và không ở chế độ headless, đợi một chút rồi sắp xếp
        if arrange_auto_var.get() and not head:
            def auto_arrange():
                time.sleep(3)  # Đợi 3 giây để các driver được tạo
                arrange_windows_auto()
            
            threading.Thread(target=auto_arrange, daemon=True).start()

        def chk():
            if all(not t.is_alive() for t in threads):
                progress_label.config(text="Hoàn tất tất cả")
                messagebox.showinfo(current_language["success"], "Tất cả script đã chạy xong.")
            else:
                root.after(500, chk)
        root.after(500, chk)
    except Exception as e:
        logging.error(f"Lỗi khi chạy multithread: {e}")
        messagebox.showerror(current_language["error"], str(e))

def schedule_run():
    try:
        h = int(hour_entry.get())
        m = int(minute_entry.get())
        now = datetime.now()
        if not (0 <= h < 24 and 0 <= m < 60):
            messagebox.showerror(current_language["error"], "Giờ hoặc phút không hợp lệ.")
            return
        runt = now.replace(hour=h, minute=m, second=0, microsecond=0)
        if runt <= now:
            runt = runt.replace(day=now.day + 1)
        delay = (runt - now).total_seconds()
        sch = sched.scheduler(time.time, time.sleep)
        sch.enter(delay, 1, run_multithread)
        threading.Thread(target=sch.run, daemon=True).start()
        messagebox.showinfo(current_language["success"], f"Script sẽ chạy lúc {h:02d}:{m:02d}")
    except Exception as e:
        logging.error(f"Lỗi khi hẹn giờ: {e}")
        messagebox.showerror(current_language["error"], f"Giờ không hợp lệ hoặc lỗi: {e}")

def save_xpath_groups():
    try:
        with open("xpath_groups.json", "w", encoding="utf-8") as f:
            json.dump(random_xpath_groups, f, ensure_ascii=False, indent=2)
        logging.info("Đã lưu nhóm XPath")
        messagebox.showinfo(current_language["success"], current_language["xpath_groups_saved"])
    except Exception as e:
        logging.error(f"Lỗi khi lưu nhóm XPath: {e}")

def load_xpath_groups(silent=False):
    try:
        if os.path.exists("xpath_groups.json"):
            with open("xpath_groups.json", "r", encoding="utf-8") as f:
                loaded = json.load(f)
                for key in random_xpath_groups.keys():
                    if key in loaded:
                        random_xpath_groups[key] = loaded[key]
            logging.info("Đã tải nhóm XPath từ file")
            if not silent:
                messagebox.showinfo(current_language["success"], current_language["xpath_groups_loaded"])
        else:
            logging.info("Không tìm thấy file xpath_groups.json")
            if not silent:
                messagebox.showinfo(current_language["info"], "Không tìm thấy file xpath_groups.json")
    except Exception as e:
        logging.error(f"Lỗi khi tải nhóm XPath: {e}")

def clear_all_xpath_groups():
    try:
        if messagebox.askyesno(current_language["confirm_delete"], 
                              "Bạn có chắc chắn muốn xóa tất cả XPath trong tất cả nhóm?"):
            for key in random_xpath_groups.keys():
                random_xpath_groups[key].clear()
            messagebox.showinfo(current_language["success"], current_language["xpath_groups_cleared"])
    except Exception as e:
        logging.error(f"Lỗi khi xóa nhóm XPath: {e}")

def open_random_xpath_popup():
    try:
        popup = tk.Toplevel(root)
        popup.title(current_language["manage_xpath_groups"])
        popup.geometry("850x650")
        
        func_frame = tk.Frame(popup)
        func_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(func_frame, text=current_language["save_xpath_groups"], 
                 command=save_xpath_groups, bg="#27ae60", fg="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(func_frame, text=current_language["load_xpath_groups"], 
                 command=load_xpath_groups, bg="#3498db", fg="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(func_frame, text=current_language["clear_all_groups"], 
                 command=clear_all_xpath_groups, bg="#e74c3c", fg="white").pack(side=tk.LEFT, padx=5)
        
        notebook_groups = ttk.Notebook(popup)
        notebook_groups.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        group_names = {
            "group_1": current_language["xpath_group_1"],
            "group_2": current_language["xpath_group_2"], 
            "group_3": current_language["xpath_group_3"],
            "group_5": current_language["xpath_group_5"],
            "group_10": current_language["xpath_group_10"],
            "group_custom": current_language["xpath_group_custom"]
        }
        
        for group_key, group_label in group_names.items():
            tab = ttk.Frame(notebook_groups)
            notebook_groups.add(tab, text=group_label)
            
            label_text = ""
            if group_key == "group_1":
                label_text = "Nhóm 1 - Sử dụng cho 'Click Random 1 XPath'\nThêm ít nhất 1 XPath vào đây"
            elif group_key == "group_2":
                label_text = "Nhóm 2 - Sử dụng cho 'Click Random 2 XPath'\nThêm ít nhất 2 XPath vào đây"
            elif group_key == "group_3":
                label_text = "Nhóm 3 - Sử dụng cho 'Click Random 3 XPath'\nThêm ít nhất 3 XPath vào đây"
            elif group_key == "group_5":
                label_text = "Nhóm 5 - Sử dụng cho 'Click Random 5 XPath'\nThêm ít nhất 5 XPath vào đây"
            elif group_key == "group_10":
                label_text = "Nhóm 10 - Sử dụng cho 'Click Random 10 XPath'\nThêm ít nhất 10 XPath vào đây"
            else:
                label_text = "Nhóm Custom - Sử dụng cho 'Click Random XPath (tùy chỉnh)'\nThêm XPath vào đây"
            
            tk.Label(tab, text=label_text, font=('Arial', 10), 
                    fg='#2c3e50', justify=tk.LEFT).pack(pady=10)
            
            list_frame = tk.Frame(tab)
            list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
            
            listbox = tk.Listbox(list_frame, height=10, font=('Consolas', 9))
            listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=listbox.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            listbox.config(yscrollcommand=scrollbar.set)
            
            for xpath in random_xpath_groups[group_key]:
                listbox.insert(tk.END, xpath)
            
            button_frame = tk.Frame(tab)
            button_frame.pack(fill=tk.X, padx=10, pady=10)
            
            def add_xpath_to_group(group=group_key, lb=listbox):
                xpath = simpledialog.askstring("Thêm XPath", 
                    f"Nhập XPath để thêm vào nhóm {group}:")
                if xpath and xpath.strip():
                    random_xpath_groups[group].append(xpath.strip())
                    lb.insert(tk.END, xpath.strip())
                    messagebox.showinfo(current_language["success"], f"Đã thêm XPath vào nhóm {group}")
            
            def delete_xpath_from_group(group=group_key, lb=listbox):
                selection = lb.curselection()
                if not selection:
                    messagebox.showwarning(current_language["warning"], current_language["no_xpath_selected"])
                    return
                
                idx = selection[0]
                xpath = lb.get(idx)
                if messagebox.askyesno(current_language["confirm_delete"], 
                                      f"Bạn có chắc muốn xóa XPath này?\n{xpath}"):
                    random_xpath_groups[group].pop(idx)
                    lb.delete(idx)
            
            tk.Button(button_frame, text="➕ Thêm XPath", 
                     command=lambda g=group_key, lb=listbox: add_xpath_to_group(g, lb),
                     bg="#3498db", fg="white").pack(side=tk.LEFT, padx=5)
            
            tk.Button(button_frame, text="🗑️ Xóa XPath đã chọn", 
                     command=lambda g=group_key, lb=listbox: delete_xpath_from_group(g, lb),
                     bg="#e74c3c", fg="white").pack(side=tk.LEFT, padx=5)
            
            count_label = tk.Label(tab, 
                text=f"Số lượng XPath trong nhóm: {len(random_xpath_groups[group_key])}",
                font=('Arial', 9, 'bold'), fg='#27ae60')
            count_label.pack(pady=5)
        
        tk.Button(popup, text=current_language["close_button"], command=popup.destroy,
                 bg="#7f8c8d", fg="white", width=20).pack(pady=10)
        
    except Exception as e:
        logging.error(f"Lỗi khi mở popup XPath random theo nhóm: {e}")

def arrange_windows_now():
    """Hàm sắp xếp cửa sổ ngay lập tức"""
    try:
        if not active_drivers:
            messagebox.showwarning("Cảnh báo", "Không có cửa sổ Chrome nào để sắp xếp")
            return
        
        cols = int(arrange_columns_entry.get())
        rows = int(arrange_rows_entry.get())
        gap = int(arrange_gap_entry.get())
        
        if cols <= 0 or rows <= 0:
            messagebox.showerror("Lỗi", "Số cột và số hàng phải lớn hơn 0")
            return
        
        screen_width, screen_height = pyautogui.size()
        window_width = (screen_width - (cols + 1) * gap) // cols
        window_height = (screen_height - (rows + 1) * gap) // rows
        
        arranged_count = 0
        for i, driver in enumerate(active_drivers):
            if i >= cols * rows:
                break
            
            try:
                row = i // cols
                col = i % cols
                
                x = col * (window_width + gap) + gap
                y = row * (window_height + gap) + gap
                
                driver.set_window_position(x, y)
                driver.set_window_size(window_width, window_height)
                
                arranged_count += 1
                logging.info(f"Đã sắp xếp cửa sổ {i+1} tại ({x}, {y})")
                
            except Exception as e:
                logging.error(f"Không thể sắp xếp cửa sổ {i+1}: {e}")
        
        if arranged_count > 0:
            messagebox.showinfo(current_language["success"], 
                              f"{current_language['arrange_success']}: {arranged_count} cửa sổ")
        else:
            messagebox.showwarning("Cảnh báo", "Không có cửa sổ Chrome nào để sắp xếp")
                    
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ")
    except Exception as e:
        logging.error(f"Lỗi khi sắp xếp cửa sổ: {e}")

def mo_chrome_py():
    def run_script():
        subprocess.run([sys.executable, "chromeinstall.py"])
    threading.Thread(target=run_script).start()

def update_client():
    def run_script():
        subprocess.run([sys.executable, "updateclient.py"])
    threading.Thread(target=run_script).start()

# ================== GUI PHẦN ==================

# Tạo cửa sổ chính
root = tb.Window(themename="darkly")
root.title("🔧 Auto Chrome Script")
root.geometry("1100x950+50+50")
root.minsize(1100, 700)

# Khởi tạo các biến Tkinter
use_specific_profile_var = tk.BooleanVar(value=False)
headless_var = tk.BooleanVar()
auto_quit_var = tk.BooleanVar(value=True)
auto_create_profiles_var = tk.BooleanVar(value=True)
delete_profiles_after_run_var = tk.BooleanVar(value=False)
auto_load_accounts_var = tk.BooleanVar(value=True)
arrange_auto_var = tk.BooleanVar(value=False)
selected_field_var = tk.StringVar()
selected_field_var.set("Chọn trường")
selected_field_var_tab2 = tk.StringVar()
selected_field_var_tab2.set("Chọn trường")

# Tạo style
style = tb.Style()
style.configure("primary.TButton", font=('Arial', 10, 'bold'))
style.configure("success.TButton", font=('Arial', 10, 'bold'))
style.configure("info.TButton", font=('Arial', 10, 'bold'))
style.configure("warning.TButton", font=('Arial', 10, 'bold'))
style.configure("danger.TButton", font=('Arial', 10, 'bold'))

# Main container
main_container = tb.Frame(root)
main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ================== HEADER ==================
header = tb.Frame(main_container, bootstyle="primary", padding=15)
header.pack(fill=tk.X, pady=(0, 10))

header_left = tb.Frame(header)
header_left.pack(side=tk.LEFT)

tb.Label(
    header_left,
    text="🔧 AUTO CHROME SCRIPT HIEUSU66",
    font=('Arial', 20, 'bold'),
    bootstyle="default"
).pack(side=tk.LEFT, padx=(0, 20))

def toggle_theme():
    global current_theme
    if current_theme == "litera":
        change_theme("darkly")
        theme_btn.config(text=current_language["light_mode"])
    else:
        change_theme("litera")
        theme_btn.config(text=current_language["dark_mode"])

theme_btn = tb.Button(
    header,
    text=current_language["dark_mode"],
    bootstyle="info-outline",
    command=toggle_theme,
    width=15
)
theme_btn.pack(side=tk.RIGHT, padx=5)

language_frame = tb.Frame(header)
language_frame.pack(side=tk.RIGHT, padx=20)

tb.Label(
    language_frame,
    text=current_language["language_label"],
    font=('Arial', 10)
).pack(side=tk.LEFT, padx=(0, 5))

language_var = tk.StringVar(value=current_language["language_option_vn"])
language_combo = tb.Combobox(
    language_frame,
    textvariable=language_var,
    values=[current_language["language_option_vn"], current_language["language_option_en"]],
    width=15,
    state="readonly"
)
language_combo.pack(side=tk.LEFT)

# ================== NOTEBOOK (TABS) ==================
notebook = tb.Notebook(main_container)
notebook.pack(fill=tk.BOTH, expand=True)

# ================== TAB DASHBOARD ==================
dashboard_tab = tb.Frame(notebook)
notebook.add(dashboard_tab, text="📊 Dashboard")

dashboard_title = tb.Label(
    dashboard_tab,
    text=current_language["dashboard"],
    font=('Arial', 18, 'bold'),
    bootstyle="primary"
)
dashboard_title.pack(pady=(10, 20))

# Cards container
cards_container = tb.Frame(dashboard_tab)
cards_container.pack(fill=tk.X, padx=20, pady=10)

def create_dashboard_card(parent, title, value, icon, color):
    # Card chính
    card = tb.Frame(parent, bootstyle=color, padding=20)

    # Khung icon + title (ăn theo màu card)
    icon_frame = tb.Frame(card, bootstyle=color)
    icon_frame.pack(anchor='w')

    # Icon
    tb.Label(
        icon_frame,
        text=icon,
        font=('Arial', 24),
        bootstyle=f"{color}-inverse"
    ).pack(side=tk.LEFT, padx=(0, 10))

    # Title
    title_label = tb.Label(
        icon_frame,
        text=title,
        font=('Arial', 10, 'bold'),
        bootstyle=f"{color}-inverse"
    )
    title_label.pack(side=tk.LEFT)

    # Value
    value_label = tb.Label(
        card,
        text=value,
        font=('Arial', 24, 'bold'),
        bootstyle=f"{color}-inverse"
    )
    value_label.pack(pady=(10, 0))

    return card, value_label, title_label


threads_card, threads_card_value, threads_card_title = create_dashboard_card(
    cards_container, 
    current_language["running_threads"], 
    "0", 
    "🔢", 
    "info"
)
threads_card.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

steps_card, steps_card_value, steps_card_title = create_dashboard_card(
    cards_container,
    current_language["total_steps"],
    "0",
    "📝",
    "success"
)
steps_card.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

profiles_card, profiles_card_value, profiles_card_title = create_dashboard_card(
    cards_container,
    current_language["profiles_count"],
    "0",
    "👤",
    "warning"
)
profiles_card.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

accounts_card, accounts_card_value, accounts_card_title = create_dashboard_card(
    cards_container,
    current_language["accounts_count"],
    "0",
    "👥",
    "danger"
)
accounts_card.grid(row=0, column=3, padx=10, pady=10, sticky='nsew')

for i in range(4):
    cards_container.columnconfigure(i, weight=1)

def update_dashboard_stats():
    try:
        threads_value = threads_entry.get() or "0"
        threads_card_value.config(text=threads_value)
        steps_card_value.config(text=str(len(script_steps)))
        profiles_card_value.config(text=str(len(list_profiles())))
        accounts_card_value.config(text=str(len(accounts)))
    except Exception as e:
        logging.error(f"Lỗi khi cập nhật dashboard stats: {e}")

# Quick Actions
quick_actions_frame = tb.LabelFrame(
    dashboard_tab,
    text=current_language["quick_actions"],
    padding=20,
    bootstyle="primary"
)
quick_actions_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

quick_actions_label = tb.Label(
    quick_actions_frame,
    text=current_language["quick_actions"],
    font=('Arial', 12, 'bold')
)
quick_actions_label.pack(anchor='w', pady=(0, 10))

quick_actions_grid = tb.Frame(quick_actions_frame)
quick_actions_grid.pack(fill=tk.BOTH, expand=True)

dashboard_buttons = {}

button_defs = [
    ("refresh", "🔄", current_language["refresh"], "info", refresh_script_list),
    ("view_profiles", "📂", current_language["view_profiles"], "info", show_profiles),
    ("delete_profiles", "🗑️", current_language["delete_profiles"], "danger", clear_profiles),
    ("install_chrome", "⚙️", current_language["install_chromedriver"], "warning", mo_chrome_py),
    ("update_app", "🔄", current_language["update_app"], "warning", update_client),
    ("guide", "❓", current_language["guide"], "info", show_guide),
    ("show_steps", "📋", current_language["show_steps_window"], "success", show_steps_window),
    ("arrange_windows", "📐", current_language["arrange_windows"], "primary", lambda: notebook.select(3)),
]

for i, (key, icon, text, style_name, command) in enumerate(button_defs):
    row, col = divmod(i, 4)
    btn = tb.Button(
        quick_actions_grid,
        text=f"{icon} {text}",
        bootstyle=style_name,
        command=command,
        padding=10,
        width=20
    )
    btn.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
    dashboard_buttons[key] = btn

for i in range(4):
    quick_actions_grid.columnconfigure(i, weight=1)

# System Status
system_status_frame = tb.LabelFrame(
    dashboard_tab,
    text=current_language["system_status"],
    padding=20,
    bootstyle="secondary"
)
system_status_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

system_status_label = tb.Label(
    system_status_frame,
    text=current_language["system_status"],
    font=('Arial', 12, 'bold')
)
system_status_label.pack(anchor='w', pady=(0, 10))

status_grid = tb.Frame(system_status_frame)
status_grid.pack(fill=tk.X)

status_items = [
    ("Chrome Driver", "✅ Sẵn sàng", "success"),
    ("Selenium", "✅ Đã cài đặt", "success"),
    ("Python", f"✅ {sys.version.split()[0]}", "success"),
    ("Tài khoản", f"📊 {len(accounts)} tài khoản", "info"),
]

for i, (label, value, style_name) in enumerate(status_items):
    frame = tb.Frame(status_grid)
    frame.grid(row=i//2, column=i%2, padx=20, pady=10, sticky='w')
    
    tb.Label(frame, text=label, font=('Arial', 10, 'bold')).pack(anchor='w')
    tb.Label(frame, text=value, bootstyle=style_name, font=('Arial', 10)).pack(anchor='w')

# ================== TAB SCRIPT MANAGEMENT ==================
tab1 = tb.Frame(notebook)
notebook.add(tab1, text="📝 Quản lý Script")

tab1.columnconfigure(0, weight=1)
tab1.columnconfigure(1, weight=1)
tab1.rowconfigure(1, weight=1)

tb.Label(tab1, text=current_language["saved_scripts"], 
        font=('Arial', 11, 'bold')).grid(row=0, column=0, sticky='w', pady=(10, 5), padx=10)

saved_scripts_frame = tb.Frame(tab1)
saved_scripts_frame.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

script_option_listbox = tk.Listbox(saved_scripts_frame, height=20, bg='white', 
                                  font=('Consolas', 9), selectbackground='#3498db')
script_option_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_left = ttk.Scrollbar(saved_scripts_frame, orient="vertical", 
                              command=script_option_listbox.yview)
scrollbar_left.pack(side=tk.RIGHT, fill=tk.Y)
script_option_listbox.config(yscrollcommand=scrollbar_left.set)

tb.Label(tab1, text=current_language["current_steps"], 
        font=('Arial', 11, 'bold')).grid(row=0, column=1, sticky='w', pady=(10, 5), padx=10)

current_steps_frame = tb.Frame(tab1)
current_steps_frame.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')

script_listbox = tk.Listbox(current_steps_frame, height=20, bg='white',
                           font=('Consolas', 9), selectbackground='#27ae60')
script_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_right = ttk.Scrollbar(current_steps_frame, orient="vertical", 
                               command=script_listbox.yview)
scrollbar_right.pack(side=tk.RIGHT, fill=tk.Y)
script_listbox.config(yscrollcommand=scrollbar_right.set)

script_buttons_frame = tb.Frame(tab1)
script_buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

edit_step_btn = tb.Button(script_buttons_frame, text="✏️ Chỉnh sửa",
                         bootstyle="warning", command=edit_step)
edit_step_btn.pack(side=tk.LEFT, padx=5)

delete_step_btn = tb.Button(script_buttons_frame, text="🗑️ Xóa bước",
                           bootstyle="danger", command=delete_step)
delete_step_btn.pack(side=tk.LEFT, padx=5)

save_script_btn = tb.Button(script_buttons_frame, text="💾 Lưu Script",
                           bootstyle="success", command=save_script)
save_script_btn.pack(side=tk.LEFT, padx=5)

# ================== TAB SETTINGS ==================
tab2 = tb.Frame(notebook)
notebook.add(tab2, text="⚙️ Thêm bước & Cài đặt")

paned_window = tk.PanedWindow(tab2, orient=tk.HORIZONTAL, sashrelief=tk.RAISED, sashwidth=5)
paned_window.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

left_pane = tb.Frame(paned_window)
paned_window.add(left_pane, width=400)

tb.Label(left_pane, text="📝 Các bước Script:", 
        font=('Arial', 11, 'bold')).pack(fill=tk.X, pady=(10, 5), padx=10)

steps_list_frame = tb.Frame(left_pane)
steps_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

tab2_steps_listbox = tk.Listbox(steps_list_frame, height=20, bg='white',
                               font=('Consolas', 9), selectbackground='#27ae60')
tab2_steps_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

steps_scrollbar = ttk.Scrollbar(steps_list_frame, orient="vertical", 
                               command=tab2_steps_listbox.yview)
steps_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tab2_steps_listbox.config(yscrollcommand=steps_scrollbar.set)

right_pane = tb.Frame(paned_window)
paned_window.add(right_pane, width=500)

add_step_frame = tb.LabelFrame(right_pane, text="➕ Thêm bước mới", 
                               padding=15, bootstyle="primary")
add_step_frame.pack(fill=tk.X, padx=10, pady=10)

action_row = tb.Frame(add_step_frame)
action_row.pack(fill=tk.X, pady=5)

action_label = tb.Label(action_row, text="Hành động:", width=10)
action_label.pack(side=tk.LEFT, padx=5)

action_combo = tb.Combobox(
    action_row,
    values=[
        "Mở URL",
        "Ngủ",
        "Click XPath",
        "Gửi ký tự (XPath|Text)",
        "Swipe (Hướng|Pixel đầu|Pixel cuối)",
        "Click Full XPath",
        "Tìm kiếm hình ảnh",
        "Chụp màn hình và lưu template",
        "Tùy chỉnh",
        "Tìm và Nhập (Text|Value)",
        "Tìm và Nhập vào Phần Tử Gần Kề (Text|Value|Position|ElementType)",
        current_language["click_random_xpath_1"],
        current_language["click_random_xpath_2"],
        current_language["click_random_xpath_3"],
        current_language["click_random_xpath_5"],
        current_language["click_random_xpath_10"],
        current_language["click_random_xpath_custom"]
    ],
    width=25,
    state="readonly"
)
action_combo.pack(side=tk.LEFT, padx=5)

value_row = tb.Frame(add_step_frame)
value_row.pack(fill=tk.X, pady=5)

value_label = tb.Label(value_row, text="Giá trị:", width=10)
value_label.pack(side=tk.LEFT, padx=5)

value_entry = tb.Entry(value_row, width=30)
value_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

buttons_row = tb.Frame(add_step_frame)
buttons_row.pack(fill=tk.X, pady=10)

add_field_btn = tb.Button(buttons_row, text="➕ Thêm trường",
                         bootstyle="info", command=lambda: None)
add_field_btn.pack(side=tk.LEFT, padx=5)

load_accounts_btn = tb.Button(buttons_row, text="📄 Tải tài khoản",
                             bootstyle="info", command=load_accounts_from_text)
load_accounts_btn.pack(side=tk.LEFT, padx=5)

random_xpath_btn = tb.Button(buttons_row, text="XPath Random",
                           bootstyle="warning", command=open_random_xpath_popup)
random_xpath_btn.pack(side=tk.LEFT, padx=5)

add_step_btn = tb.Button(buttons_row, text="➕ Thêm bước",
                        bootstyle="success", command=add_step)
add_step_btn.pack(side=tk.RIGHT, padx=5)

run_settings_frame = tb.LabelFrame(right_pane, text="⚡ Cài đặt chạy", 
                                   padding=15, bootstyle="secondary")
run_settings_frame.pack(fill=tk.X, padx=10, pady=10)

# Sửa các checkbox bằng tk.Checkbutton thay vì tb.Checkbutton
auto_load_checkbox = tk.Checkbutton(
    run_settings_frame,
    text="📥 Tự động tải account.txt",
    variable=auto_load_accounts_var,
    bg='#2c3e50', fg='white',
    selectcolor='#3498db',
    font=('Arial', 10),
    activebackground='#2c3e50',
    activeforeground='white'
)
auto_load_checkbox.pack(anchor='w', pady=5)

settings_row1 = tb.Frame(run_settings_frame)
settings_row1.pack(fill=tk.X, pady=5)

threads_label = tb.Label(settings_row1, text="Số luồng:", width=12)
threads_label.pack(side=tk.LEFT, padx=5)

threads_entry = tb.Entry(settings_row1, width=8)
threads_entry.insert(0, "1")
threads_entry.pack(side=tk.LEFT, padx=5)

chrome_size_label = tb.Label(settings_row1, text="Kích thước Chrome:", width=18)
chrome_size_label.pack(side=tk.LEFT, padx=5)

chrome_width = tb.Entry(settings_row1, width=6)
chrome_width.insert(0, "1200")
chrome_width.pack(side=tk.LEFT, padx=2)

tb.Label(settings_row1, text="x").pack(side=tk.LEFT)

chrome_height = tb.Entry(settings_row1, width=6)
chrome_height.insert(0, "800")
chrome_height.pack(side=tk.LEFT, padx=2)

settings_row2 = tb.Frame(run_settings_frame)
settings_row2.pack(fill=tk.X, pady=5)

hide_chrome_check = tk.Checkbutton(
    settings_row2,
    text="Ẩn Chrome (headless)",
    variable=headless_var,
    bg='#2c3e50', fg='white',
    selectcolor='#3498db',
    font=('Arial', 10),
    activebackground='#2c3e50',
    activeforeground='white'
)
hide_chrome_check.pack(side=tk.LEFT, padx=10)

auto_close_check = tk.Checkbutton(
    settings_row2,
    text="Tự đóng Chrome khi xong",
    variable=auto_quit_var,
    bg='#2c3e50', fg='white',
    selectcolor='#3498db',
    font=('Arial', 10),
    activebackground='#2c3e50',
    activeforeground='white'
)
auto_close_check.pack(side=tk.LEFT, padx=10)

settings_row3 = tb.Frame(run_settings_frame)
settings_row3.pack(fill=tk.X, pady=5)

auto_create_check = tk.Checkbutton(
    settings_row3,
    text="Tạo profile tự động",
    variable=auto_create_profiles_var,
    bg='#2c3e50', fg='white',
    selectcolor='#3498db',
    font=('Arial', 10),
    activebackground='#2c3e50',
    activeforeground='white'
)
auto_create_check.pack(side=tk.LEFT, padx=10)

delete_profiles_check = tk.Checkbutton(
    settings_row3,
    text="Xóa profile sau khi chạy",
    variable=delete_profiles_after_run_var,
    bg='#2c3e50', fg='white',
    selectcolor='#3498db',
    font=('Arial', 10),
    activebackground='#2c3e50',
    activeforeground='white'
)
delete_profiles_check.pack(side=tk.LEFT, padx=10)

settings_row4 = tb.Frame(run_settings_frame)
settings_row4.pack(fill=tk.X, pady=10)

schedule_label = tb.Label(settings_row4, text="Hẹn giờ chạy:", width=12)
schedule_label.pack(side=tk.LEFT, padx=5)

hour_label = tb.Label(settings_row4, text="Giờ:", width=4)
hour_label.pack(side=tk.LEFT)

hour_entry = tb.Entry(settings_row4, width=4)
hour_entry.insert(0, "15")
hour_entry.pack(side=tk.LEFT, padx=2)

minute_label = tb.Label(settings_row4, text="Phút:", width=4)
minute_label.pack(side=tk.LEFT)

minute_entry = tb.Entry(settings_row4, width=4)
minute_entry.insert(0, "30")
minute_entry.pack(side=tk.LEFT, padx=2)

schedule_btn = tb.Button(settings_row4, text="🕑 Hẹn giờ",
                        bootstyle="warning", command=schedule_run)
schedule_btn.pack(side=tk.LEFT, padx=20)

settings_row5 = tb.Frame(run_settings_frame)
settings_row5.pack(fill=tk.X, pady=5)

use_profile_checkbox = tk.Checkbutton(
    settings_row5,
    text="Chọn profile để chạy",
    variable=use_specific_profile_var,
    bg='#2c3e50', fg='white',
    selectcolor='#3498db',
    font=('Arial', 10),
    activebackground='#2c3e50',
    activeforeground='white'
)

run_button_frame = tb.Frame(right_pane)
run_button_frame.pack(fill=tk.X, padx=10, pady=20)

run_script_btn = tb.Button(
    run_button_frame,
    text="▶️ CHẠY SCRIPT",
    bootstyle="success",
    command=run_multithread,
    padding=(30, 15),
    width=20
)
run_script_btn.pack()

progress_frame = tb.Frame(right_pane)
progress_frame.pack(fill=tk.X, padx=10, pady=10)

progress_label = tb.Label(progress_frame, text="Sẵn sàng...")
progress_label.pack(anchor="w")

progress_var = tk.IntVar()
progressbar = tb.Progressbar(
    progress_frame,
    variable=progress_var,
    maximum=100,
    bootstyle="success-striped",
    length=400
)
progressbar.pack(fill=tk.X, pady=5)

# ================== TAB ARRANGE WINDOWS ==================
tab3 = tb.Frame(notebook)
notebook.add(tab3, text="🪟 Sắp xếp cửa sổ")

# Tạo layout chính cho tab 3
arrange_main_frame = tb.Frame(tab3)
arrange_main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Tiêu đề
arrange_settings_label = tb.Label(
    arrange_main_frame,
    text=current_language["arrange_settings_title"],
    font=('Arial', 16, 'bold'),
    bootstyle="primary"
)
arrange_settings_label.pack(pady=(0, 20))

# Khung cấu hình
arrange_config_frame = tb.LabelFrame(
    arrange_main_frame,
    text="Cấu hình sắp xếp",
    padding=20,
    bootstyle="secondary"
)
arrange_config_frame.pack(fill=tk.X, pady=(0, 20))

# Hàng 1: Số cột
arrange_row1 = tb.Frame(arrange_config_frame)
arrange_row1.pack(fill=tk.X, pady=10)

arrange_columns_label = tb.Label(arrange_row1, text=current_language["arrange_columns"], width=15, anchor='w')
arrange_columns_label.pack(side=tk.LEFT, padx=10)

arrange_columns_entry = tb.Entry(arrange_row1, width=10)
arrange_columns_entry.insert(0, "3")
arrange_columns_entry.pack(side=tk.LEFT)

# Hàng 2: Số hàng
arrange_row2 = tb.Frame(arrange_config_frame)
arrange_row2.pack(fill=tk.X, pady=10)

arrange_rows_label = tb.Label(arrange_row2, text=current_language["arrange_rows"], width=15, anchor='w')
arrange_rows_label.pack(side=tk.LEFT, padx=10)

arrange_rows_entry = tb.Entry(arrange_row2, width=10)
arrange_rows_entry.insert(0, "2")
arrange_rows_entry.pack(side=tk.LEFT)

# Hàng 3: Khoảng cách
arrange_row3 = tb.Frame(arrange_config_frame)
arrange_row3.pack(fill=tk.X, pady=10)

arrange_gap_label = tb.Label(arrange_row3, text=current_language["arrange_gap"], width=15, anchor='w')
arrange_gap_label.pack(side=tk.LEFT, padx=10)

arrange_gap_entry = tb.Entry(arrange_row3, width=10)
arrange_gap_entry.insert(0, "10")
arrange_gap_entry.pack(side=tk.LEFT)

# Khung tự động sắp xếp
arrange_auto_frame = tb.LabelFrame(
    arrange_main_frame,
    text="Tự động sắp xếp",
    padding=20,
    bootstyle="info"
)
arrange_auto_frame.pack(fill=tk.X, pady=(0, 20))

arrange_auto_checkbox = tk.Checkbutton(
    arrange_auto_frame,
    text=current_language["arrange_auto"],
    variable=arrange_auto_var,
    bg='#2c3e50', fg='white',
    selectcolor='#3498db',
    font=('Arial', 11, 'bold'),
    activebackground='#2c3e50',
    activeforeground='white'
)
arrange_auto_checkbox.pack(anchor='w', pady=(0, 10))

arrange_auto_desc_label = tk.Label(
    arrange_auto_frame,
    text=current_language["arrange_auto_desc"],
    font=('Arial', 10),
    wraplength=500
)
arrange_auto_desc_label.pack(anchor='w', pady=(0, 10))

# Nút sắp xếp ngay
arrange_button_frame = tb.Frame(arrange_main_frame)
arrange_button_frame.pack(fill=tk.X, pady=(0, 20))

arrange_now_btn = tb.Button(
    arrange_button_frame,
    text=current_language["arrange_button"],
    bootstyle="primary",
    command=arrange_windows_now,
    padding=(20, 15),
    width=20
)
arrange_now_btn.pack()

# Ghi chú
arrange_notes_frame = tb.Frame(arrange_main_frame)
arrange_notes_frame.pack(fill=tk.X)

# Sửa lỗi ở đây: thay tb.Label bằng tk.Label và sử dụng foreground thay vì fg
arrange_notes_label = tk.Label(
    arrange_notes_frame,
    text=current_language["arrange_notes"],
    font=('Arial', 9),
    foreground='#7f8c8d',
    wraplength=500,
    justify=tk.LEFT
)
arrange_notes_label.pack(pady=10)

# ================== FLOATING ACTION BUTTON (RUN SCRIPT) ==================
def create_floating_action_button(parent, command, icon="▶️", tooltip="Run Script"):
    fab = tb.Button(
        parent,
        text=icon,
        bootstyle="danger",  # Màu đỏ nổi bật
        command=command,
        padding=(20, 20),
        cursor="hand2"
    )
    fab.place(relx=0.97, rely=0.95, anchor=tk.CENTER)
    
    # Thêm hiệu ứng hover
    def on_enter(e):
        fab.configure(bootstyle="danger-outline")
    
    def on_leave(e):
        fab.configure(bootstyle="danger")
    
    fab.bind("<Enter>", on_enter)
    fab.bind("<Leave>", on_leave)
    
    return fab

# Tạo nút chạy script nổi ở góc dưới bên phải
fab = create_floating_action_button(main_container, run_multithread, "▶️", current_language["run_script_quick"])

# ================== KHỞI TẠO ==================

# Tải cài đặt
settings = load_settings()
threads_entry.delete(0, tk.END)
threads_entry.insert(0, settings.get("threads", "1"))
chrome_width.delete(0, tk.END)
chrome_width.insert(0, settings.get("width", "1200"))
chrome_height.delete(0, tk.END)
chrome_height.insert(0, settings.get("height", "800"))
auto_create_profiles_var.set(settings.get("auto_create_profiles", "True") == "True")
delete_profiles_after_run_var.set(settings.get("delete_profiles_after_run", "False") == "True")
auto_load_accounts_var.set(settings.get("auto_load_accounts", "True") == "True")
arrange_auto_var.set(settings.get("arrange_auto", "False") == "True")
arrange_columns_entry.delete(0, tk.END)
arrange_columns_entry.insert(0, settings.get("arrange_columns", "3"))
arrange_rows_entry.delete(0, tk.END)
arrange_rows_entry.insert(0, settings.get("arrange_rows", "2"))
arrange_gap_entry.delete(0, tk.END)
arrange_gap_entry.insert(0, settings.get("arrange_gap", "10"))

# Đặt theme
theme = settings.get("theme", "darkly")
change_theme(theme)

# Đặt ngôn ngữ
lang = settings.get("language", "vi")
change_language(lang)

def on_language_change(event):
    lang_code = "vi" if language_var.get() == current_language["language_option_vn"] else "en"
    change_language(lang_code)
    save_settings()

language_combo.bind("<<ComboboxSelected>>", on_language_change)

# Bindings
script_option_listbox.bind("<<ListboxSelect>>", on_script_option_select)
script_listbox.bind("<Double-Button-1>", edit_step)
tab2_steps_listbox.bind("<Double-Button-1>", edit_step_tab2)

def update_profile_checkbox_visibility(*args):
    try:
        threads = int(threads_entry.get())
        if threads == 1:
            use_profile_checkbox.pack(side=tk.LEFT, padx=10)
        else:
            use_profile_checkbox.pack_forget()
            use_specific_profile_var.set(False)
    except:
        pass

threads_entry.bind('<KeyRelease>', update_profile_checkbox_visibility)
threads_entry.bind('<FocusOut>', update_profile_checkbox_visibility)

# Khởi tạo
refresh_script_list()
if auto_load_accounts_var.get():
    root.after(100, auto_load_accounts)
root.after(200, lambda: load_xpath_groups(silent=True))
root.after(100, update_profile_checkbox_visibility)
root.after(300, update_dashboard_stats)

def auto_update_dashboard():
    update_dashboard_stats()
    root.after(5000, auto_update_dashboard)

root.after(1000, auto_update_dashboard)

# Chạy ứng dụng
root.mainloop()