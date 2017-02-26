// 初期化
function setYearArray(min, max)
{
  var srcArray = [];
  // srcArrayにmin～maxまでの値を挿入
	for(var i = min; i < max; i++)
	{  
        srcArray[i+'年'] = i;   
	}
	return srcArray;
}

function main()
{
  // 連想配列
  year = setYearArray(1999, 2017);
	alert(year['1999年']);
}
