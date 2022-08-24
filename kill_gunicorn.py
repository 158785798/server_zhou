import os
import subprocess

proc_name = 'gunicorn_8096'


def kill_process():
    # 终端执行的命令
    process_id = subprocess.Popen(["pgrep", "-f", proc_name], stdout=subprocess.PIPE, shell=False)
    # 获取pid
    pid = str(process_id.communicate()[0], 'utf-8').split("\n")
    for i in pid:
        if i != '':
            try:
                os.system("kill -9 " + str(i))
            except:
                pass


if __name__ == '__main__':
    kill_process()