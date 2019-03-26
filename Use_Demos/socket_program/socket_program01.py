# coding=utf-8

"""
    在Python中 使用socket模块的函数socket就可以完成：
        import socket
        socket.socket(AddressFamily, Type)
    说明：
        函数socket.socket创建一个socket，该函数带有两个参数：
            - AddressFamily:可以选择AF_INET（用于Internet进程间通信）或者AF_UNIX(用于同一台机器进程间通信)，实际工作中常用AF_INET
            - Type：套接字类型，可以是SOCKET_STREAM(流式套接字，主要用于TCp协议)或者SOCKET_DGRAM（数据报套接字，主要用于UDP协议）
"""
import socket

# 创建一个tcp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.close()

# 创建一个udp socket（udp套接字）
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.close()
