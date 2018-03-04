/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: linh <marvin@42.fr>                        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/02 11:38:59 by linh              #+#    #+#             */
/*   Updated: 2018/03/03 08:45:32 by linh             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

static void daemonize(void)
{
    if (fork())
        exit(EXIT_SUCCESS);
    if (fork())
        exit(EXIT_SUCCESS);
	close(0);
	close(1);
	setsid();
}

int         main(int argc, char **argv)
{
    int server_fd;
    struct sockaddr_in server;
    int client_socket;
    char buf[1024];
    int portnum;
    int num;
    int opt = 1;
    // int pid;
    // int sid;

    num = 0;
    if (argc > 3 || argc == 1)
    {
        printf("usage: ./server port or ./server -D port\n");
        return (-1);
    }
    else if (argc == 2)
        portnum = atoi(argv[1]);
    else if (argc == 3 && !strcmp(argv[1],"-D"))
    {
        num = 1;
        portnum = atoi(argv[2]);
    }
    else
    {
        printf("usage: ./server port or ./server -D port\n");
        return (-1);
    }
    if (!(server_fd = socket(AF_INET, SOCK_STREAM, 0)))
        return (-1);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(portnum);

    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
                                                  &opt, sizeof(opt));
    bind(server_fd, (struct sockaddr *)&server, sizeof(server));
    listen(server_fd, 3);

    if (num == 1)
    {
        printf("Deamonize process...\n");
        daemonize();
    }

    while (1)
    {
        client_socket = accept(server_fd, (struct sockaddr *)NULL, NULL);
        read(client_socket,buf, 1024);
        if (strcmp(buf, "exit") == 0)
        {
            write(client_socket, "exiting...\n", sizeof("exiting...\n"));
            exit (0);
        }
        write(client_socket, "pong pong\n", sizeof("pong pong\n"));
    }
    return (0);
}
