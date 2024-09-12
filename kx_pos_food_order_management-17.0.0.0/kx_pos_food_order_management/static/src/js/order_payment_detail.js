/** @odoo-module **/

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";
const { Component, useState } = owl;
import { useService } from "@web/core/utils/hooks";
import { jsonrpc } from "@web/core/network/rpc_service";

/**
 * Applying a patch to the Order class to integrate custom functionality.
 */
patch(Order.prototype, {
    setup(_defaultObj, options) {
        super.setup(...arguments);
        this.orm = options.pos.orm;
        this.popup = options.pos.popup;
        this.kitchen = true;
    },
    /**
     * Override the payment method to incorporate custom payment processing logic.
     */
    async pay() {
        var order_name = this.pos.selectedOrder.uid;
        var self = this;
        await this.orm.call("pos.order", "check_order", ["", order_name]).then(function (result) {
            if (result.category) {
                var title = "No category is associated with the current order in the kitchen.(" + result.category + ')';
                self.kitchen = false;
                self.popup.add(ErrorPopup, {
                    title: _t(title),
                    body: _t("No food items are available for the specified category in this kitchen. Please remove the selected items and update the order by clicking the 'Order' button. Afterward, proceed with payment."),
                });
            } else if (result == true) {
                self.kitchen = false;
                self.popup.add(ErrorPopup, {
                    title: _t("Meal is not ready"),
                    body: _t("Please Complete all the Meal first."),
                });
            } else {
                self.kitchen = true;
            }
        });

        if (!this.orderlines.length) {
            return;
        }

        if (
            this.orderlines.some(
                (line) => line.get_product().tracking !== "none" && !line.has_valid_product_lot()
            ) &&
            (this.pos.picking_type.use_create_lots || this.pos.picking_type.use_existing_lots)
        ) {
            const { confirmed } = await this.env.services.popup.add(ConfirmPopup, {
                title: _t("Some Serial/Lot Numbers are unassigned"),
                body: _t(
                    "You are attempting to sell products with serial/lot numbers, but some are not assigned. \nDo you wish to proceed with the transaction?"
                ),
                confirmText: _t("Yes"),
                cancelText: _t("No"),
            });

            if (confirmed) {
                if (this.kitchen) {
                    this.pos.mobile_pane = "right";
                    this.env.services.pos.showScreen("PaymentScreen");
                }
            }
        } else {
            if (this.kitchen) {
                this.pos.mobile_pane = "right";
                this.env.services.pos.showScreen("PaymentScreen");
            }
        }
    }
});
