var elem = document.querySelector('input[type="range"]');
    var rangeValue = function(){
    var newValue = elem.value;
    var target = document.querySelector('.value');
    target.innerHTML = newValue;
    console.log(newValue);
    }
    elem.addEventListener("input", rangeValue);
    var elem = document.querySelector('input[type="range"]');
    var ver = 50,hor = 50;

    function servo(smer) {
        var step = elem.value;
        var target = document.querySelector('.value');
        step = parseInt(target.innerHTML)
        if (smer == 'up') {
            if ((ver + step) <= 180) {
                if (ver < 180) {
                    ver = ver + step;
                    console.log(ver);
                }
            }
            else if (ver >= 180) {
                alert("MAXIMÁLNÍ ÚHEL!!!")
            }
            else {
                confirm("HROZÍ PŘESAŽENÍ MAXIMÁLNÍHO ÚHLU");
            }
        }
        else if (smer == 'down') {
            if ((ver - step) >= 0) {
                if (ver > 0) {
                    ver = ver - step;
                    console.log(ver);
                }
            }
            else if (ver <= 0) {
                alert("MINIMÁLNÍ ÚHEL!!!")
            }
            else {
                confirm("HROZÍ PŘESAŽENÍ MINIMÁLNÍHO ÚHLU");
            }
        }
        else if (smer == 'right') {
            if ((hor + step) <= 180){
                if (hor < 180) {
                    hor = hor + step;
                    console.log(hor);
                }
            }
            else if (hor >= 180) {
                alert("MAXIMÁLNÍ ÚHEL!!!")
            }
            else {
                confirm("HROZÍ PŘESAŽENÍ MAXIMÁLNÍHO ÚHLU");
            }
        }
        else if (smer == 'left') {
            if ((hor - step) >= 0){
                if (hor > 0) {
                    hor = hor - step;
                    console.log(hor);
                }
            }
            else if (hor <= 0) {
                alert("MINIMÁLNÍ ÚHEL!!!")
            }
            else {
                confirm("HROZÍ PŘESAŽENÍ MINIMÁLNÍHO ÚHLU");
            }
        }
    }
    function arrows(event) {
        var newValue = elem.value;
        var target = document.querySelector('.value');
        step = parseInt(target.innerHTML)
        arrow = event.charCode || event.keyCode
        if (arrow == 38) {
            if ((ver + step) <= 180){
                if (ver < 180) {
                    ver = ver + step;
                    console.log(ver);
                }
            }
            else if (ver >= 180) {
                alert("MAXIMÁLNÍ ÚHEL!!!")
            }
            else {
                confirm("HROZÍ PŘESAŽENÍ MAXIMÁLNÍHO ÚHLU");
            }
        }
        if (arrow == 40) {
            if ((ver - step) >= 0){
                if (ver > 0) {
                    ver = ver - step;
                    console.log(ver);
                }
            }
            else if (ver <= 0) {
                alert("MINIMÁLNÍ ÚHEL!!!")
            }
            else {
                confirm("HROZÍ PŘESAŽENÍ MINIMÁLNÍHO ÚHLU");
            }
        }
        if (arrow == 39) {
            if ((hor + step) <= 180){
                if (hor < 180) {
                    hor = hor + step;
                    console.log(hor);
                }
            }
            else if (hor >= 180) {
                alert("MAXIMÁLNÍ ÚHEL!!!")
            }
            else {
                confirm("HROZÍ PŘESAŽENÍ MAXIMÁLNÍHO ÚHLU");
            }
        }
        if (arrow == 37) {
            if ((hor - step) >= 0){
                if (hor > 0) {
                    hor = hor - step;
                    console.log(hor);
                }
            }
            else if (hor <= 0) {
                alert("MINIMÁLNÍ ÚHEL!!!")
            }
            else {
                confirm("HROZÍ PŘESAŽENÍ MINIMÁLNÍHO ÚHLU");
            }
        }
    };
    function ready() {
          window.addEventListener('keydown', arrows);
    };