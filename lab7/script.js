var container = document.getElementById('container');
window.addEventListener("keyup", function(e){
    console.log(e.key);
    if (e.key == 'Escape'){
        container.textContent = "";
    }
    else if (e.key == 'Backspace'){
        var str = container.textContent;
        container.textContent = str.substring(0, str.length-1);
    } 
    else{
        container.textContent += e.key;
    }
    add_new_chars();
});

function add_new_chars(x, b = true){
    var numsize = x;
    if(b){
        numsize = Math.floor(Math.random() * x) + 1; // random number between 0 and 2, so plus 1
    }
    var rand_func = '';
    for (let i = 0; i < numsize; i++) {
        var numchars = 97 + Math.floor(Math.random() * 26); // 產生 A 到 Z 的亂數字元
        rand_func += String.fromCharCode(numchars);//轉換數字到英文
    }
    return rand_func;
};