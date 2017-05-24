function sortFunc(a, b){
	a = a.toString().toLowerCase();
	b = b.toString().toLowerCase();
	if(a < b) return -1;
	else if(a > b) return 1;
	return 0;
}

window.onload = function () {
    array = ["Emiya", "Jannue", "Artoria"]
    array.sort(sortFunc);
    alert(array); // Artoria,Emiya,Jannue
}
