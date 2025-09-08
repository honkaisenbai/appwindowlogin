import os
import msvcrt
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()
users_db = {}  # Lưu tạm user/password, có thể thay bằng file sau này

def clear():
    os.system("cls")

def show_panel(title: str, message: str, style="bold cyan"):
    panel = Panel(
        Align.center(message, vertical="middle"),
        title=title,
        border_style=style,
        width=60,
        padding=(1,2)
    )
    console.print(panel)

def input_password(prompt="Password: "):
    console.print(prompt, end="", style="bold")
    password = ""
    while True:
        ch = msvcrt.getch()
        if ch in {b'\r', b'\n'}:
            print()
            break
        elif ch == b'\x08':  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        elif ch == b'\x03':  # Ctrl+C
            raise KeyboardInterrupt
        else:
            password += ch.decode('utf-8')
            print("*", end="", flush=True)
    return password

def login():
    while True:
        clear()
        show_panel("LOGIN", "Đăng nhập hệ thống\nNhập 0 để quay lại menu chính", style="bold cyan")
        username = input("Username: ").strip()
        if username == "0":  # Quay lại menu chính
            break
        password = input_password("Password: ")

        if username in users_db and users_db[username] == password:
            clear()
            show_panel("WELCOME", f"Xin chào [green]{username}[/green]! Bạn đã đăng nhập thành công ✅", style="bold magenta")
            input("\nNhấn Enter để tiếp tục...")
            break
        else:
            clear()
            show_panel("ERROR", "Username hoặc Password sai! Thử lại hoặc nhập 0 để quay lại menu.", style="bold red")
            input("\nNhấn Enter để thử lại...")

def signup():
    while True:
        clear()
        show_panel("SIGN UP", "Tạo tài khoản mới", style="bold green")
        username = input("Username: ").strip()
        if username in users_db:
            console.print("[red]Username đã tồn tại![/red]")
            input("Nhấn Enter để thử lại...")
            continue
        password = input_password("Password: ")
        users_db[username] = password
        console.print(f"[green]Tạo tài khoản thành công cho {username}![/green]")
        input("Nhấn Enter để quay lại menu...")
        break

def main_menu():
    while True:
        clear()
        show_panel("MAIN MENU", "1. Login\n2. Sign Up\n3. Exit", style="bold blue")
        choice = input("Chọn: ").strip()
        if choice == "1":
            login()
        elif choice == "2":
            signup()
        elif choice == "3":
            console.print("[bold yellow]Thoát chương trình[/bold yellow]")
            break
        else:
            console.print("[red]Lựa chọn không hợp lệ[/red]")
            input("Nhấn Enter để thử lại...")

if __name__ == "__main__":
    main_menu()
