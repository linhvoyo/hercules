/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   client.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: linh <marvin@42.fr>                        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/03 07:31:15 by linh              #+#    #+#             */
/*   Updated: 2018/03/03 10:51:05 by linh             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <sys/socket.h>
#include <string.h>
#include <netinet/in.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netdb.h>

int main(int argc, char **argv)
{
    argc = 0;
    int client_socket;
    struct sockaddr_in server;
    char buf[1024];
    struct hostent *host_server;

    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if(client_socket < 0)
        return (0);

    host_server = gethostbyname(argv[1]);
    if (host_server == NULL)
    {
        printf("no such host");
        return (0);
    }
    bzero((char *) &server, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_port = htons(atoi(argv[2]));
    memcpy(&server.sin_addr, host_server->h_addr, host_server->h_length);
    if ((connect(client_socket, (struct sockaddr *)&server, sizeof(server)) < 0))
        return (0);
    if ((send(client_socket, argv[3], sizeof(argv[3]), 0) < 0))
        return (0);
    printf("Sent: %s\n", argv[3]);
    read(client_socket,buf,1024);
    printf("Recieved: %s", buf);
    close(client_socket);
    return 0;
}
