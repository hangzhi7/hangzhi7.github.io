(function(){
    var script = document.createElement('script');
    script.src     = "https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js";
    script.async   = false
    script.defer   = true

    document.head.appendChild(script);
    script.onload = function() {
        fmtBusuanzi();
    }
})();

let jx = false;

function fmtBusuanzi () {
    setTimeout(function(){
        const bszUV = document.getElementById('busuanzi_value_site_uv');
        if (bszUV) {
            bszUV.innerText = jx? numberFormat(bszUV.innerText):bszUV.innerText;
        }
        const bszPV = document.getElementById('busuanzi_value_site_pv');
        if (bszPV) {
            bszPV.innerText = jx? numberFormat(bszPV.innerText):bszPV.innerText;
        }
        const bszPPV = document.getElementById('busuanzi_value_page_pv');
        if (bszPPV) {
            bszPPV.innerText = jx?  numberFormat(bszPPV.innerText):bszPPV.innerText;
        }
    }, 800);
}

function numberFormat (number) {
    let result;
    if (number.indexOf(',') > 0) {
        number = number.replaceAll(",", "");
    }

    if (number > 10000) {
        result = (number / 10000.0).toFixed(2) + ' w';
    } else if (number > 1000) {
        result = (number / 1000.0).toFixed(2) + ' k';
    } else {
        result = number;
    }
    return result;
}