print('Запуск... Пожалуйста, подождите')

try:

    import os, threading, time, subprocess, zipfile, re, json, random

    try: 
        import serial.tools.list_ports
        import serial                                                                                                                                                                                                                                                                                                                                                                                             
    except:

        print('Устанавливаем модуль Serial...')                                      

        os.system('pip install setuptools')
        os.system('pip install pyserial')

        try: 

            import serial
            import serial.tools.list_ports
            print('Модуль Serial установлен!')                                                                                                                                                                                                                                                                                                                                        

        except: 

            input('Не удалось установить модуль Serial.')

    try: import requests                                                                                                                                                                                                                                                                                                                                                                                             
    except:

        print('Устанавливаем модуль Requests...')                                      

        os.system('pip install setuptools')
        os.system('pip install Requests')

        try: 

            import requests
            print('Модуль Requests установлен!')                                                                                                                                                                                                                                                                                                                                        

        except: 

            input('Не удалось установить модуль Requests.')

    try: 
        from tkinter import messagebox, filedialog
        from customtkinter import *                                                                                                                                                                                                                                                                                                                                                                                           

    except:

        print('Устанавливаем модуль CustomTkinter...')                                      

        os.system('pip install setuptools')
        os.system('pip install tkinter')
        os.system('pip install customtkinter')

        try: 

            from customtkinter import * 
            from tkinter import messagebox, filedialog

            print('Модуль CustomTkinter установлен!')                                                                                                                                                                                                                                                                                                                                        

        except: 

            input('Не удалось установить модуль CustomTkinter.')

    def zanyat():

        try:

            s = serial.Serial(f'COM{portt}')
            add_log('Порт занят!')
            while True:
                res = s.read()
                
        except:...

    installing = False

    if os.name == 'posix':username = os.getenv('USER') or os.getenv('LOGNAME')
    else:username = os.getenv('USERNAME')
    tempdir = f'C:\\Users\\{username}\\AppData\\Local\\Temp'

    def installfile(url, name, terminal=False):

        global installing

        if not terminal: threading.Thread(target=lambda: messagebox.showinfo('M5Tool', 'Устанавливаем... Логи будут в консоли.')).start()

        if installing: 
            if not terminal: threading.Thread(target=lambda: messagebox.showinfo('M5Tool', 'Ты уже что-то устанавливаешь!')).start()
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
                            speed_mbps = ((len(chunk)+0.1) / (1024 * 1024)) / (time.time()+1-starttime)
                            proc = (completed+0.1)//(oneprocent+0.1)
                            if not terminal: add_log(f'Устанавливаем... ({speed_mbps} МБ/с) {proc}%')
                            else: print(f'Устанавливаем... ({speed_mbps} МБ/с) {proc}%')
                            f.write(chunk)
                            f.flush()
                            os.fsync(f.fileno())
                            starttime = time.time()
                    
                break
            except Exception as e: 
                if not terminal: add_log(f'Пытаемся установить снова... Проверьте скорость вашего интернет-соединения, ошибка: {e}')
                else: print(f'Пытаемся установить снова... Проверьте скорость вашего интернет-соединения, ошибка: {e}')

        installing = False

    if not os.path.exists('esptool480\\esptool-win64\\esptool.exe'):

        print('Устанавливаем зависимости... Пожалуйста, подождите.')

        installfile('https://github.com/espressif/esptool/releases/download/v4.8.0/esptool-v4.8.0-win64.zip', 'file.zip', True)

        print('Архив установлен.\nРазархивируем архив...')

        with zipfile.ZipFile('file.zip', 'r') as zip_ref:
            zip_ref.extractall('esptool480')

        os.makedirs('esptool480', exist_ok=True)

        print('Архив разархивирован!\nЗависимости установлены!')

    window = CTk()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    window.title('M5Tool')
    window.geometry('300x730')
    window.resizable(False, False)
    set_appearance_mode("dark")

    fileee = None
    portt = None
    device = 'plus2'
    alllogs = []

    def secondthread():

        global starter

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
            
            if name == 'UserDemo (заводская)': 

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
            
            if name == 'UserDemo (заводская)': return None 

            if name == 'CatHack': return None
            
            if name == 'Hamster Kombat': 
                
                return 'https://m5burner-cdn.m5stack.com/firmware/28eafdd732442b83395017a8f490a048.bin'
            
        elif device == 'cardputer':

            if name == 'Nemo':

                return 'https://github.com/n0xa/m5stick-nemo/releases/download/v2.7.0/M5Nemo-v2.7.0-M5Cardputer.bin'
            
            if name == 'Marauder':

                return 'https://m5burner-cdn.m5stack.com/firmware/aeb96d4fec972a53f934f8da62ab7341.bin'
            
            if name == 'UserDemo (заводская)': 

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

        global fileee, portt, serialport, flashing

        if portt != '' and portt: 

            if fileee:
        
                if not fileee.endswith('.bin'):

                    messagebox.showerror(title='M5Tool', message=f'Это точно файл прошивки? Должен быть .bin файл!')

                else:

                    if not os.path.exists('esptool480\\esptool-win64'): 

                        messagebox.showerror(title='M5Tool', message=f'EspTool не установлен! Перезапустите программу')

                    else:

                        flashing = True
                        try: serialport.close()
                        except Exception as e: ...##print(f'error {e}')

                        process = bgtask(f"esptool480\\esptool-win64\\esptool.exe --chip auto --port COM{portt} --baud 1500000 --before default_reset write_flash -z --flash_mode dio --flash_freq 80m --flash_size detect 0x000 \"{fileee}\"")

                        while True:

                            output = process.stdout.readline()

                            if output:

                                output_str = output.decode()

                                if "fatal error" in output_str or 'error occurred' in output_str:

                                    if 'not open' in output_str.lower():

                                        messagebox.showerror(title='M5Tool', message=f'Не удалось подключиться к устройству, попробуйте переподключить устройство или скачать драйвера')

                                    else:

                                        messagebox.showerror(title='M5Tool', message=f'Произошла неизвестная ошибка: {output_str}, попробуйте установить драйвера, если они не установлены')
                                        
                                    flashing = False

                                    break

                                elif 'Hash of data verified.' in output_str: 

                                    messagebox.showinfo(title='M5Tool', message=f'Прошивка успешно установлена')

                                    flashing = False

                                    break

                                add_log(output_str)

                            else: ...

            else: messagebox.showerror(title='M5Tool', message=f'Вы не выбрали файл прошивки')

        else: messagebox.showerror(title='M5Tool', message=f'Вы не подключили устройство к пк. Если вы подключили, но не получается прошить, попробуйте установить драйвера')
        flashing=False

    def flashtoolisntall():
        
        add_log('Устанавливаем архив...')

        r = installfile('https://github.com/espressif/esptool/releases/download/v4.8.0/esptool-v4.8.0-win64.zip', 'file.zip')

        if not r:

            add_log('Архив установлен.\nРазархивируем архив...')
        
            with zipfile.ZipFile('file.zip', 'r') as zip_ref:
                zip_ref.extractall('esptool480')

            os.makedirs('esptool480', exist_ok=True)

            add_log('Архив разархивирован!')

            messagebox.showinfo(title='M5Tool', message='Успех!')

    def installch341():

        add_log('Устанавливаем файл...')

        os.makedirs('CH341', exist_ok=True)

        r = installfile('https://github.com/Sonys9/M5Tool/raw/refs/heads/main/CH341SER.EXE', 'CH341\\CH3CH341.exe')

        if not r:

            add_log('Файл установлен! Запускаем...')

            os.system('start CH341\\CH3CH341.exe')

            messagebox.showinfo(title='M5Tool', message='Успех! Нажмите Install для установки драйверов.')

    def installch343():

        add_log('Устанавливаем файл...')

        os.makedirs('CH343', exist_ok=True)

        r = installfile('https://github.com/Sonys9/M5Tool/raw/refs/heads/main/CH343SER.EXE', 'CH343\\CH343.exe')

        if not r:

            add_log('Файл установлен! Запускаем...')

            os.system('start CH343\\CH343.exe')

            messagebox.showinfo(title='M5Tool', message='Успех! Нажмите Install для установки драйверов.')

    def installch9102():

        add_log('Устанавливаем файл...')

        os.makedirs('CH9102', exist_ok=True)

        r = installfile('https://github.com/Sonys9/M5Tool/raw/refs/heads/main/CH9102.exe', 'CH9102\\CH9102.exe')

        if not r:

            add_log('Файл установлен! Запускаем...')

            os.system('start CH9102\\CH9102.exe')

            messagebox.showinfo(title='M5Tool', message='Успех! Нажмите Install для установки драйверов.')
    
    def installdriverswindow():

        driverwindow = CTk()
        driverwindow.title("Драйвера")
        driverwindow.geometry('200x150')
        set_appearance_mode("dark")

        CTkFrame(driverwindow, width=180, height=130).place(x=10,y=10)

        ch341 = CTkButton(driverwindow, text='CH341', width=160, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=installch341).start())
        ch341.place(x=20, y=20)

        ch9102 = CTkButton(driverwindow, text='CH9102', width=160, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=installch9102).start())
        ch9102.place(x=20, y=60)

        ch343 = CTkButton(driverwindow, text='CH343', width=160, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=installch343).start())
        ch343.place(x=20, y=100)

        driverwindow.mainloop()

    def installfrmw():

        global firmws

        firmware = firmws.get()
        
        fileurl = getfrmwr(firmware)

        add_log(f'Ссылка: {fileurl}')

        if fileurl == None: messagebox.showerror(title='M5Tool', message='Прошивка для вашего устройства не найдена :(')

        else:

            r = requests.get(fileurl)

            file_path = filedialog.asksaveasfilename(
                title="Сохранить файл",
                defaultextension=".bin", 
                filetypes=(("Файл прошивки", "*.bin"), ("Все файлы", "*.*"))
            )
            
            if file_path: 
                with open(file_path, 'wb') as f:
                    f.write(r.content)

    def installandflash():

        global firmws, fileee

        firmware = firmws.get()
        
        fileurl = getfrmwr(firmware)

        add_log(f'Ссылка: {fileurl}')

        if fileurl == None: messagebox.showerror(title='M5Tool', message='Прошивка для вашего устройства не найдена :(')

        else:

            threading.Thread(target=lambda: messagebox.showinfo('M5Tool', 'Устанавливаем... Логи будут в консоли.')).start()

            r = requests.get(fileurl)

            fileee = f'{tempdir}\\{random.randint(10000,999999)}.bin'

            with open(fileee, 'wb') as f: f.write(r.content)

            flashh()

    def Eraseall():

        global portt, flashing, serialport

        if portt and portt != '':

            result = messagebox.askquestion("M5Tool", "Вы уверены?")

            if result == 'yes':

                flashing = True
                try: serialport.close()
                except Exception as e:... #print(f'error {e}')

                if not os.path.exists('esptool480\\esptool-win64'): 

                    messagebox.showerror(title='M5Tool', message=f'EspTool не установлен! Перезапустите программу')

                else:

                    process = bgtask(f"esptool480\\esptool-win64\\esptool.exe --chip auto --port COM{portt} --baud 1500000 erase_flash")

                    while True:

                        output = process.stdout.readline()

                        if output:

                            output_str = output.decode()

                            if "fatal error" in output_str or 'error occurred' in output_str:

                                if 'not open' in output_str.lower():

                                    messagebox.showerror(title='M5Tool', message=f'Не удалось подключиться к устройству, попробуйте переподключить устройство')

                                else:

                                    messagebox.showerror(title='M5Tool', message=f'Произошла неизвестная ошибка: {output_str}')

                                flashing = False

                                break

                            elif 'Hash of data verified.' in output_str: 

                                messagebox.showinfo(title='M5Tool', message=f'Данные с устройства успешно стёрты!')

                                flashing = False

                                break

                            add_log(output_str)

                        else: ...

        else: messagebox.showerror(title='M5Tool', message=f'Вы не подключили устройство к пк. Если вы подключили, но не получается прошить, попробуйте установить драйвера')
        flashing=False

    def change(dev): 
        global device
        device = dev

    def change2(value):
        global portt, add_log
        #value = comport.get()
        portt = value.replace('COM', '')
        add_log(portt)
        add_log(f"COM порт: COM{portt}")

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

                    add_log(f"COM порт: COM{portt}")
                

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
            title="Сохранить файл",
            defaultextension=".bin", 
            filetypes=(("Файл прошивки", "*.bin"), ("Все файлы", "*.*"))
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
            
            first = CTkLabel(frame, text=f'{kostil["firmwares"][current][3]} (от {kostil["firmwares"][current][6]})', font=('Arial Black', 15))
            first.pack()

            second = CTkLabel(frame, text=f'{ndescr}\n\n{kostil["firmwares"][current][7]} скачиваний, загружено {kostil["firmwares"][current][1]}')
            second.pack()

            third = CTkButton(frame, text=f'Установить', fg_color=fg, hover_color=hover, 
                            command=lambda file=kostil["firmwares"][current][2]: threading.Thread(target=installvialink, args=(file,)).start())
            third.pack(pady=10)
            nextt = CTkButton(frame, text=f'Следующее', fg_color=fg, hover_color=hover, width=200, command=nexttt)
            nextt.pack(pady=20)
            down = CTkButton(frame, text=f'Назад', fg_color=fg, hover_color=hover, width=200, command=downn)
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
            
            first = CTkLabel(frame, text=f'{kostil["firmwares"][current][3]} (от {kostil["firmwares"][current][6]})', font=('Arial Black', 15))
            first.pack()

            second = CTkLabel(frame, text=f'{ndescr}\n\n{kostil["firmwares"][current][7]} скачиваний, загружено {kostil["firmwares"][current][1]}')
            second.pack()

            third = CTkButton(frame, text=f'Установить', fg_color=fg, hover_color=hover, 
                            command=lambda file=kostil["firmwares"][current][2]: threading.Thread(target=installvialink, args=(file,)).start())
            third.pack(pady=10)
            nextt = CTkButton(frame, text=f'Следующее', fg_color=fg, hover_color=hover, width=200, command=nexttt)
            nextt.pack(pady=20)
            down = CTkButton(frame, text=f'Назад', fg_color=fg, hover_color=hover, width=200, command=downn)
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
                
                first = CTkLabel(frame, text=f'{every[0][3]} (от {every[0][6]})', font=('Arial Black', 15))
                first.pack()

                second = CTkLabel(frame, text=f'{ndescr}\n\n{every[0][7]} скачиваний, загружено {every[0][1]}')
                second.pack()

                third = CTkButton(frame, text=f'Установить', fg_color=fg, hover_color=hover, 
                                command=lambda file=every[0][2]: threading.Thread(target=installvialink, args=(file,)).start())
                third.pack(pady=10)
                nextt = CTkButton(frame, text=f'Следующее', fg_color=fg, hover_color=hover, width=200, command=nexttt)
                nextt.pack(pady=20)
                down = CTkButton(frame, text=f'Назад', fg_color=fg, hover_color=hover, width=200, command=downn)
                down.pack(pady=20)
                toremove.append(frame)

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
        m5burner.title("M5Burner (окно можно масштабировать вручную)")
        m5burner.geometry('600x600')
        set_appearance_mode("dark")

        allfirmwaresfromm5burner = getall()
        
        search = CTkEntry(m5burner, placeholder_text='Поиск', width=590, height=30)
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

            if portt and portt != '' and not flashing:

                try: baud = int(custombaudrate.get())
                except: baud = 115200

                try: 
                    
                    serialport = serial.Serial(f'COM{portt}', baud)

                    add_log('Подключено к устройству')

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
        console.title("Консоль и логи")
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
        
        custombaudrate = CTkEntry(console, placeholder_text='Введите BaudRate', width=280, height=30)
        custombaudrate.place(x=10,y=250)

        custombaudrate.insert('0', '115200')

        inputtext = CTkEntry(console, placeholder_text='Введите команду', width=190, height=30)
        inputtext.place(x=310,y=250)

        entercmd = CTkButton(console, text='Отправить', width=50, height=30, fg_color=fg, hover_color=hover, command=lambda: threading.Thread(target=addcmd).start())
        entercmd.place(x=510, y=250)

        add_log('Логи M5Tool будут здесь', False)
        add_serial_log('Логи устройства будут здесь')

        for log in alllogs: add_log(log, False)

        threading.Thread(target=getalltext).start()
        threading.Thread(target=autozanyat).start()

        console.mainloop()

    fg = '#008E63'
    hover = '#225244'
    bg = '#2B2B2B'

    CTkFrame(window, width=280, height=45).place(x=10,y=10)

    CTkLabel(window, text='M5Tool by Palka', bg_color=bg, font=('Calibri', 20)).place(x=20, y=17)
    
    CTkFrame(window, width=280, height=155).place(x=10,y=65)

    choiceafile = CTkButton(window, text='Выбрать файл', width=100, fg_color=fg, bg_color=bg, hover_color=hover, command=choicefile)
    choiceafile.place(x=20, y=75)
    
    infoo = CTkLabel(window, text='Файл не выбран', bg_color=bg, font=('Calibri', 15))
    infoo.place(x=130, y=75)

    flash = CTkButton(window, text='Прошить', width=160, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=flashh).start())
    flash.place(x=20, y=115)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

    eraseall = CTkButton(window, text='Стереть всё', width=90, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=Eraseall).start())
    eraseall.place(x=190, y=115)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

    installdrivers = CTkButton(window, text='Установить драйвера', width=260, height=40, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installdriverswindow).start())
    installdrivers.place(x=20, y=165)

    CTkFrame(window, width=280, height=130).place(x=10,y=230)

    firmws = CTkOptionMenu(window, values=["M5Launcher", "Marauder", "Bruce", "Nemo", "UserDemo (заводская)", "CatHack", 'Hamster Kombat'], width=260, fg_color=fg, bg_color=bg, hover=hover, button_color=hover)
    firmws.place(x=20, y=240)

    installfrmwr = CTkButton(window, text='Установить .bin файл', width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installfrmw).start())
    installfrmwr.place(x=20, y=280)

    flash2 = CTkButton(window, text='Прошить прошивку', width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: threading.Thread(target=installandflash).start())
    flash2.place(x=20, y=320)        

    CTkFrame(window, width=280, height=175).place(x=10,y=370)

    radio_var = IntVar(value=0)
    m5stickcplus2 = CTkRadioButton(window, text="M5StickC Plus2",
                                                 variable= radio_var, value=1, command=lambda: change('plus2'), fg_color=fg, bg_color=bg, hover_color=hover)
    m5stickcplus2.place(x=20, y=380)
    m5stickcplus11 = CTkRadioButton(window, text="M5StickC Plus1.1",
                                                 variable= radio_var, value=2, command=lambda: change('plus11'), fg_color=fg, bg_color=bg, hover_color=hover)
    m5stickcplus11.place(x=20, y=420)

    cardputer = CTkRadioButton(window, text="Cardputer",
                                                 variable= radio_var, value=3, command=lambda: change('cardputer'), fg_color=fg, bg_color=bg, hover_color=hover)
    cardputer.place(x=20, y=460)                    
    
    m5stickcplus2.select()

    comport = CTkOptionMenu(window, values=["Сканируем..."], width=260, fg_color=fg, bg_color=bg, hover=hover, button_color=hover, command=change2)
    comport.place(x=20, y=500)

    CTkFrame(window, width=280, height=45).place(x=10,y=555)

    starter = CTkCheckBox(window, text='Автоматически занимать COM порт', bg_color=bg, hover_color=hover, fg_color=fg)
    starter.place(x=20, y=565)

    CTkFrame(window, width=280, height=50).place(x=10,y=610)

    installfrmwr = CTkButton(window, text='Открыть встроенный M5Burner', width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, 
                             command=lambda: threading.Thread(target=openm5burner).start())
    installfrmwr.place(x=20, y=620)

    threading.Thread(target=getcomports).start()
    threading.Thread(target=secondthread).start()

    CTkFrame(window, width=280, height=50).place(x=10,y=670)

    openconsole = CTkButton(window, text='Открыть консоль/логи', width=260, height=30, fg_color=fg, bg_color=bg, hover_color=hover, 
                             command=lambda: threading.Thread(target=openconsolee).start())
    openconsole.place(x=20, y=680)

    window.mainloop()

except Exception as e:
    
    input(f'Ошибка: {e}')