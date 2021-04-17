'''Project for killing processes'''


def main():
    if len(sys.argv) < 2:
        sys.exit('usage: %s name' % __file__)
    else:
        list_of_proc_objects = []
        for argv in sys.argv[1:]:
            list_of_proc_objects.append(argv)
    print('=' * 20)
    for value in list_of_proc_objects:
        killed = []
        print(f'\n{value}')
        for proc in psutil.process_iter():
            if proc.name() == value.strip() and proc.pid != getpid():
                proc.kill()
                killed.append(proc.pid)
                print('[+] Proccess was killed')
        if not killed:
            print('[-] No process found')
    print('\n')
    print("=" * 20)
    sys.exit(0)


if __name__ == '__main__':
    from os import getpid
    import sys 

    import psutil

    main()
        