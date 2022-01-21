/*eslint-disable*/
"use strict";

import HTTPHandler from '@/services/http'
import Storage from '@/services/storage'

export default class APIHandler {
    constructor() { this.storage = new Storage(window.localStorage); }

    login(username, password) {
        if (password.length > 0) {
            const http = new HTTPHandler('http://localhost:8888/api/v1/users/login');
            return Promise.resolve(
                http.post({
                        username: username,
                        password: password
                    }
                )
                    .then(response => {
                        console.log("Sooooo.....");
                        console.log(response.data.result);
                        const data = response.data.result;

                        this.storage.clear();
                        this.storage.set('token', data.token);
                        this.storage.set('role', data.role);
                        this.storage.set('id', data.id);
                    })
                    .catch(function (error) { console.log("Whoops!"); return Promise.reject(error);  })
            )
        } else {
            return Promise.reject("Password is missing!");
        }
    }

    signup(username, password, passwordConfirmation, role) {
        if (username.length == 0) {
            return Promise.reject("Username's missing!\nTry again!");
        }
        if (role.length == 0) {
            return Promise.reject("Role's missing!\nTry again!");
        }
        if ((password.length > 0) && (password === passwordConfirmation))
        {
            const http = new HTTPHandler("http://localhost:8888/api/v1/users");
            console.log(username, password, role);
            return Promise.resolve(
                http.post({
                    username: username,
                    password: password,
                    role: role
                })
                    .then(response => {
                        console.log(response.data);
                        const data = response.data.result;

                        this.storage.clear();
                        this.storage.set('token', data.token);
                        this.storage.set('role', data.role);
                        this.storage.set('id', data.id);
                    })
                    .catch((error) => {
                        return Promise.reject(error);
                    })
            );
        } else {
            return Promise.reject("Passwords do not match!\nTry again!");
        }
    }

    fetchGPs() {
        const token = this.storage.get('token');

        const http = new HTTPHandler('http://localhost:8888/api/v1/grands-prix');
        return Promise.resolve(
            http.get(token)
                .catch((error) => {
                    return Promise.reject(error);
                })
        );
    }

    addGP(title, date, userId) {
        if (title.length > 0) {
            const token = this.storage.get('token');

            const http = new HTTPHandler('http://localhost:8888/api/v1/grands-prix');
            return Promise.resolve(
                http.post({
                        "title": title,
                        "date": date,
                        "vendor_id": userId
                    },
                    token
                )
                    .catch((error) => {
                        return Promise.reject(error);
                    })
            );
        } else {
            return Promise.reject("GP title is missing!\nAdd one and try again!");
        }
    }

    deleteGP(gpId) {
        const token = this.storage.get('token');

        const http = new HTTPHandler(`http://localhost:8888/api/v1/grands-prix/${gpId}`);
        return Promise.resolve(
            http.delete(token)
                .catch((error) => {
                    Promise.reject(error);
                })
        );
    }

    fetchTickets(gpId) {
        const token = this.storage.get('token');

        const http = new HTTPHandler(`http://localhost:8888/api/v1/tickets/${gpId}`);
        return Promise.resolve(
            http.get(token)
                .catch((error) => {
                    this.storage.clear();
                    return Promise.reject(error);
                })
        );
    }

    addTicket(price, session, gpId) {
        if ((price > 0) && (session !== 0)) {
            const token = this.storage.get('token');

            const http = new HTTPHandler('http://localhost:8888/api/v1/tickets');
            return Promise.resolve(
                http.post({
                        "price": price,
                        "session": session,
                        "gp_id": gpId
                    },
                    token
                )
                    .catch((error) => {
                        return Promise.reject(error);
                    })
            );
        } else {
            return Promise.reject("Some information is missing!\nFill price & session and try again!");
        }
    }

    deleteTicket(ticketId) {
        const token = this.storage.get('token');

        const http = new HTTPHandler(`http://localhost:8888/api/v1/tickets/${ticketId}`);
        return Promise.resolve(
            http.delete(token)
                .catch((error) => {
                    return Promise.reject(error);
                })
        );
    }

    buyTicket(ticketId) {
        const token = this.storage.get('token');

        const http = new HTTPHandler('http://localhost:8888/api/v1/tickets/buy');
        return Promise.resolve(
            http.patch({
                    'ticket_id': ticketId,
                },
                token
            )
                .catch((error) => {
                    return Promise.reject(error);
                })
        );
    }
}
