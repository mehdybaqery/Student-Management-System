import tkinter as tk

class ThemeManager:
    def __init__(self):
        self.theme_mode = "light"
        self.colors = {
            "light": {
                "bg": "#f0f2f5",
                "card_bg": "#ffffff",
                "text": "#2c3e50",
                "accent": "#3498db",
                "secondary": "#ecf0f1",
                "success": "#27ae60",
                "warning": "#e74c3c"
            },
            "dark": {
                "bg": "#2c3e50",
                "card_bg": "#34495e",
                "text": "#ecf0f1",
                "accent": "#3498db",
                "secondary": "#46627f",
                "success": "#27ae60",
                "warning": "#e74c3c"
            }
        }

    def toggle_theme(self):
        """تغییر بین تم تاریک و روشن"""
        self.theme_mode = "dark" if self.theme_mode == "light" else "light"

    def get_current_theme(self):
        """دریافت تم فعلی"""
        return self.colors[self.theme_mode]

    def get_theme_mode(self):
        """دریافت حالت تم"""
        return self.theme_mode

    def apply_theme(self, root):
        """اعمال تم به ویجت‌ها"""
        colors = self.get_current_theme()
        root.configure(bg=colors['bg'])
        self._update_widget_colors(root, colors)

    def _update_widget_colors(self, widget, colors):
        """به‌روزرسانی رنگ ویجت‌ها"""
        try:
            if isinstance(widget, tk.Frame):
                widget.configure(bg=colors['card_bg'])
            elif isinstance(widget, tk.Label):
                if 'card' in str(widget.winfo_parent()):
                    widget.configure(bg=colors['card_bg'], fg=colors['text'])
                else:
                    widget.configure(bg=colors['bg'], fg=colors['text'])
            elif isinstance(widget, tk.Entry):
                widget.configure(bg='white', fg='black', insertbackground='black')
            elif isinstance(widget, tk.Text):
                widget.configure(bg='white', fg='black', insertbackground='black')
        except Exception:
            pass

        for child in widget.winfo_children():
            self._update_widget_colors(child, colors)