function deleteFunction(id, title){
    var r = confirm(`Tem certeza que deseja apagar a receita\n ${title}?`);
    if (r == true){
        location.replace("/deletar/" + id);
    }
}

function mudarCss(){
    if (document.getElementById("dica-sim").checked){
        document.getElementById('div_id_dica').style.display = "block"
    }else {
        document.getElementById('div_id_dica').style.display = "none";
    }
}
