class blksnap_update:
    def update():
        import subprocess
        subprocess.call('git clone --single-branch --branch VAL-6.2 https://github.com/veeam/blksnap', shell = True)
        subprocess.call('cd blksnap/module && bash mk.sh build', shell = True)
        subprocess.call('cd blksnap/module && sudo bash mk.sh install', shell = True)

if __name__ == "__main__":
    blksnap_update.update()
    
