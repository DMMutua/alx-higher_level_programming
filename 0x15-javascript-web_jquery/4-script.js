const $headerelement = $('header');
const $divredhead = $('DIV#toggle_header');

$divredhead.on('click', () => {
	const current_class = $headerelement.attr('class');

	if (current_class == 'green') {
		$headerelement.toggleClass(`${current_class} red`);
	}

	if (current_class == 'red') {
		$headerelement.toggleClass(`${current_class} green`);
	}
});
