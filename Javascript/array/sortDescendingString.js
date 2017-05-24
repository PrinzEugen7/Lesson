function sortFunc(a, b){
	a = a.toString().toLowerCase();
	b = b.toString().toLowerCase();
	if(b < a) return -1;
	else if(b > a) return 1;
	return 0;
}

window.onload = function () {
    array = ["Emiya", "Jannue", "Artoria"]
    array.sort(sortFunc);
    alert(array); // Jannue,Emiya,Artoria
}
