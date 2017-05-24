function katakanaToHiragana(src) {
	return src.replace(/[\u30a1-\u30f6]/g, function(match) {
		var chr = match.charCodeAt(0) - 0x60;
		return String.fromCharCode(chr);
	});
}

function sortFunc(a, b){
	a = katakanaToHiragana(a.toString());
	b = katakanaToHiragana(b.toString());
	if(b < a) return -1;
	else if(b > a) return 1;
	return 0;
}

window.onload = function () {
    array = ["エミヤ", "ジャンヌ", "アルトリア"]
    array.sort(sortFunc);
    alert(array); // ジャンヌ,エミヤ,アルトリア
}
