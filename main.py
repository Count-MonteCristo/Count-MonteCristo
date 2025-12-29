import gifos

# Initialize the Terminal object with cyberpunk aesthetic
t = gifos.Terminal(
    width=900,
    height=600,
    xpad=10,
    ypad=10,
    font_size=16,
)

# Set the frames per second
t.set_fps(15)

# Boot sequence with cyberpunk flair
def boot_line(text, row, delay=2, color="white", contin=False, save=False):
    t.set_txt_color(color)
    t.gen_text(text=text, row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")

def print_dots_done(row, delay=2):
    boot_line(".", row, delay, contin=True)
    boot_line(".", row, delay, contin=True)
    boot_line(".", row, delay, contin=True)
    boot_line(" [OK]", row, delay, contin=True, color="magenta")

# Cyberpunk boot sequence
boot_line("╔═══════════════════════════════════════════════════════╗", 1, delay=3, color="magenta")
boot_line("║     NEON PROTOCOL v3.7.2 :: INITIALIZING...         ║", 2, delay=3, color="cyan")
boot_line("╚═══════════════════════════════════════════════════════╝", 3, delay=3, color="magenta")
t.clone_frame(10)

boot_line(">> Jacking into the datasphere", 5, delay=3, color="cyan")
print_dots_done(5)
boot_line(">> Neural link established", 6, delay=3, color="cyan")
print_dots_done(6)
boot_line(">> Loading user profile: LUIS_NAVARRO.exe", 7, delay=3, color="cyan")
print_dots_done(7)
t.clone_frame(15)

t.clear_frame()

# Login sequence
t.gen_text(text="github@datasphere:~$ ", row_num=1, contin=False)
t.set_txt_color("cyan")
t.gen_text(text="login", row_num=1, contin=True)
t.set_txt_color("white")
t.clone_frame(5)

t.gen_text(text="Username: ", row_num=2, contin=False)
t.set_txt_color("magenta")
t.gen_typing_text(text="Count-MonteCristo", row_num=2, contin=True, speed=0.1)
t.set_txt_color("white")
t.clone_frame(10)

t.gen_text(text="Password: ", row_num=3)
t.set_txt_color("green")
t.gen_typing_text(text="**************", row_num=3, col_num=10, contin=True, speed=0.05)
t.set_txt_color("white")
t.clone_frame(15)

t.clear_frame()
boot_line(">> ACCESS GRANTED", 1, delay=5, color="green")
boot_line(">> Welcome to the Grid, Luis", 2, delay=5, color="cyan")
t.clone_frame(20)

t.clear_frame()

# Set cyberpunk prompt
t.set_prompt("\x1b[35mluis\x1b[39m@\x1b[36mdatasphere\x1b[39m:~$ ")

# whoami command
t.gen_prompt(1)
t.gen_typing_text(text="whoami", row_num=1, contin=True, speed=0.15)
t.clone_frame(5)
t.set_txt_color("magenta")
t.gen_text(text="Luis Navarro", row_num=2)
t.set_txt_color("cyan")
t.gen_text(text="Software Engineer | Full-Stack Developer | UX/UI Designer", row_num=3)
t.set_txt_color("white")
t.clone_frame(20)

# cat mission.txt
t.gen_prompt(5)
t.gen_typing_text(text="cat mission.txt", row_num=5, contin=True, speed=0.15)
t.clone_frame(5)
t.set_txt_color("white")
mission_text = """Building digital experiences that blend form and function.
From concept to deployment, I architect solutions that perform."""
t.gen_text(text=mission_text, row_num=6)
t.clone_frame(25)

# ls skills/
t.gen_prompt(9)
t.gen_typing_text(text="ls skills/", row_num=9, contin=True, speed=0.15)
t.clone_frame(5)
t.set_txt_color("cyan")
t.gen_text(text="frontend/    ", row_num=10, contin=False)
t.set_txt_color("magenta")
t.gen_text(text="backend/    ", row_num=10, contin=True)
t.set_txt_color("yellow")
t.gen_text(text="databases/    ", row_num=10, contin=True)
t.set_txt_color("green")
t.gen_text(text="design/    ", row_num=10, contin=True)
t.set_txt_color("blue")
t.gen_text(text="cloud/", row_num=10, contin=True)
t.set_txt_color("white")
t.clone_frame(20)

# cat stack.txt
t.gen_prompt(12)
t.gen_typing_text(text="cat stack.txt", row_num=12, contin=True, speed=0.15)
t.clone_frame(5)
stack_text = """\x1b[96m⚡ JavaScript, Python, React, Node.js, Express\x1b[0m
\x1b[95m🎨 HTML/CSS, Bootstrap, Material-UI, Figma\x1b[0m
\x1b[93m💾 MongoDB, MySQL, SQL Server, Oracle\x1b[0m
\x1b[94m☁️  Google Cloud, Azure\x1b[0m
\x1b[92m🔧 Git, VS Code, JWT, Mocha, Chai\x1b[0m"""
t.gen_text(text=stack_text, row_num=13)
t.clone_frame(30)

# echo $STATUS
t.gen_prompt(19)
t.gen_typing_text(text="echo $STATUS", row_num=19, contin=True, speed=0.15)
t.clone_frame(5)
t.set_txt_color("green")
t.gen_text(text="✓ ONLINE :: Available for collaboration", row_num=20)
t.gen_text(text="✓ Ready to build something extraordinary", row_num=21)
t.set_txt_color("white")
t.clone_frame(25)

# ./connect.sh
t.gen_prompt(23)
t.gen_typing_text(text="./connect.sh", row_num=23, contin=True, speed=0.15)
t.clone_frame(5)
connect_text = """\x1b[96mEstablishing uplink...\x1b[0m
\x1b[92m✓ GitHub     → github.com/Count-MonteCristo\x1b[0m

\x1b[95mConnection established. Let's build something amazing.\x1b[0m"""
t.gen_text(text=connect_text, row_num=24)
t.clone_frame(30)

# Final prompt with cursor
t.gen_prompt(32)
t.clone_frame(60)

# Disconnect sequence
t.gen_typing_text(text="exit", row_num=32, contin=True, speed=0.15)
t.clone_frame(10)
t.clear_frame()
boot_line(">> Disconnecting from mainframe...", 1, delay=5, color="cyan")
boot_line(">> Neural link terminated", 2, delay=5, color="magenta")
boot_line(">> Stay chrome, netrunner.", 3, delay=5, color="green")
t.clone_frame(20)

# Generate the GIF
t.gen_gif()
