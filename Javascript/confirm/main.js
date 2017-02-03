function main()
{
    var flag = confirm("ここは田舎者なのん？"); 
	// OKが押されたら
    if (flag == true)
    {
        alert("やっぱり田舎なのんなー");
    }
	// キャンセルが押されたら
    else if (flag == false)
    {
        alert("都会なのん！");
    }
}
