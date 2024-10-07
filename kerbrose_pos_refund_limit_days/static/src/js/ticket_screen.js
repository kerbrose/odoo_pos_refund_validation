/** @odoo-module */

import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";



patch(TicketScreen.prototype, {
    onClickOrder(clickedOrder) {
        let limitDays = clickedOrder.pos.config.limit_days_return;
        let numberOfDays = clickedOrder.pos.config.return_number_of_days;
        let orderDate = clickedOrder.date_order;
        let now = luxon.DateTime.now();
        let numberOfDaysOrder = now.diff(orderDate, "days").days;
        if (limitDays && numberOfDaysOrder > numberOfDays) {
            this.popup.add(ErrorPopup, {
                title: _t('Error'),
                body: _t('The Order Exceeds refund Policy Days'),
            });
            
        } else {
            super.onClickOrder(...arguments);
        }
    },
});
