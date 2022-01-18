/*eslint-disable*/
"use strict";

export default class Storage {
    constructor(storage) { this.storage = storage; }

    set(name, value) { this.storage.setItem(name, value); }
    get(name) { return this.storage.getItem(name); }
    
    clear() { this.storage.clear(); }
}
