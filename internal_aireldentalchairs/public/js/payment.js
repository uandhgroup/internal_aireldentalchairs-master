window.pay = {
	paypal_button_id: "GCJUKSH7DBJX6",
	paypal_url: "https://www.paypal.com/cgi-bin/webscr",
	paypal: function(btn) {
		var $btn = btn ? $(btn) : $(this);
		$(".paypal-form").remove();
		$('<form action="' + pay.paypal_url + '" method="post" target="_top" class="paypal-form hidden">\
			<input type="hidden" name="cmd" value="_s-xclick">\
			<input type="hidden" name="hosted_button_id" value="' + pay.paypal_button_id + '">\
			<input type="hidden" name="on0" value="Pay For">\
			<input type="hidden" name="os0" value="' + $btn.attr("data-plan") + '">\
			<input type="hidden" name="currency_code" value="USD">\
		</form>').appendTo("body").submit();
	},

	wire_transfer: function(btn, msg_selector) {
		var $btn = btn ? $(btn) : $(this);
		var msg = $(msg_selector).html();
		var amount = $(btn).attr("data-amount");
		var msg = '<p class="lead">Amount: <b>' + amount + '</b></p><hr>' + msg;
		$('.wire-transfer-dialog').remove();
		frappe.msgprint(msg, "Wire Transfer").addClass("wire-transfer-dialog");
	},
}

// var script = document.createElement( 'script' );
// script.src = "https://wchat.freshchat.com/js/widget.js"
// $("head").append(script);

// setTimeout(() => {
// 	var script = document.createElement( 'script' );
// 	script.textContent = `window.fcWidget.init({
// 		token: "2041bf4a-21c8-4921-8ff0-9cf5a49534c5",
// 		host: "https://wchat.freshchat.com"
// 	});`;
// 	script.type = "text/javascript";
// 	$("body").append( script );
// }, 2000);
