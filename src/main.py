#!/usr/bin/env python3
"""
Student Management System - Main Entry Point
"""

import tkinter as tk
from src.gui.app import ModernStudentRegistrationSystem

def main():
    
    root = tk.Tk()
    app = ModernStudentRegistrationSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
