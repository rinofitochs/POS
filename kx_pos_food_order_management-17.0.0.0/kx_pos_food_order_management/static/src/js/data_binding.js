/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
    /**
     * Processes the data loaded for the Point of Sale (POS) store.
     *
     * @param {Object} loadedData - The data imported for the Point of Sale (POS) system.
     * @returns {Promise} A promise that resolves upon completion of data processing.
     */
    async _processData(loadedData) {
        await super._processData(...arguments);
        this.pos_orders = loadedData['pos.order'];
        this.pos_order_lines = loadedData['pos.order.line'];
    },
});


