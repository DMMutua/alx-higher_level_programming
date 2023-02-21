const $headerElem = $('header');
const $divRedHead = $('div#red_header');

$divRedHead.on('click', function () {
	$headerElem.addClass('red');
});
