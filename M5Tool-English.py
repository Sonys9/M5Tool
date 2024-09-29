print('Loading... Please, wait.')

try:

    import os, threading, time, subprocess, zipfile, re, json

    try: 
        import serial.tools.list_ports
        import serial                                                                                                                                                                                                                                                                                                                                                                                              ; print('TG: @M5STICKHACK')
    except:

        print('Installing a module Serial...')                                      

        os.system('pip install setuptools')
        os.system('pip install pyserial')

        try: 

            import serial
            import serial.tools.list_ports
            print('Module Serial has been successful installed!')                                                                                                                                                                                                                                                                                                                                         ; print('TG: @M5STICKHACK')

        except: 

            input('An unknown error has been occured.')

    try: import requests                                                                                                                                                                                                                                                                                                                                                                                              ; print('TG: @M5STICKHACK')
    except:

        print('Installing a module Requests...')                                      

        os.system('pip install setuptools')
        os.system('pip install Requests')

        try: 

            import requests
            print('Module Requests has been successful installed!')                                                                                                                                                                                                                                                                                                                                         ; print('TG: @M5STICKHACK')

        except: 

            input('An unknown error has been occured.')

    try: 
        from tkinter import messagebox, filedialog
        from customtkinter import *                                                                                                                                                                                                                                                                                                                                                                                            ; print('TG: @M5STICKHACK')

    except:

        print('Installing a module CustomTkinter...')                                      

        os.system('pip install setuptools')
        os.system('pip install tkinter')
        os.system('pip install customtkinter')

        try: 

            from customtkinter import * 
            from tkinter import messagebox, filedialog

            print('Module CustomTkinter has been successful installed!')                                                                                                                                                                                                                                                                                                                                         ; print('TG: @M5STICKHACK')

        except: 

            input('An unknown error has been occured.')

    def zanyat():

        try:

            s = serial.Serial(f'COM{portt}')
            add_log(f'-Port COM{portt}')
            while True:
                res = s.read()
                
        except:...

    window = CTk()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ;sys.stdout.write("\nТ̷G̵:̷ ̷М̶5̶S̴Т̴I̶С̷К̵Н̶А̶С̴К̴\n")
    window.title('M5Tool')
    window.geometry('300x690')
    window.resizable(False, False)
    set_appearance_mode("dark")

    fileee = None
    portt = None
    device = 'plus2'

    def secondthread():

        while True:

            time.sleep(0.1)

            if starter.get() == 1:

                try: 
                    threading.Thread(target=zanyat).start()
                except:
                    starter.deselect()

    def getfrmwr(name):

        global device

        if device == 'plus2':
            
            if name == 'Nemo':

                return 'https://github.com/n0xa/m5stick-nemo/releases/download/v2.7.0/M5Nemo-v2.7.0-M5StickCPlus2.bin'
            
            if name == 'Marauder':

                return 'https://m5burner-cdn.m5stack.com/firmware/b732d70a74405f7f1c6e961fa4d17f37.bin'
            
            if name == 'UserDemo': 

                return 'https://github.com/m5stack/M5StickCPlus2-UserDemo/releases/download/V0.1/K016-P2-M5StickCPlus2-UserDemo-V0.1_0x0.bin'
            
            if name == 'CatHack':

                return parsefirmwr('/Stachugit/CatHack/releases/')
            
            if name == 'Hamster Kombat':

                return 'https://m5burner-cdn.m5stack.com/firmware/896bce78796597d2ddc1545443f0a1c3.bin'
            
        elif device == 'plus11':

            if name == 'Nemo':

                return 'https://github.com/n0xa/m5stick-nemo/releases/download/v2.7.0/M5Nemo-v2.7.0-M5StickCPlus.bin'
            
            if name == 'Marauder':

                return 'https://m5burner-cdn.m5stack.com/firmware/3397b17ad7fd314603abf40954a65369.bin'
            
            if name == 'UserDemo': return None 

            if name == 'CatHack': return None
            
            if name == 'Hamster Kombat': 
                
                return 'https://m5burner-cdn.m5stack.com/firmware/28eafdd732442b83395017a8f490a048.bin'
            
        elif device == 'cardputer':

            if name == 'Nemo':

                return 'https://github.com/n0xa/m5stick-nemo/releases/download/v2.7.0/M5Nemo-v2.7.0-M5Cardputer.bin'
            
            if name == 'Marauder':

                return 'https://m5burner-cdn.m5stack.com/firmware/aeb96d4fec972a53f934f8da62ab7341.bin'
            
            if name == 'UserDemo': 

                return 'https://github.com/m5stack/M5Cardputer-UserDemo/releases/download/V0.9/K132-Cardputer-UserDemo-V0.9_0x0.bin'
            
            if name == 'CatHack': return None

            if name == 'Hamster Kombat': return None

        if name == 'M5Launcher':

            return parsefirmwr('/bmorcelli/M5Stick-Launcher/releases/')
        
        if name == 'Bruce':

            return parsefirmwr('/pr3y/Bruce/releases/')

    def parsefirmwr(repo):

        global portt, device

        r = requests.get(f"https://github.com{repo}")

        all = re.search(f'href="{repo}(.*?)"', r.text, re.DOTALL).group(1)

        r = requests.get(f"https://github.com{repo}expanded_assets{all[3:]}")

        all = re.findall(f'href="{repo}(.*?)"', r.text, re.DOTALL)

        for frmw in all:    
            if device == 'plus2':
                if 'plus2' in frmw.lower(): return f"https://github.com"+repo+frmw
            elif device == 'plus11':
                if 'plus' in frmw.lower() and not 'plus2' in frmw.lower(): return f"https://github.com"+repo+frmw
            elif device == 'cardputer':
                if 'card' in frmw.lower(): return f"https://github.com"+repo+frmw

        if len(all) == 1:return f"https://github.com"+repo+all[0]

    #portt = '5' test
    #for i in ['marauder', 'bruce', 'nemo', 'm5launcher']: add_log(getfrmwr(i)) test

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

        global fileee, portt

        if portt != '' and fileee != None: # убрал говнокодище с if else и пофиксил мелкий незначительный баг (22.09.2024)
        
            if not fileee.endswith('.bin'):

                messagebox.showerror(title='M5Tool', message=f'Are you sure? Its not a .bin file!')

            else:

                if not os.path.exists('esptool480\\esptool-win64'): 

                    messagebox.showerror(title='M5Tool', message=f'EspTool isnt installed!')

                else:

                    process = bgtask(f"esptool480\\esptool-win64\\esptool.exe --chip auto --port COM{portt} --baud 1500000 --before default_reset write_flash -z --flash_mode dio --flash_freq 80m --flash_size detect 0x000 \"{fileee}\"")

                    while True:

                        output = process.stdout.readline()

                        if output:

                            output_str = str(output.strip())

                            if "fatal error" in output_str or 'error occurred' in output_str:

                                if 'not open' in output_str.lower():

                                    messagebox.showerror(title='M5Tool', message=f'An error has been occured at connecting to COM port. Try reconnect your device.')

                                else:

                                    messagebox.showerror(title='M5Tool', message=f'Error: {output_str}')

                                break

                            elif 'Hash of data verified.' in output_str: 

                                messagebox.showinfo(title='M5Tool', message=f'Success!')

                                break

                            add_log(output_str)

                        else: ...
                    
    def flashtoolisntall():

        if os.path.exists('esptool480'): messagebox.showinfo(title='M5Tool', message='EspTool alr installed!')

        else:

            add_log('Downloading an archive...')

            while True:
                try:
                    r = requests.get('https://github.com/espressif/esptool/releases/download/v4.8.0/esptool-v4.8.0-win64.zip', timeout=240, stream=True)

                    total_size = int(r.headers.get('content-length', 0))
                    completed = 0
                    proc = 0
                    oneprocent = total_size//100

                    with open('file.zip', 'wb') as f: 

                        starttime = time.time()

                        for chunk in r.iter_content(chunk_size = 512 * 1024):
                            if chunk:
                                #add_log(total_size)
                                #add_log(completed)
                                completed += len(chunk)
                                speed_mbps = ((len(chunk)+0.01) / (1024 * 1024)) / (time.time()-starttime)
                                proc = (completed+0.01)//(oneprocent+0.01)
                                #completed+=proc
                                add_log(f'Downloading... ({speed_mbps} Mbps) {proc}%')
                                f.write(chunk)
                                f.flush()
                                os.fsync(f.fileno())
                                starttime = time.time()
                        
                    break
                except Exception as e: add_log(f'Retrying... Error: {e}')

            add_log('Archive has been downloaded.\nUnpacking an archive...')
        
            with zipfile.ZipFile('file.zip', 'r') as zip_ref:
                zip_ref.extractall('esptool480')

            os.makedirs('esptool480', exist_ok=True)

            add_log('Success!')

            messagebox.showinfo(title='M5Tool', message='Success!')

    def installCH341driver():

        if os.path.exists('CH341'): messagebox.showinfo(title='M5Tool', message='Drivers alr installed!')

        else:

            add_log('Downloading a file...')

            os.makedirs('CH341', exist_ok=True)

            while True:
                try:
                    r = requests.get('https://github.com/Sonys9/M5Tool/raw/refs/heads/main/CH341SER.EXE', timeout=240, stream=True)

                    total_size = int(r.headers.get('content-length', 0))
                    completed = 0
                    proc = 0
                    oneprocent = total_size//100

                    with open('CH341\\CH3CH341.exe', 'wb') as f: 

                        starttime = time.time()

                        for chunk in r.iter_content(chunk_size = 512 * 1024):
                            if chunk:
                                #add_log(total_size)
                                #add_log(completed)
                                completed += len(chunk)
                                speed_mbps = ((len(chunk)+0.01) / (1024 * 1024)) / (time.time()-starttime)
                                proc = (completed+0.01)//(oneprocent+0.01)
                                #completed+=proc
                                add_log(f'Downloading... ({speed_mbps} Mbps) {proc}%')
                                f.write(chunk)
                                f.flush()
                                os.fsync(f.fileno())
                                starttime = time.time()
                        
                    break
                except Exception as e: add_log(f'Retrying... Error: {e}')

            add_log('File has been downloaded! Launching...')

            os.system('start CH341\\CH3CH341.exe')

            messagebox.showinfo(title='M5Tool', message='Success! Click Install to continue')

    def installfrmw():

        global firmws

        firmware = firmws.get()
        
        fileurl = getfrmwr(firmware)

        add_log(f'Link: {fileurl}')

        if fileurl == None: messagebox.showerror(title='M5Tool', message='A firmware file dont found for your device')

        else:

            r = requests.get(fileurl)

            file_path = filedialog.asksaveasfilename(
                title="Save a file",
                defaultextension=".bin", 
                filetypes=(("Firmware file", "*.bin"), ("All files", "*.*"))
            )
            
            if file_path: 
                with open(file_path, 'wb') as f:
                    f.write(r.content)

    def Eraseall():

        global portt

        if portt != None:

            result = messagebox.askquestion("M5Tool", "Are you sure?")

            if result == 'yes':

                process = bgtask(f"esptool480\\esptool-win64\\esptool.exe --chip auto --port COM{portt} --baud 1500000 erase_flash")

                while True:

                    output = process.stdout.readline()

                    if output:

                        output_str = str(output.strip())

                        if "fatal error" in output_str or 'error occurred' in output_str:

                            if 'not open' in output_str.lower():

                                messagebox.showerror(title='M5Tool', message=f'An error has been occured at connecting to COM port. Try reconnect your device.')

                            else:

                                messagebox.showerror(title='M5Tool', message=f'Error: {output_str}')

                            break

                        elif 'Hash of data verified.' in output_str: 

                            messagebox.showinfo(title='M5Tool', message=f'Success!')

                            break

                        add_log(output_str)

                    else: ...

    def change(dev): 
        global device
        device = dev

    def change2(value):
        global portt, add_log
        #value = comport.get()
        portt = value.replace('COM', '')
        add_log(portt)
        add_log(f"COM port: COM{portt}")

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
                #portt = ''

            if len(detectedcomports) == 1:

                comport.set(detectedcomports[0])
                portt = detectedcomports[0][3:]

                if lastport != portt:

                    lastport = portt

                    add_log(f"COM port: COM{portt}")
                

        #else: messagebox.showinfo(title='M5Tool', message=f'Найден(-о) {len(detectedcomports)} COM порт(-ов)')

        #portt = detectedcomport
        #window.title(f'M5Tool | COM PORT: {portt}')

    #def checkpin():

    #    global pincode, sf, starter   

    #    pin = pincode.get().replace(' ','')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ;pin=str(int(pin)*7) 

    #    if pin == '66185': 

    #        sf.destroy()
    #        pincode.destroy()

    #        starter.place(x=20, y=550)

    #    else: messagebox.showerror(title='M5Tool', message='Неверный пин-код!')

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
            title="Save a file",
            defaultextension=".bin", 
            filetypes=(("Firmware file", "*.bin"), ("All files", "*.*"))
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
            
            first = CTkLabel(frame, text=f'{kostil["firmwares"][current][3]} (by {kostil["firmwares"][current][6]})', font=('Arial Black', 15))
            first.pack()

            second = CTkLabel(frame, text=f'{ndescr}\n\n{kostil["firmwares"][current][7]} downloads, uploaded at {kostil["firmwares"][current][1]}')
            second.pack()

            third = CTkButton(frame, text=f'Download', fg_color=fg, hover_color=hover, 
                            command=lambda file=kostil["firmwares"][current][2]: threading.Thread(target=installvialink, args=(file,)).start())
            third.pack(pady=10)
            nextt = CTkButton(frame, text=f'Next', fg_color=fg, hover_color=hover, width=200, command=nexttt)
            nextt.pack(pady=20)
            down = CTkButton(frame, text=f'Down', fg_color=fg, hover_color=hover, width=200, command=downn)
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
            
            first = CTkLabel(frame, text=f'{kostil["firmwares"][current][3]} (by {kostil["firmwares"][current][6]})', font=('Arial Black', 15))
            first.pack()

            second = CTkLabel(frame, text=f'{ndescr}\n\n{kostil["firmwares"][current][7]} downloads, uploaded at {kostil["firmwares"][current][1]}')
            second.pack()

            third = CTkButton(frame, text=f'Download', fg_color=fg, hover_color=hover, 
                            command=lambda file=kostil["firmwares"][current][2]: threading.Thread(target=installvialink, args=(file,)).start())
            third.pack(pady=10)
            nextt = CTkButton(frame, text=f'Next', fg_color=fg, hover_color=hover, width=200, command=nexttt)
            nextt.pack(pady=20)
            down = CTkButton(frame, text=f'Down', fg_color=fg, hover_color=hover, width=200, command=downn)
            down.pack(pady=20)
            toremove.append(frame)



    def doublethread():

        global search, m5burner, toremove, allfirmwaresfromm5burner, kostil, device

        last = None
        kostil = {}

        while True:

            time.sleep(0.1)

            text = search.get()

            if text != last:

                last = text

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
        
                ndescr = [every[0][4][i:i + 100] for i in range(0, len(every[0][4]), 100)]
                ndescr = '\n'.join(ndescr)
                
                first = CTkLabel(frame, text=f'{every[0][3]} (by {every[0][6]})', font=('Arial Black', 15))
                first.pack()

                second = CTkLabel(frame, text=f'{ndescr}\n\n{every[0][7]} downloads, uploaded at {every[0][1]}')
                second.pack()

                third = CTkButton(frame, text=f'Download', fg_color=fg, hover_color=hover, 
                                command=lambda file=every[0][2]: threading.Thread(target=installvialink, args=(file,)).start())
                third.pack(pady=10)
                nextt = CTkButton(frame, text=f'Next', fg_color=fg, hover_color=hover, width=200, command=nexttt)
                nextt.pack(pady=20)
                down = CTkButton(frame, text=f'Down', fg_color=fg, hover_color=hover, width=200, command=downn)
                down.pack(pady=20)
                toremove.append(frame)

    def add_log(text):
        try:
            global log_text
            log_text.configure(state='normal')
            log_text.insert(END, text + '\n') 
            log_text.see(END)
            log_text.configure(state='disabled')
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
        
        search = CTkEntry(m5burner, placeholder_text='Search', width=590, height=30)
        search.pack()

        toremove = []

        threading.Thread(target=doublethread).start()

        m5burner.mainloop()

    def addcmd():

        global inputtext, serialport, portt

        text = inputtext.get()

        serialport.write(text.encode())

    def autozanyat():

        global serialport, portt, add_serial_log, custombaudrate

        while True:

            time.sleep(0.001)

            if portt and portt != '':

                try: baud = int(custombaudrate.get())
                except: baud = 115200

                try: 
                    
                    serialport = serial.Serial(f'COM{portt}', baud)

                    add_log('Connected')

                except: ...#add_serial_log('Не удалось подключиться к устройству')

            else: 
                
                serialport = None
                #connected = False

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
        console.title("Console and logs")
        console.geometry('600x300')
        set_appearance_mode("dark")

        serialport = None

        log_text = CTkTextbox(console, width=280, height=230)
        log_text.configure(state='disabled', font=('Calibri', 13))
        log_text.place(x=10, y=10)

        serial_text = CTkTextbox(console, width=280, height=230)
        serial_text.configure(state='disabled', font=('Calibri', 13))
        serial_text.place(x=310, y=10)     
        
        custombaudrate = CTkEntry(console, placeholder_text='Enter a BaudRate', width=280, height=30)
        custombaudrate.place(x=10,y=250)

        custombaudrate.insert('0', '115200')

        inputtext = CTkEntry(console, placeholder_text='Enter a command', width=190, height=30)
        inputtext.place(x=310,y=250)

        entercmd = CTkButton(console, text='Send', width=50, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=addcmd).start())
        entercmd.place(x=510, y=250)

        add_log('M5Tool\'s logs will be here')
        add_serial_log('Device\'s logs will be here')

        threading.Thread(target=getalltext).start()
        threading.Thread(target=autozanyat).start()

        console.mainloop()

    fg = '#008E63'
    hover = '#225244'
    bg = '#2B2B2B'

    CTkFrame(window, width=280, height=45).place(x=10,y=10)

    #secretfunction = False

    #starter = CTkCheckBox(window, text='Автоматически занимать COM порт', bg_color=bg, hover_color=hover, fg_color=fg)
    #секретная функция :) чтобы ее врубить поменяй False на True в secretfunction (мне админ тгк сказал вырезать но я бедбой кодер)
    #if secretfunction:

    #    starter.place(x=20, y=20)
    
    #else:

    #    CTkLabel(window, text='M5Tool by @M5StickHack (TG)', bg_color=bg, font=('Calibri', 20)).place(x=20, y=17)

    # новая система пинкода для крутых декомпилеров

    CTkLabel(window, text='M5Tool by TG: m5stickhack', bg_color=bg, font=('Calibri', 20)).place(x=20, y=17)
    
    CTkFrame(window, width=280, height=155).place(x=10,y=65)

    choiceafile = CTkButton(window, text='Choice a file', width=100, fg_color=fg, bg_color=bg, hover_color=hover, command=choicefile)
    choiceafile.place(x=20, y=75)
    
    infoo = CTkLabel(window, text='File isnt choiced', bg_color=bg, font=('Calibri', 15))
    infoo.place(x=130, y=75)

    flash = CTkButton(window, text='Flash', width=160, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=flashh).start())
    flash.place(x=20, y=115)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ; os.system('echo Т̵̬̿̚G̷̠͍̀̈́'+' ̵̛̠͑М̷͙̳̎͘5̴͙̉S̷̭̓̕Т̶̦̏̎Ĭ̵̯̦͝'+'С̸͖̝͛К̸̞͗͝Н̷͕̊̍А̵̖̓С̵̣͓̚К̷͕̉̀')

    eraseall = CTkButton(window, text='Erase all', width=90, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=Eraseall).start())
    eraseall.place(x=190, y=115)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ; os.system('echo Т̵̬̿̚G̷̠͍̀̈́'+' ̵̛̠͑М̷͙̳̎͘5̴͙̉S̷̭̓̕Т̶̦̏̎Ĭ̵̯̦͝'+'С̸͖̝͛К̸̞͗͝Н̷͕̊̍А̵̖̓С̵̣͓̚К̷͕̉̀')

    installflashtool = CTkButton(window, text='Download a EspTool', width=120, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=flashtoolisntall).start())
    installflashtool.place(x=20, y=165)

    installCH341 = CTkButton(window, text='Download a drivers', width=110, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installCH341driver).start())
    installCH341.place(x=160, y=165)

    CTkFrame(window, width=280, height=90).place(x=10,y=230)

    #installm5launcher = CTkButton(window, text='Установить M5Launcher', width=260, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installfrmw,args=('m5launcher',)).start())
    #installm5launcher.place(x=20, y=240)

    #installbruce = CTkButton(window, text='Установить Bruce', width=260, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installfrmw,args=('bruce',)).start())
    #installbruce.place(x=20, y=290)

    #installnemo = CTkButton(window, text='Установить Nemo', width=260, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installfrmw,args=('nemo',)).start())
    #installnemo.place(x=20, y=340)

    #installmarauder = CTkButton(window, text='Установить Marauder', width=260, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installfrmw,args=('marauder',)).start())
    #installmarauder.place(x=20, y=390)

    # у меня глаза болели от кода выше (который уже закоментирован) сори я переделаю

    firmws = CTkOptionMenu(window, values=["M5Launcher", "Marauder", "Bruce", "Nemo", "UserDemo", "CatHack", 'Hamster Kombat'], width=200, fg_color=fg, bg_color=bg, hover=hover, button_color=hover)
    firmws.place(x=20, y=240)

    installfrmwr = CTkButton(window, text='Download a .bin file', width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installfrmw).start())
    installfrmwr.place(x=20, y=280)

    CTkFrame(window, width=280, height=175).place(x=10,y=330)

    radio_var = IntVar(value=0)
    m5stickcplus2 = CTkRadioButton(window, text="M5StickC Plus2",
                                                 variable= radio_var, value=1, command=lambda: change('plus2'), fg_color=fg, bg_color=bg, hover_color=hover)
    m5stickcplus2.place(x=20, y=340)
    m5stickcplus11 = CTkRadioButton(window, text="M5StickC Plus1.1",
                                                 variable= radio_var, value=2, command=lambda: change('plus11'), fg_color=fg, bg_color=bg, hover_color=hover)
    m5stickcplus11.place(x=20, y=380)

    cardputer = CTkRadioButton(window, text="Cardputer",
                                                 variable= radio_var, value=3, command=lambda: change('cardputer'), fg_color=fg, bg_color=bg, hover_color=hover)
    cardputer.place(x=20, y=420)                    
    
    m5stickcplus2.select()

    #checkcomport = CTkButton(window, text='Обновить список COM портов', height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=getcomport).start())
    #checkcomport.place(x=20, y=585)

    comport = CTkOptionMenu(window, values=["Scanning..."], width=200, fg_color=fg, bg_color=bg, hover=hover, button_color=hover, command=change2)
    comport.place(x=20, y=460)

    CTkFrame(window, width=280, height=45).place(x=10,y=515)

    #pincode = CTkEntry(window, placeholder_text='Пин-код', width=260, height=30)
    #pincode.place(x=20, y=525)

    #sf = CTkButton(window, text='Активировать доп. функцию', width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=checkpin)
    #sf.place(x=20, y=565)

    starter = CTkCheckBox(window, text='COM port fucker', bg_color=bg, hover_color=hover, fg_color=fg)
    starter.place(x=20, y=525)

    CTkFrame(window, width=280, height=50).place(x=10,y=570)

    installfrmwr = CTkButton(window, text='Open Simple M5Burner', width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, 
                             command=lambda: threading.Thread(target=openm5burner).start())
    installfrmwr.place(x=20, y=580)

    threading.Thread(target=getcomports).start()
    threading.Thread(target=secondthread).start()
    #как вы заметили, я очень люблю threading

    CTkFrame(window, width=280, height=50).place(x=10,y=630)

    openconsole = CTkButton(window, text='Open Logs/Console', width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, 
                             command=lambda: threading.Thread(target=openconsolee).start())
    openconsole.place(x=20, y=640)

    window.mainloop()

except Exception as e:
    
    input(f'Error: {e}, contact me (@freedomleaker) in telegram (our chat: @stickhack_chat)')