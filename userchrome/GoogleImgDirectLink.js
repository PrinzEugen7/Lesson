(function() {

if (window != window.parent)
    return;
function handle(node) {
    var items = document.evaluate('self::a[img][contains(@href, "/imgres?")]', node, null, 7, null);
    for(var i = 0; i < items.snapshotLength; i++) {
        var a = items.snapshotItem(i);
        a.dataset.href = a.href;
        a.addEventListener('mousedown', function(e) {
            if (e.button === 1)
                window.open(e.currentTarget.dataset.href);
        }, false);
        if (/imgurl=(https?:\/\/[^&]+)/.test(decodeURIComponent(a.href)))
            a.href = RegExp.$1;
    }
}
var mo = new MutationObserver(function(records) {
    records.forEach(function(record) {
        handle(record.target);
    });
});
mo.observe(document.body, {subtree: true, attributes: true, attributeFilter: ['href']});

})();
