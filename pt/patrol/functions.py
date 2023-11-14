import paramiko
import socket
import time
from datetime import date
from .models import OsData, CpuData, Logs

client = paramiko.SSHClient() # создание ssh клиента
start_logs = Logs.objects.all().count() # начало логов текущего подключения


# функция подключения к удаленному хосту по ssh
def connection_ssh(request):
    error = ""
    host = request.POST['inputIP']
    port = request.POST['inputPort']
    user = request.POST['inputLogin']
    secret = request.POST['inputPassword']

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=secret, port=port)
        send_log('connection_ssh(request)', 'successful ssh connection to host ' + host)
    except (paramiko.ssh_exception.SSHException, socket.error) as e:
        error = f"Error connecting to SSH server: {e}"
        send_log('connection_ssh(request)', f"Error connecting to SSH server: {e}")

    return error


# функция запуска детекта ОС и ЦП
def detect():
    result = {}
    send_log('detect()', 'OS data detection')
    result['os_data'] = detect_os_data()

    send_log('detect()', 'CPU data detection')
    result['cpu_data'] = detect_cpu_info()

    result['logs'] = print_log()

    return result


# функция детекта ОС (получение основных сведений об ОС удаленного хоста)
def detect_os_data():
    os = detect_data_on_host('lsb_release -i')
    description = detect_data_on_host('lsb_release -d')
    release = detect_data_on_host('lsb_release -r')
    codename = detect_data_on_host('lsb_release -c')
    architecture = detect_data_on_host('uname -m')
    kernel = detect_data_on_host('uname -r')
    type_system = detect_data_on_host('getconf LONG_BIT')

    OsData.objects.create(OS=os, description=description, release=release, codename=codename, architecture=architecture,
                          kernel=kernel, type=type_system)
    send_log('detect_os_data()', 'creating an OsData database record')

    n = OsData.objects.all().count()
    os_data = OsData.objects.get(pk=n)

    return os_data


# функция детекта ЦП (получение основных сведений об ЦП удаленного хоста)
def detect_cpu_info():
    modes = detect_data_on_host('lscpu | grep -m 1 \'CPU op-mode(s):\'')
    vendor = detect_data_on_host('lscpu | grep -m 1 \'Vendor ID:\'')
    model = detect_data_on_host('lscpu | grep -m 1 \'Model name:\'')
    CPUs = detect_data_on_host('lscpu | grep -m 1 \'CPU(s):\'')
    threads = detect_data_on_host('lscpu | grep -m 1 \'Thread(s) per core:\'')
    cores_per_socket = detect_data_on_host('lscpu | grep -m 1 \'Core(s) per socket:\'')
    sockets = detect_data_on_host('lscpu | grep -m 1 \'Socket(s):\'')

    CpuData.objects.create(modes=modes, vendor=vendor, model=model, CPUs=CPUs, threads=threads,
                          cores_per_socket=cores_per_socket, sockets=sockets)
    send_log('detect_cpu_info()', 'creating an CpuData database record')

    n = CpuData.objects.all().count()
    cpu_data = CpuData.objects.get(pk=n)

    return cpu_data


# функция отправления команды на хост, получения и парсинга ответа хоста
def detect_data_on_host(command):
    stdin, stdout, stderr = client.exec_command(command)
    send_log('detect_data_on_host()', 'send command: ' + command)
    data = stdout.read().decode()
    send_log('detect_data_on_host()', 'detected data: ' + data)
    data = data[data.find(':') + 1::].strip()

    stdin.close()
    stdout.close()
    stderr.close()

    return data


# функция логирования запущенных команд и ответов хоста
def send_log(function, event):
    curr_date = date.today()
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    Logs.objects.create(date=curr_date, time=curr_time, function=function, event=event)


# функция подготовки логов за текущее подключение к отображению на странице
def print_log():
    n = Logs.objects.all().count()
    logs = Logs.objects.filter(pk__range=(start_logs + 2, n))

    return logs


# функция разрыва соединения
def close_connection():
    client.close()
    send_log('close_connection()', 'connection break')
    start_logs = Logs.objects.all().count()
