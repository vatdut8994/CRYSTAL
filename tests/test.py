from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionOnScreenOnly
import subprocess

def get_active_app():
    return NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()

def get_selected_text():
    script = """
    tell application "System Events"
        try
            set selectedText to (get the clipboard)
            return selectedText
        on error
            return "No text selected"
        end try
    end tell
    """
    return subprocess.check_output(["osascript", "-e", script]).decode("utf-8").strip()

if __name__ == "__main__":
    print(f"Active App: {get_active_app()}")
    print(f"Selected Text: {get_selected_text()}")
