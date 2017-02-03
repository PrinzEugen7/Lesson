function main()
{
    var flag = confirm('吹雪「前のページに戻りますか？」'); 
	// OKが押されたら
    if (flag == true)
    {
        history.forward();
    }
}
