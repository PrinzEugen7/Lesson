window.onload = function () {
    var fixedTag = $(".admin");
    var footer = $(".footer");
    var fixedTagHeight = fixedTag.outerHeight(true);
    var fixedTagTop = fixedTag.offset().top;
    $(window).scroll(function(){
        var scrollTop = $(this).scrollTop();
        if(scrollTop > fixedTagTop){
            var footerTop = footer.offset().top;           
            if(scrollTop + fixedTagHeight > footerTop){
                customTopPosition = footerTop - (scrollTop + fixedTagHeight)
                fixedTag.css({position: "fixed", top:  customTopPosition + "px"});
            }else{
                fixedTag.css({position: "fixed", top: "10px"});
            }
        }else{
            fixedTag.css({position: "static", top: "auto"});
        }
    });
};