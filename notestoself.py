from datetime import datetime
import textwrap as t_XSDSDDS_bullshitS_SDDSS, sys, os; 
def format(entry) -> str:
    _ = f"{('-' * 100)}\n"; b_e = f'\n{datetime.now()}\n'; b_e += _ ; 
    w_= t_XSDSDDS_bullshitS_SDDSS.TextWrapper(width = 100); 
    for line in w_.wrap(text=entry): b_e += f'{line}\n'; b_e += _ ; return b_e
if(len(sys.argv) <= 1): print("____________ERROR_____________"); exit(0)
with open(f"{os.path.expanduser('~')}/.notestoself", 'a+') as systemd:
    systemd.write(format(sys.argv[1]))
    systemd.close()
 