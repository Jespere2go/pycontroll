import platform
import socket
import subprocess as sub

max_reps = 5
overule_shutdown = True

host = "127.0.0.1"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Hello from client".encode(), (host, port))

data, addr = s.recvfrom(1024)
print(data.decode())


def shutdown():
    success = False
    shutdown_issued = False
    repcount = 0
    if platform.system() == "Linux" or "Darwin":
        sub.run(["shutdown"])
        success = True
    if platform.system() == "Windows":
        while not shutdown_issued and repcount < max_reps:
            completed = sub.run(["shutdown", "/s"])
            return_code = completed.returncode
            if return_code == 0:
                shutdown_issued = True
                success = True
            if return_code == 1190 and overule_shutdown:
                sub.run(["shutdown", "/a"])
                repcount = +1
            else:
                break

    else:
        success = False
    return success


# shutdown()
