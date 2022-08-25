document.querySelector("#enviooo").addEventListener("submit", function(e){
    var i = document.getElementById('showinggg');
    var s = document.getElementById('spinnerrr');
    
    if (i != undefined) i.setAttribute('hidden', true);
    s.removeAttribute('hidden');
});