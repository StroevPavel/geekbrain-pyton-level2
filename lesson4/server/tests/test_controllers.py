from text.controllers import (
	get_upper_text, get_lower_text
	)

def test_get_lower_text_is_lower():
	test_text = 'TEST TEXT'
	assert_text = 'test text'
	assert get_lower_text(test_text) == assert_text

def test_get_upper_text_is_lower():
	test_text = 'test text'
	assert_text = 'TEST TEXT'
	assert get_upper_text(test_text) == assert_text