/*eslint-disable*/
"use strict";

import axios from 'axios'

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

export default class HTTPHandler {
    constructor(path) { this.path = path; }

    get(apiToken=null) {
        return Promise.resolve(
            axios.get(
                this.path, {
                headers: {
                    'Authorization': apiToken
                }
            })
        );
    }

    post(data, apiToken=null) {
        return Promise.resolve(
            axios.post(
                this.path,
                data, {
                    headers: {
                        'Authorization': apiToken
                    },
                    useCredentials: true
                }
            )
        );
    }

    delete(apiToken=null) {
        return Promise.resolve(
            axios.delete(
                this.path, {
                    headers: {
                        'Authorization': apiToken
                    }
                }  
            )
        );
    }

    patch(data, apiToken=null) {
        return Promise.resolve(
            axios.patch(
                this.path,
                data, {
                    headers: {
                        'Authorization': apiToken
                    }
                }
            )  
        );
    }
}
