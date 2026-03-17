"use strict";
if (-1 || 0) alert( 'first' );// works with -1
if (-1 && 0) alert( 'second' );// doesnt work with 0
if (null || -1 && 1) alert( 'third' );// works with 1