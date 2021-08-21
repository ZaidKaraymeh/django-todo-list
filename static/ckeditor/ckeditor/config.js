/**
 * @license Copyright (c) 2003-2021, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	CKEDITOR.config.toolbar = [
	  [
		"Styles",
		"Format",
		"Bold",
		"Italic",
		"Underline",
		"Strike",
		"SpellChecker",
		"Undo",
		"Redo",
	  ],
	  ["JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock"],
	
	  ["Link", "Unlink", "Anchor"],
	
	  ["Image", "Flash", "Table", "HorizontalRule"],
	  ["TextColor", "BGColor"],
	  ["Smiley", "SpecialChar"]
	];
}