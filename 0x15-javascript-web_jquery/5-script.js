const $list_element = $('ul.my_list');
const $additem_toelem = $('div#add_item');

$additem_toelem.on('click', () => {
	$list_element.append('<li>Item</li>');
});
