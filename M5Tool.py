print('Запуск... Пожалуйста, подождите')

try:

    import os, threading, time, subprocess, zipfile, re, json, random, webbrowser, sys

    try: 
        import serial.tools.list_ports
        import serial                                                                                                                                                                                                                                                                                                                                                                                             
    except:

        print('Installing a module Serial...')                                      

        os.system('pip install setuptools')
        os.system('pip install pyserial')

        try: 

            import serial
            import serial.tools.list_ports
            print('Serial is installed!')                                                                                                                                                                                                                                                                                                                                        

        except: 

            input('Cant install Serial!')

    try: import requests                                                                                                                                                                                                                                                                                                                                                                                             
    except:

        print('Installing a module Requests...')                                      

        os.system('pip install setuptools')
        os.system('pip install requests')

        try: 

            import requests
            print('Requests is installed!')                                                                                                                                                                                                                                                                                                                                        

        except: 

            input('Cant install Requests!')

    try: 
        from tkinter import messagebox, filedialog
        from customtkinter import *                                                                                                                                                                                                                                                                                                                                                                                           

    except:

        print('Installing a module CustomTkinter...')                                      

        os.system('pip install setuptools')
        os.system('pip install tkinter')
        os.system('pip install customtkinter')

        try: 

            from customtkinter import * 
            from tkinter import messagebox, filedialog

            print('CustomTkinter is installed!')                                                                                                                                                                                                                                                                                                                                        

        except: 

            input('Cant install CustomTkinter!')

    try:
        with open('translations.json', 'r', encoding='utf-8') as file:
            translations = json.load(file)
    except:
        print('Reinstalling translations...')
        try:
            r = requests.get('https://github.com/Sonys9/M5Tool/raw/refs/heads/main/translations.json')
            with open('translations.json', 'w', encoding='utf-8') as f:
                f.write(r.text)
            with open('translations.json', 'r', encoding='utf-8') as file:
                translations = json.load(file)
        except Exception as e:
            messagebox.showerror(title="M5Tool", message=f"Error when parsing translations: {e}, check your Internet connection!")
            sys.exit(0)
    def zanyat():

        try:

            s = serial.Serial(f'COM{portt}')
            add_log(translations['porttaken'][lang])
            while True:
                s.read()
                
        except:...

    installing = False

    if os.name == 'posix':username = os.getenv('USER') or os.getenv('LOGNAME')
    else:username = os.getenv('USERNAME')
    tempdir = f'C:\\Users\\{username}\\AppData\\Local\\Temp'

    def installfile(url, name, terminal=False):

        global installing, statuslabel

        if not terminal: threading.Thread(target=lambda: messagebox.showinfo('M5Tool', translations['installing..'][lang])).start()

        if installing: 
            if not terminal: threading.Thread(target=lambda: messagebox.showinfo('M5Tool', translations['alrinstalling'][lang])).start()
            return True
        
        installing = True

        while True:
            try:
                r = requests.get(url, timeout=240, stream=True)

                total_size = int(r.headers.get('content-length', 0))
                completed = 0
                proc = 0
                oneprocent = total_size//100

                with open(name, 'wb') as f: 

                    starttime = time.time()

                    for chunk in r.iter_content(chunk_size = 64 * 1024):
                        if chunk:
                            completed += len(chunk)
                            speed_mbps = ((len(chunk)+0.1) / (1024 * 16)) / (time.time()+1-starttime)
                            proc = (completed+0.1)//(oneprocent+0.1)
                            if not terminal: add_log(f'{translations["installing"][lang]}... ({round(speed_mbps, 3)} {translations["mbs"][lang]}) {proc}%')
                            else: 
                                print(f'{translations["installing"][lang]}... ({round(speed_mbps, 3)} {translations["mbs"][lang]}) {proc}%')
                                statuslabel.configure(text=f'{translations["installing"][lang]}... ({round(speed_mbps, 3)} {translations["mbs"][lang]}) {proc}%')
                            f.write(chunk)
                            f.flush()
                            os.fsync(f.fileno())
                            starttime = time.time()
                    
                break
            except Exception as e: 
                if not terminal: add_log(translations["retrying"][lang].replace(r'%err%', e))
                else: print(translations["retrying"][lang].replace(r'%err%', e))

        installing = False

    fileee = None
    portt = None
    device = 'plus2'
    alllogs = []

    M5ToolVersion = '4.6'

    if not os.path.exists('M5ToolConfig.json'): 
        with open('M5ToolConfig.json', 'w') as f: f.write('{"baudrateflash": "1500000", "addressflash": "0x000", "lang": "EN"}')
        flashaddress = '0x000'
        flashbaudrate = '1500000'
        lang = 'EN'
    else:
        with open('M5ToolConfig.json', 'r') as f:
            loaded = json.loads(f.read())
            try:
                flashaddress = loaded['addressflash']
                flashbaudrate = loaded['baudrateflash']
                lang = loaded['lang']
            except:
                with open('M5ToolConfig.json', 'w') as f: f.write('{"baudrateflash": "1500000", "addressflash": "0x000", "lang": "EN"}')
                flashaddress = '0x000'
                flashbaudrate = '1500000'
                lang = 'EN'

    def secondthread():

        global starter

        while True:

            time.sleep(0.1)

            if starter.get() == 1:

                try: 
                    threading.Thread(target=zanyat).start()
                except:
                    starter.deselect()

    cache = {}

    def parsefirmwr(repo, device):

        global portt, cache

        if repo not in cache.keys():

            r = requests.get(f"https://github.com{repo}")

            all = re.search(f'href="{repo}(.*?)"', r.text, re.DOTALL).group(1)

            r = requests.get(f"https://github.com{repo}expanded_assets{all[3:]}")

            all = re.findall(f'href="{repo}(.*?)"', r.text, re.DOTALL)

            cache[repo] = all

        else: all = cache[repo]

        for frmw in all:    
            if device == 'plus2':
                if 'plus2' in frmw.lower(): return f"https://github.com"+repo+frmw
            elif device == 'plus11':
                if 'plus' in frmw.lower() and not 'plus2' in frmw.lower(): return f"https://github.com"+repo+frmw
            elif device == 'cardputer':
                if 'card' in frmw.lower(): return f"https://github.com"+repo+frmw
            elif device == 'CYD1USB':
                if 'cyd' in frmw.lower() and '2432s028' in frmw.lower(): return f"https://github.com"+repo+frmw
            elif device == 'CYD2USB':
                if 'cyd' in frmw.lower(): return f"https://github.com"+repo+frmw

        if len(all) == 1:return f"https://github.com"+repo+all[0]

    def parsefirmwares():

        global popular, add_log

        popular = {'plus2': {
            'Nemo': 'https://github.com/n0xa/m5stick-nemo/releases/download/v2.7.0/M5Nemo-v2.7.0-M5StickCPlus2.bin',
            'Marauder': 'https://m5burner-cdn.m5stack.com/firmware/b732d70a74405f7f1c6e961fa4d17f37.bin',
            'UserDemo': 'https://github.com/m5stack/M5StickCPlus2-UserDemo/releases/download/V0.1/K016-P2-M5StickCPlus2-UserDemo-V0.1_0x0.bin',
            'CatHack': parsefirmwr('/Stachugit/CatHack/releases/', 'plus2'),
            'Hamster Kombat': 'https://m5burner-cdn.m5stack.com/firmware/896bce78796597d2ddc1545443f0a1c3.bin',
            'Bruce': parsefirmwr('/pr3y/Bruce/releases/', 'plus2'),
            'M5Launcher': parsefirmwr('/bmorcelli/M5Stick-Launcher/releases/', 'plus2')
        }, 'plus11': {
            'Nemo': 'https://github.com/n0xa/m5stick-nemo/releases/download/v2.7.0/M5Nemo-v2.7.0-M5StickCPlus.bin',
            'Marauder': 'https://m5burner-cdn.m5stack.com/firmware/3397b17ad7fd314603abf40954a65369.bin',
            'CatHack': None,
            'UserDemo': None,
            'Hamster Kombat': 'https://m5burner-cdn.m5stack.com/firmware/28eafdd732442b83395017a8f490a048.bin',
            'Bruce': parsefirmwr('/pr3y/Bruce/releases/', 'plus11'),
            'M5Launcher': parsefirmwr('/bmorcelli/M5Stick-Launcher/releases/', 'plus11')
        }, 'cardputer': {
            'Nemo': 'https://github.com/n0xa/m5stick-nemo/releases/download/v2.7.0/M5Nemo-v2.7.0-M5Cardputer.bin',
            'Marauder': 'https://m5burner-cdn.m5stack.com/firmware/aeb96d4fec972a53f934f8da62ab7341.bin',
            'UserDemo': 'https://github.com/m5stack/M5Cardputer-UserDemo/releases/download/V0.9/K132-Cardputer-UserDemo-V0.9_0x0.bin',
            'CatHack': None,
            'Hamster Kombat': None,
            'Bruce': parsefirmwr('/pr3y/Bruce/releases/', 'cardputer'),
            'M5Launcher': parsefirmwr('/bmorcelli/M5Stick-Launcher/releases/', 'cardputer')
        }, "cyd2usb": {
            'Nemo': None,
            'Marauder': 'https://github.com/Sonys9/M5Tool/raw/refs/heads/main/data/Marauder_espcyd2usb_v1.0.0.bin',
            'UserDemo': None,
            'CatHack': None,
            'Hamster Kombat': None,
            'Bruce': parsefirmwr('/pr3y/Bruce/releases/', 'CYD2USB'),
            'M5Launcher': parsefirmwr('/bmorcelli/M5Stick-Launcher/releases/', 'CYD2USB')
        }, "cyd1usb": {
            'Nemo': None,
            'Marauder': 'https://github.com/Sonys9/M5Tool/raw/refs/heads/main/data/Marauder_espcyd1usb_v1.0.0.bin',
            'UserDemo': None,
            'CatHack': None,
            'Hamster Kombat': None,
            'Bruce': parsefirmwr('/pr3y/Bruce/releases/', 'CYD1USB'),
            'M5Launcher': parsefirmwr('/bmorcelli/M5Stick-Launcher/releases/', 'CYD1USB')
        }}
        add_log(translations["parsend"][lang])
    threading.Thread(target=parsefirmwares).start()
    def getfrmwr(name):

        global device, popular

        try:return popular[device][name]
        except:return 'wait'

    def choicefile():

        global infoo, fileee

        file_path = filedialog.askopenfilename()
        if file_path: 
            filename = file_path.split('/')[-1]
            if len(filename) > 18:
                infoo.configure(text=filename[:20]+'...')
            else:
                infoo.configure(text=filename)

            fileee=file_path

    def bgtask(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd="./"):
        return subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)

    def flashh():

        global fileee, portt, serialport, flashing, flashbaudrate, flashaddress

        if portt: 

            if fileee:
        
                if not fileee.endswith('.bin'):

                    messagebox.showerror(title='M5Tool', message=translations["fileerr"][lang])

                else:

                    if not os.path.exists('esptool480\\esptool-win64'): 

                        messagebox.showerror(title='M5Tool', message=translations["esptoolisnt"][lang])

                    else:

                        flashing = True
                        try: serialport.close()
                        except Exception as e: ...

                        process = bgtask(f"esptool480\\esptool-win64\\esptool.exe --chip auto --port COM{portt} --baud {flashbaudrate} --before default_reset write_flash -z --flash_mode dio --flash_freq 80m --flash_size detect {flashaddress} \"{fileee}\"")

                        while True:

                            output = process.stdout.readline()

                            if output:

                                output_str = output.decode()

                                if "fatal error" in output_str or 'error occurred' in output_str:

                                    if 'not open' in output_str.lower():

                                        messagebox.showerror(title='M5Tool', message=translations["connecterr"][lang])

                                    else:

                                        messagebox.showerror(title='M5Tool', message=translations["flasherr"][lang].replace(r"%output_str%",output_str))
                                        
                                    flashing = False

                                    break

                                elif 'Hash of data verified.' in output_str: 

                                    messagebox.showinfo(title='M5Tool', message=translations["flashedok"][lang])

                                    flashing = False

                                    break

                                add_log(output_str)

                            else: ...

            else: messagebox.showerror(title='M5Tool', message=translations["filenotchoiced"][lang])

        else: messagebox.showerror(title='M5Tool', message=translations["devicenotcon"][lang])
        flashing=False

    def flashtoolisntall():
        
        add_log(translations["archinst1"][lang])

        r = installfile('https://github.com/espressif/esptool/releases/download/v4.8.0/esptool-v4.8.0-win64.zip', 'file.zip')

        if not r:

            add_log(translations["archinst2"][lang])
        
            with zipfile.ZipFile('file.zip', 'r') as zip_ref:
                zip_ref.extractall('esptool480')

            os.makedirs('esptool480', exist_ok=True)

            add_log(translations["archunp"][lang])

            messagebox.showinfo(title='M5Tool', message=translations["success"][lang])

    def installadriver(name, dir, link, endtext=translations["success1"][lang]):

        add_log(translations["instfile"][lang])

        os.makedirs(name, exist_ok=True)

        r = installfile(link, dir)

        if not r:

            add_log(translations["filestart"][lang])

            os.system(f'start {dir}')

            messagebox.showinfo(title='M5Tool', message=endtext)

    def installsecdriver(name, dir, link, endtext):

        add_log(translations["archinst1"][lang])

        r = installfile(link, 'file.zip')

        if not r:

            add_log(translations["archinst2"][lang])

            with zipfile.ZipFile('file.zip', 'r') as zip_ref:
                zip_ref.extractall(name)

            add_log(translations["archunp"][lang])

            os.system(f'start {dir}')

            messagebox.showinfo(title='M5Tool', message=endtext)

    def installdriverswindow():

        driverwindow = CTk()
        driverwindow.title(translations["driverswin"][lang])
        driverwindow.geometry('200x230')
        set_appearance_mode("dark")

        CTkFrame(driverwindow, width=180, height=210).place(x=10,y=10)

        ch341 = CTkButton(driverwindow, text='CH341', width=160, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=installadriver,
                                                args=('CH341', 'CH341\\CH3CH341.exe', 'https://github.com/Sonys9/M5Tool/raw/refs/heads/main/data/drivers/CH341SER.EXE')).start())
        ch341.place(x=20, y=20)

        ch9102 = CTkButton(driverwindow, text='CH9102', width=160, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=installadriver,
                                                args=('CH9102', 'CH9102\\CH9102.exe', 'https://github.com/Sonys9/M5Tool/raw/refs/heads/main/data/drivers/CH9102.exe')).start())
        ch9102.place(x=20, y=60)

        ch343 = CTkButton(driverwindow, text='CH343', width=160, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=installadriver,
                                                args=('CH343', 'CH343\\CH343.exe', 'https://github.com/Sonys9/M5Tool/raw/refs/heads/main/data/drivers/CH343SER.EXE')).start())
        ch343.place(x=20, y=100)

        CDM212364 = CTkButton(driverwindow, text='CDM212364', width=160, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=installadriver,
                                                args=('CDM212364', 'CDM212364\\CDM212364.exe', 'https://github.com/Sonys9/M5Tool/raw/refs/heads/main/data/drivers/CDM212364_Setup.exe',
                                                      translations["success2"][lang])).start())
        CDM212364.place(x=20, y=140)

        CP210x = CTkButton(driverwindow, text='CP210x', width=160, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=installsecdriver,
                                                args=('CP210x', 'CP210x\\CP210xVCPInstaller_x64.exe', 'https://github.com/Sonys9/M5Tool/raw/refs/heads/main/data/drivers/CP210x_Windows_Drivers.zip',
                                                      translations["success2"][lang])).start())
        CP210x.place(x=20, y=180)

        driverwindow.mainloop()

    def installfrmw():

        global firmws

        firmware = firmws.get()
        
        fileurl = getfrmwr(firmware)

        add_log(translations["urlis"][lang].replace(r'%url%', fileurl))

        if fileurl == None: messagebox.showerror(title='M5Tool', message=translations["firmwnotfound"][lang])
        elif fileurl == 'wait': messagebox.showerror(title='M5Tool', message=translations["waitparse"][lang])
        else:

            r = requests.get(fileurl)

            file_path = filedialog.asksaveasfilename(
                title=translations["saveafile"][lang],
                defaultextension=".bin", 
                filetypes=((translations["ffile"][lang], "*.bin"), (translations["afiles"][lang], "*.*"))
            )
            
            if file_path: 
                with open(file_path, 'wb') as f:
                    f.write(r.content)

    def installandflash():

        global firmws, fileee

        firmware = firmws.get()
        
        fileurl = getfrmwr(firmware)

        add_log(translations["urlis"][lang].replace(r'%url%', fileurl))

        if fileurl == None: messagebox.showerror(title='M5Tool', message=translations["firmwnotfound"][lang])
        elif fileurl == 'wait': messagebox.showerror(title='M5Tool', message=translations["waitparse"][lang])
        else:

            threading.Thread(target=lambda: messagebox.showinfo('M5Tool', translations["installing.."][lang])).start()

            r = requests.get(fileurl)

            fileee = f'{tempdir}\\{random.randint(10000,999999)}.bin'

            with open(fileee, 'wb') as f: f.write(r.content)

            flashh()

    def Eraseall():

        global portt, flashing, serialport, flashbaudrate

        if portt:

            result = messagebox.askquestion("M5Tool", translations["areyousure"][lang])

            if result == 'yes':

                flashing = True
                try: serialport.close()
                except Exception as e:...

                if not os.path.exists('esptool480\\esptool-win64'): 

                    messagebox.showerror(title='M5Tool', message=translations["esptoolisnt"][lang])

                else:

                    process = bgtask(f"esptool480\\esptool-win64\\esptool.exe --chip auto --port COM{portt} --baud {flashbaudrate} erase_flash")

                    while True:

                        output = process.stdout.readline()

                        if output:

                            output_str = output.decode()

                            if "fatal error" in output_str or 'error occurred' in output_str:

                                if 'not open' in output_str.lower():

                                    messagebox.showerror(title='M5Tool', message=translations["connecterr"][lang])

                                else:

                                    messagebox.showerror(title='M5Tool', message=translations["flasherr"][lang].replace(r'%output_str%', output_str))

                                flashing = False

                                break

                            elif 'Hash of data verified.' in output_str: 

                                messagebox.showinfo(title='M5Tool', message=translations["erasedok"][lang])

                                flashing = False

                                break

                            add_log(output_str)

                        else: ...

        else: messagebox.showerror(title='M5Tool', message=translations["devicenotcon"][lang])
        flashing=False

    def change(selected): 
        global device
        if selected == 'Cardputer': device = 'cardputer'
        if selected == 'M5StickC Plus1.1': device = 'plus11'
        if selected == 'M5StickC Plus2': device = 'plus2'
        if selected == 'Esp-CYD-2-USB': device = 'cyd2usb'
        if selected == 'Esp-CYD-1-USB': device = 'cyd1usb'
        add_log(translations["devis"][lang].replace(r'%dev%', selected))

    def change2(value):
        global portt, add_log
        portt = value.replace('COM', '')
        add_log(translations["comis"][lang].replace(r'%com%', portt))

    def getcomports():

        global portt, add_log

        lastport = ''

        while True:

            time.sleep(1)

            detectedcomports = []
            
            ports = serial.tools.list_ports.comports()

            for port, desc, hwid in sorted(ports):
                detectedcomports.append(port)

            comport.configure(values=detectedcomports)

            if detectedcomports == []: 
                comport.set('')
                lastport = ''

            if len(detectedcomports) == 1:

                comport.set(detectedcomports[0])
                portt = detectedcomports[0][3:]

                if lastport != portt:

                    lastport = portt

                    add_log(translations["comis"][lang].replace(r'%com%', portt))
                

    def getall():

        r = requests.get('https://raw.githubusercontent.com/bmorcelli/M5Stack-json-fw/main/script/all_device_firmware.json')

        try: 
            result = json.loads(r.text)
            all = []
            for res in result:
                name = res['name']
                descr = res['description']
                cover = res['cover'] if 'cover' in res else None
                category = res['category']
                author = res['author']
                downloads = res['download']
                vers = res['versions']
                all.append({'name': name, 'descr': descr, 'cover': cover,
                            'category': category, 'author': author, 'downl': downloads,
                            'vers': vers})
            return all
        except Exception as e: return f'ParseErr ({e})'

    def installvialink(link):

        r = requests.get(link)

        file_path = filedialog.asksaveasfilename(
            title=translations["saveafile"][lang],
            defaultextension=".bin", 
            filetypes=((translations["ffile"][lang], "*.bin"), (translations["afiles"][lang], "*.*"))
        )
        
        if file_path: 
            with open(file_path, 'wb') as f:
                f.write(r.content)

    def downn():

        global kostil, m5burner, toremove

        if kostil['current'] > 0:

            kostil['current'] -= 1

            current = kostil['current']

            for obj in toremove: obj.destroy()

            frame=CTkFrame(m5burner, width=280, height=155)
            frame.pack(pady=5)
    
            ndescr = [kostil["firmwares"][current][4][i:i + 100] for i in range(0, len(kostil["firmwares"][current][4]), 100)]
            ndescr = '\n'.join(ndescr)
            
            first = CTkLabel(frame, text=f'{kostil["firmwares"][current][3]} ({translations["by"][lang]} {kostil["firmwares"][current][6]})', font=('Arial Black', 15))
            first.pack()

            second = CTkLabel(frame, text=f'{ndescr}\n\n{kostil["firmwares"][current][7]}{translations["loadsinst"][lang]}{kostil["firmwares"][current][1]}')
            second.pack()

            third = CTkButton(frame, text=translations["downloadbin"][lang], fg_color=fg, hover_color=hover, 
                            command=lambda file=kostil["firmwares"][current][2]: threading.Thread(target=installvialink, args=(file,)).start())
            third.pack(pady=10)
            nextt = CTkButton(frame, text=translations["next"][lang], fg_color=fg, hover_color=hover, width=200, command=nexttt)
            nextt.pack(pady=20)
            down = CTkButton(frame, text=translations["down"][lang], fg_color=fg, hover_color=hover, width=200, command=downn)
            down.pack(pady=20)
            toremove.append(frame)
            

    def nexttt():
        
        global kostil, m5burner, toremove

        if kostil['current']+1 < len(kostil["firmwares"]):

            kostil['current'] += 1

            current = kostil['current']

            for obj in toremove: obj.destroy()

            frame=CTkFrame(m5burner, width=280, height=155)
            frame.pack(pady=5)
    
            ndescr = [kostil["firmwares"][current][4][i:i + 100] for i in range(0, len(kostil["firmwares"][current][4]), 100)]
            ndescr = '\n'.join(ndescr)
            
            first = CTkLabel(frame, text=f'{kostil["firmwares"][current][3]} ({translations["by"][lang]} {kostil["firmwares"][current][6]})', font=('Arial Black', 15))
            first.pack()

            second = CTkLabel(frame, text=f'{ndescr}\n\n{kostil["firmwares"][current][7]}{translations["loadsinst"][lang]}{kostil["firmwares"][current][1]}')
            second.pack()

            third = CTkButton(frame, text=translations["downloadbin"][lang], fg_color=fg, hover_color=hover, 
                            command=lambda file=kostil["firmwares"][current][2]: threading.Thread(target=installvialink, args=(file,)).start())
            third.pack(pady=10)
            nextt = CTkButton(frame, text=translations["next"][lang], fg_color=fg, hover_color=hover, width=200, command=nexttt)
            nextt.pack(pady=20)
            down = CTkButton(frame, text=translations["down"][lang], fg_color=fg, hover_color=hover, width=200, command=downn)
            down.pack(pady=20)
            toremove.append(frame)



    def doublethread():

        global search, m5burner, toremove, allfirmwaresfromm5burner, kostil, device

        last = None
        lastdev = None
        kostil = {}

        while True:

            time.sleep(0.1)

            text = search.get()
            
            if device not in ['cardputer', 'plus2', 'plus11']:
                messagebox.showerror(title='M5Tool', message=translations["m5burnerbd"][lang])
                m5burner.destroy()
                return
                
            if text != last or device != lastdev:

                last = text
                lastdev = device

                every = []

                for firmware in allfirmwaresfromm5burner:
                    need = 'cardputer' if device == 'cardputer' else 'stickc'
                    if firmware['category'] == need and text.lower() in firmware['name'].lower():
                        for res in firmware['vers']: 

                            ver = res['version'] if 'version' in res else None
                            date = res['published_at'] if 'published_at' in res else None
                            file = 'https://m5burner-cdn.m5stack.com/firmware/'+res['file']
                            name = firmware['name']
                            descr = firmware['descr']
                            cover = 'https://m5burner-cdn.m5stack.com/cover/'+firmware['cover']
                            author = firmware['author']
                            downloads = firmware['downl']

                            every.append([ver, date, file, name, descr, cover, author, downloads])

                kostil={'current': 0, 'firmwares': every}

                for obj in toremove: obj.destroy()

                frame=CTkFrame(m5burner, width=280, height=155)
                frame.pack(pady=5)
                toremove.append(frame)

                try:
        
                    ndescr = [every[0][4][i:i + 100] for i in range(0, len(every[0][4]), 100)]
                    ndescr = '\n'.join(ndescr)
                    
                    first = CTkLabel(frame, text=f'{every[0][3]} ({translations["by"][lang]} {every[0][6]})', font=('Arial Black', 15))
                    first.pack()

                    second = CTkLabel(frame, text=f'{ndescr}\n\n{every[0][7]}{translations["loadsinst"][lang]}{every[0][1]}')
                    second.pack()

                    third = CTkButton(frame, text=translations["downloadbin"][lang], fg_color=fg, hover_color=hover, 
                                    command=lambda file=every[0][2]: threading.Thread(target=installvialink, args=(file,)).start())
                    third.pack(pady=10)
                    nextt = CTkButton(frame, text=translations["next"][lang], fg_color=fg, hover_color=hover, width=200, command=nexttt)
                    nextt.pack(pady=20)
                    down = CTkButton(frame, text=translations["down"][lang], fg_color=fg, hover_color=hover, width=200, command=downn)
                    down.pack(pady=20)
                    

                except:...

    def add_log(text, add=True):
        try:
            global log_text, alllogs
            if text not in alllogs and add: print(text)
            log_text.configure(state='normal')
            log_text.insert(END, text + '\n') 
            log_text.see(END)
            log_text.configure(state='disabled')
            if add: alllogs.append(text)
        except:...

    def add_serial_log(text):
        try:
            global serial_text
            serial_text.configure(state='normal')
            serial_text.insert(END, text + '\n') 
            serial_text.see(END)
            serial_text.configure(state='disabled')
        except:...

    def openm5burner():

        global search, m5burner, toremove, allfirmwaresfromm5burner

        m5burner = CTk()
        m5burner.title("M5Burner")
        m5burner.geometry('600x600')
        set_appearance_mode("dark")

        allfirmwaresfromm5burner = getall()
        
        search = CTkEntry(m5burner, placeholder_text=translations["searchbar"][lang], width=590, height=30)
        search.pack()

        toremove = []

        threading.Thread(target=doublethread).start()

        m5burner.mainloop()

    def addcmd():

        global inputtext, serialport, portt

        text = inputtext.get()

        serialport.write(text.encode())

    def autozanyat():

        global serialport, portt, add_serial_log, custombaudrate, flashing

        flashing = False

        while True:

            time.sleep(0.001)

            if portt and not flashing:

                try: baud = int(custombaudrate.get())
                except: baud = 115200

                try: 
                    
                    serialport = serial.Serial(f'COM{portt}', baud)

                    add_log(translations["connectedtodev"][lang])

                except: ...

            else: 
                
                serialport = None

    def getalltext():

        global serialport, add_serial_log

        while True:

            time.sleep(0.01)

            if serialport != None:

                try:

                    if serialport.in_waiting > 0:

                        dataBarCode = serialport.readline()

                        add_serial_log(dataBarCode.decode("utf-8"))

                except:...

    def openconsolee():

        global log_text, serial_text, inputtext, serialport, custombaudrate

        console = CTk()
        console.title(translations["consoleandlogs"][lang])
        console.geometry('600x300')
        set_appearance_mode("dark")

        serialport = None

        log_text = CTkTextbox(console, width=280, height=230)
        log_text.configure(state='disabled', font=('Calibri', 13))
        log_text.place(x=10, y=10)

        log_text.delete("1.0", END)

        serial_text = CTkTextbox(console, width=280, height=230)
        serial_text.configure(state='disabled', font=('Calibri', 13))
        serial_text.place(x=310, y=10)     
        
        custombaudrate = CTkEntry(console, placeholder_text=translations["enterbaud"][lang], width=280, height=30)
        custombaudrate.place(x=10,y=250)

        custombaudrate.insert('0', '115200')

        inputtext = CTkEntry(console, placeholder_text=translations["entercmd"][lang], width=190, height=30)
        inputtext.place(x=310,y=250)

        entercmd = CTkButton(console, text=translations["sendbtn"][lang], width=50, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=addcmd).start())
        entercmd.place(x=510, y=250)

        add_log(translations["m5toollogshere"][lang], False)
        add_serial_log(translations["devicelogshere"][lang])

        for log in alllogs: add_log(log, False)

        threading.Thread(target=getalltext).start()
        threading.Thread(target=autozanyat).start()

        console.mainloop()

    def installfiles():

        global windowloading, statuslabel

        lbl = CTkLabel(windowloading, text=translations["archinst"][lang], font=('Calibri', 13))
        lbl.pack()

        statuslabel = CTkLabel(windowloading, text=f'{translations["installing.."][lang]} (0 {translations["mbs"][lang]}) 0%', font=('Calibri', 13))
        statuslabel.pack()

        installfile('https://github.com/espressif/esptool/releases/download/v4.8.0/esptool-v4.8.0-win64.zip', 'file.zip', True)
        statuslabel.destroy()
        lbl.configure(text=translations["archinst2"][lang])

        with zipfile.ZipFile('file.zip', 'r') as zip_ref:
            zip_ref.extractall('esptool480')

        os.makedirs('esptool480', exist_ok=True)

        lbl.configure(text=translations["reqend"][lang])

        lbl.destroy()

        windowloading.destroy()

    def loadwin():

        global windowloading, statuslabel

        windowloading = CTk()
        windowloading.title('M5Tool: Loading...')
        windowloading.geometry('400x100')
        windowloading.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))

        threading.Thread(target=installfiles).start()

        windowloading.mainloop()

    def cfgupdate():

        global flashbaudrate, flashaddress, baudr, addr, add_log, lang, langs

        try:

            baudratevalue = baudr.get()
            addressvalue = addr.get()

            try: baudratevalue = int(baudratevalue)
            except: 
                add_log(translations["badbaud"][lang])
                messagebox.showerror(title='M5Tool', message=translations["badbaud"][lang])
                return

            if 'x' not in addressvalue.lower(): 
                add_log(translations["badaddr"][lang])
                messagebox.showerror(title='M5Tool', message=translations["badaddr"][lang])
                return

            result = {"baudrateflash": baudratevalue, "addressflash": addressvalue, "lang": lang}

            needrestart = False
            
            with open('M5ToolConfig.json', 'r') as f:
                loaded = json.loads(f.read())
                flashaddress = loaded['addressflash']
                flashbaudrate = loaded['baudrateflash']
                lang2 = loaded['lang']
                if lang != lang2: needrestart=True

            with open('M5ToolConfig.json', 'w') as f:
                json.dump(result, f, indent=4)
                flashbaudrate = baudratevalue
                flashaddress = addressvalue
                add_log(translations["savedok"][lang])
                messagebox.showinfo(title='M5Tool', message=translations["savedok"][lang])
                if needrestart: messagebox.showinfo('M5Tool', translations['restartneeded'][lang])

        except Exception as e:  
            add_log(translations["saveerr"][lang].replace(r'%err%', e))
            messagebox.showerror(title='M5Tool', message=translations["saveerr"][lang].replace(r'%err%', e))
            return

    def change3(value):
        global lang, add_log
        if value == 'Русский': lang = 'RU'
        elif value == 'English': lang = 'EN'
        elif value == 'Arabic': lang = 'AR'
        add_log(translations["language"][lang]+f': {value}')

    def opensettings():

        global flashbaudrate, flashaddress, baudr, addr, lang, langs

        settingswindow = CTk()
        settingswindow.title(translations["opensettings"][lang])
        settingswindow.geometry('300x190')
        set_appearance_mode("dark")

        CTkFrame(settingswindow, width=280, height=130).place(x=10,y=10)

        baudr = CTkEntry(settingswindow, placeholder_text=translations["baudr"][lang], width=260, height=30)
        baudr.place(x=20,y=20)
        baudr.insert(0, flashbaudrate)
        
        addr = CTkEntry(settingswindow, placeholder_text=translations["addresstoflash"][lang], width=260, height=30)
        addr.place(x=20,y=60)
        addr.insert(0, flashaddress)

        langs = CTkOptionMenu(settingswindow, values=['English', 'Русский', 'Arabic'], height=30, width=260, fg_color=fg, bg_color=bg, hover=hover, button_color=hover, command=change3)
        langs.place(x=20, y=100)

        save = CTkButton(settingswindow, text=translations["savecfg"][lang], width=280, height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=cfgupdate)
        save.place(x=10, y=150)     

        settingswindow.mainloop()

    def checkupdates():

        updwindow = CTk()
        updwindow.title(translations["updates"][lang])
        updwindow.geometry('300x300')
        set_appearance_mode("dark")

        CTkFrame(updwindow, width=280, height=280).place(x=10,y=10)

        try:
            r=requests.get('https://github.com/Sonys9/M5Tool/raw/refs/heads/main/ver.txt')
            loaded = json.loads(r.text)
            vers = [loaded['version'], loaded['updlog'][lang]]
        except: vers = ['bad', '']

        if vers[0] == 'bad': 
            messagebox.showinfo('M5Tool', translations["upderr"][lang])
            updwindow.destroy()
            return
        
        CTkLabel(updwindow, text=translations["yourver"][lang].replace(r'%newver%', vers[0]).replace(r'%yourver%', M5ToolVersion), bg_color=bg, font=('Calibri', 23)).place(x=20, y=20)
        CTkLabel(updwindow, text=translations["youhavenew"][lang] if float(vers[0])<=float(M5ToolVersion) else translations["youhaveold"][lang], bg_color=bg, font=('Calibri', 17)).place(x=20, y=50)
        
        updtextbox = CTkTextbox(updwindow, width=260, height=200)
        updtextbox.configure(state='normal', font=('Calibri', 13))
        updtextbox.place(x=20, y=80)

        updtextbox.insert(END, translations["whatsnew"][lang]+'\n\n'+vers[1]) 
        updtextbox.see(END)
        updtextbox.configure(state='disabled')

        updwindow.mainloop()

    fg = '#008E63'
    hover = '#225244'
    bg = '#2B2B2B'

    window = CTk()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    window.title('M5Tool')
    window.geometry('590x375')
    window.resizable(False, False)
    set_appearance_mode("dark")
    window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))

    CTkFrame(window, width=280, height=45).place(x=10,y=10)

    CTkLabel(window, text='M5Tool by Palka', bg_color=bg, font=('Calibri', 20)).place(x=20, y=17)
    
    redirect = CTkButton(window, text='Telegram', width=110, height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: webbrowser.open('t.me/+BQManHgPo4ZmNGIy'))
    redirect.place(x=170, y=17)       
    
    CTkFrame(window, width=280, height=155).place(x=10,y=65)

    choiceafile = CTkButton(window, text=translations["choiceafile"][lang], width=100, fg_color=fg, bg_color=bg, hover_color=hover, command=choicefile)
    choiceafile.place(x=20, y=75)
    
    infoo = CTkLabel(window, text=translations["notchoiced"][lang], bg_color=bg, font=('Calibri', 15))
    infoo.place(x=130, y=75)

    flash = CTkButton(window, text=translations["flashbtn"][lang], width=160, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=flashh).start())
    flash.place(x=20, y=115)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

    eraseall = CTkButton(window, text=translations["eraseall"][lang], width=90, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=Eraseall).start())
    eraseall.place(x=190, y=115)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

    installdrivers = CTkButton(window, text=translations["installdriv"][lang], width=260, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installdriverswindow).start())
    installdrivers.place(x=20, y=165)

    CTkFrame(window, width=280, height=130).place(x=10,y=230)

    firmws = CTkOptionMenu(window, values=["M5Launcher", "Marauder", "Bruce", "Nemo", "UserDemo", "CatHack", 'Hamster Kombat'], width=260, fg_color=fg, bg_color=bg, hover=hover, button_color=hover)
    firmws.place(x=20, y=240)

    installfrmwr = CTkButton(window, text=translations["installbin"][lang], width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installfrmw).start())
    installfrmwr.place(x=20, y=280)

    flash2 = CTkButton(window, text=translations["flashbtn"][lang], width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installandflash).start())
    flash2.place(x=20, y=320)        

    CTkFrame(window, width=280, height=90).place(x=300,y=10)

    devices = CTkOptionMenu(window, values=["M5StickC Plus2", 'M5StickC Plus1.1', 'Cardputer', 'Esp-CYD-2-USB', 'Esp-CYD-1-USB'], height=30, width=260, fg_color=fg, bg_color=bg, hover=hover, button_color=hover, command=change)
    devices.place(x=310, y=20)

    comport = CTkOptionMenu(window, values=[translations["scanning"][lang]], height=30, width=260, fg_color=fg, bg_color=bg, hover=hover, button_color=hover, command=change2)
    comport.place(x=310, y=60)

    CTkFrame(window, width=280, height=45).place(x=300,y=110)

    starter = CTkCheckBox(window, text=translations["pickcom"][lang], bg_color=bg, hover_color=hover, fg_color=fg)
    starter.place(x=310, y=120)

    CTkFrame(window, width=280, height=170).place(x=300,y=165)

    installfrmwr = CTkButton(window, text=translations["openm5burner"][lang], width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, 
                             command=lambda: threading.Thread(target=openm5burner).start())
    installfrmwr.place(x=310, y=175)

    openconsole = CTkButton(window, text=translations["consoleandlogs"][lang], width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, 
                             command=lambda: threading.Thread(target=openconsolee).start())
    openconsole.place(x=310, y=215)

    settings = CTkButton(window, text=translations["opensettings"][lang], width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, 
                             command=lambda: threading.Thread(target=opensettings).start())
    settings.place(x=310, y=255)

    update = CTkButton(window, text=translations["checkupdates"][lang], width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, 
                             command=lambda: threading.Thread(target=checkupdates).start())
    update.place(x=310, y=295)

    threading.Thread(target=getcomports).start()
    threading.Thread(target=secondthread).start()
    
    if not os.path.exists('esptool480\\esptool-win64\\esptool.exe'):threading.Thread(target=loadwin).start()
    window.mainloop()

except Exception as e:
    
    input(translations["errorinend"][lang].replace(r'%err%', e))
